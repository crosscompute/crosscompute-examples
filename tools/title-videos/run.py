import json
import shlex
import shutil
import subprocess
from glob import glob
from invisibleroads_macros_disk import TemporaryStorage
from os.path import abspath, basename, exists, join, splitext
from sys import argv
from urllib.request import urlretrieve as download_url
from youtube_dl import YoutubeDL


def check_output(command_string):
    print(command_string)
    stdout_bytes = subprocess.check_output(shlex.split(command_string))
    return stdout_bytes.decode('utf-8').strip()


input_folder, output_folder, log_folder, debug_folder = argv[1:]
variables = json.load(open(join(input_folder, 'variables.dictionary'), 'rt'))
image_url = variables['image_url']
image_time_in_seconds = variables['image_time_in_seconds']
video_url = variables['video_url']


image_path = join(debug_folder, basename(image_url))
download_url(image_url, image_path)


original_video_path = join(debug_folder, 'original.mp4')
if not exists(original_video_path):
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
        shutil.move(temporary_path, original_video_path)


channel_layout = check_output(
    f'ffprobe -show_entries stream=channel_layout -select_streams a:0 '
    f'-of csv=p=0 {original_video_path}')
width_in_pixels, height_in_pixels = check_output(
    'ffprobe -v error -select_streams v:0 '
    '-show_entries stream=width,height -of csv=p=0 '
    f'{original_video_path}'
).split(',')


image_video_path = join(debug_folder, 'image.mp4')
image_video_scale = ','.join([
    f'{width_in_pixels}:{height_in_pixels}:force_original_aspect_ratio=1',
    f'pad={width_in_pixels}:{height_in_pixels}:(ow-iw)/2:(oh-ih)/2',
])
check_output(
    f'ffmpeg -y -loop 1 -i {image_path} '
    f'-f lavfi -i anullsrc=channel_layout={channel_layout} -shortest '
    f'-t {image_time_in_seconds} '
    f'-vf format=yuv420p,scale={image_video_scale} '
    f'{image_video_path}')


paths = [image_video_path, original_video_path]
rows = ["file '%s'" % abspath(_) for _ in paths]
files_path = join(debug_folder, 'files.txt')
open(files_path, 'wt').write('\n'.join(rows))
final_video_path = join(output_folder, 'video.mp4')
check_output(
    f'ffmpeg -y -f concat -safe 0 -i {files_path} -c copy '
    f'{final_video_path}')
