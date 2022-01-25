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


original_video_path = join(debug_folder, 'original.ts')
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
        check_output(
            f'ffmpeg -i "{temporary_path}" -c copy '
            f'-bsf:v h264_mp4toannexb -f mpegts "{original_video_path}"')


width_in_pixels, height_in_pixels = check_output(
    'ffprobe -v error -select_streams v:0 '
    '-show_entries stream=width,height -of csv=p=0 '
    f'{original_video_path}'
).splitlines()[0].split(',')


image_video_path = join(debug_folder, 'image.ts')
image_video_scale = ','.join([
    f'{width_in_pixels}:{height_in_pixels}:force_original_aspect_ratio=1',
    f'pad={width_in_pixels}:{height_in_pixels}:(ow-iw)/2:(oh-ih)/2',
])
check_output(
    f'ffmpeg -y -loop 1 -i "{image_path}" '
    f'-f lavfi -i aevalsrc=0 -shortest '
    f'-t {image_time_in_seconds} '
    f'-vf scale={image_video_scale} '
    f'"{image_video_path}"')


final_video_path = join(output_folder, 'video.ts')
subprocess.run([
    'cat',
    image_video_path,
    original_video_path,
], stdout=open(final_video_path, 'wb'))
