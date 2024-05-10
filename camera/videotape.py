import subprocess


class Videotape:
    def __init__(
            self,
            width: int = 1920,
            height: int = 1080,
            timeout: int = 10000,
            bitrate: int = 10000000,
            rotation: int = 0,
    ):
        self._main_command = "libcamera-vid"
        self._o_parameter = "-o"
        self._w_parameter = "--width"
        self._h_parameter = "--height"
        self._bitrate_parameter = "--bitrate"
        self._timeout_parameter = "--timeout"
        self._rotation_parameter = "--rotation"
        self._width = width
        self._height = height
        self._bitrate = bitrate
        self._timeout = timeout
        self._rotation = rotation

    def record_video(self, output_file: str):
        command = [self._main_command, self._o_parameter, output_file]
        command.extend([self._w_parameter, str(self._width)])
        command.extend([self._h_parameter, str(self._height)])
        command.extend([self._bitrate_parameter, str(self._bitrate)])
        command.extend([self._timeout_parameter, str(self._timeout)])
        command.extend([self._rotation_parameter, str(self._rotation)])
        print(f"指令集是:{command}")
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"命令执行失败: {e}")


