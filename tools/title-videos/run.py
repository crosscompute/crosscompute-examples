import json
import shutil
import subprocess
from glob import glob
from invisibleroads_macros_disk import TemporaryStorage
from os.path import abspath, basename, join, splitext
from sys import argv
from urllib.request import urlretrieve as download_url
from youtube_dl import YoutubeDL


input_folder, output_folder, log_folder, debug_folder = argv[1:]
variables = json.load(open(join(input_folder, 'variables.dictionary'), 'rt'))
image_url = variables['image_url']
image_time_in_seconds = variables['image_time_in_seconds']
video_url = variables['video_url']


image_path = join(output_folder, basename(image_url))
download_url(image_url, image_path)


with TemporaryStorage() as s:
    temporary_folder = s.folder
    video_path_template = join(temporary_folder, '%(title)s.%(ext)s')
    with YoutubeDL({
        'format': 'mp4',
        'outtmpl': video_path_template,
    }) as y:
        y.download([video_url])
    temporary_paths = glob(join(temporary_folder, '*'))
    temporary_path = temporary_paths[0]
    video_extension = splitext(temporary_path)[1]
    original_video_path = join(output_folder, 'original' + video_extension)
    shutil.move(temporary_path, original_video_path)


width_in_pixels, height_in_pixels = subprocess.check_output([
    'ffprobe',
    '-v', 'error',
    '-select_streams', 'v:0',
    '-show_entries', 'stream=width,height',
    '-of', 'csv=p=0',
    original_video_path,
]).decode('utf-8').strip().split(',')


image_video_path = join(debug_folder, 'image' + video_extension)
subprocess.run([
    'ffmpeg', '-y',
    '-framerate', f'1/{image_time_in_seconds}',
    '-i', image_path,
    '-f', 'lavfi', '-i', 'aevalsrc=0', '-shortest',
    '-c:v', 'libx264',
    '-t', str(image_time_in_seconds),
    '-pix_fmt', 'yuv420p',
    '-vf', 'scale=' + ','.join([
        f'{width_in_pixels}:{height_in_pixels}:force_original_aspect_ratio=1',
        f'pad={width_in_pixels}:{height_in_pixels}:(ow-iw)/2:(oh-ih)/2',
    ]),
    image_video_path,
])


paths = [image_video_path, original_video_path]
rows = ["file '%s'" % abspath(_) for _ in paths]
files_path = join(debug_folder, 'files.txt')
open(files_path, 'wt').write('\n'.join(rows))
subprocess.run([
    'ffmpeg', '-y',
    '-f', 'concat',
    '-safe', '0',
    '-i', files_path,
    '-c', 'copy',
    join(output_folder, 'video.mp4'),
])
