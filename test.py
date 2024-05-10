from camera.video_converter import VideoConverter
from util.uuid import get_time_uid

vc = VideoConverter()

i = 10

for e in range(i):
    f = f"video{e+1}.h264"
    print(f)
    vc.convert_to_mp4(f, f"{get_time_uid()}.mp4")
