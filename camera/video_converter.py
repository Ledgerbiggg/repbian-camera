import os
import subprocess

from util.uuid import get_today_date_string


class VideoConverter:
    def __init__(self):
        pass

    def convert_to_mp4(self, input_file: str, output_file: str):
        data_str = get_today_date_string()
        # 构建ffmpeg命令来转换视频格式
        subprocess.run(["mkdir", "-p", "video"])
        subprocess.run(["mkdir", "-p", "video/" + data_str])
        output_file = os.path.join("video", data_str, output_file)
        command = ['ffmpeg', '-f', 'h264', '-i', input_file, '-vcodec', 'copy', output_file]
        try:
            subprocess.run(command, check=True)
            print(f"转换成功: {input_file} 到 {output_file}")
            self._remove_input_file(input_file)
        except subprocess.CalledProcessError as e:
            print(f'ffmpeg执行出错:{e}')

    @staticmethod
    def _remove_input_file(input_file: str):
        # 构建命令来删除原视频文件
        command = ['rm', '-f', input_file]
        try:
            subprocess.run(command, check=True)
            print(f"删除文件成功: {input_file}")
        except subprocess.CalledProcessError as e:
            print('ffmpeg执行出错:', e)
