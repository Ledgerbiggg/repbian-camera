import time

from util.uuid import get_time_uid
from camera.videotape import *

from camera.video_converter import *
from concurrent.futures import ThreadPoolExecutor


class Recording:
    def __init__(self):
        pass

    @staticmethod
    def record_video(
            timeout: int = 10000
    ):
        i = 1
        v = Videotape(
            timeout=timeout,
            rotation=90
        )
        vc = VideoConverter()
        executor = ThreadPoolExecutor(max_workers=1)
        while True:
            print(f"开始录制第{i}视频")
            v.record_video(f"video{i}.h264")
            time.sleep(1)
            executor.submit(
                vc.convert_to_mp4,
                input_file=f"video{i}.h264",
                output_file=f"{get_time_uid()}.mp4",
            )  # 在后台线程中执行视频转换
            i += 1
