import subprocess


class Shot:

    def __init__(
            self,
            pic_name: str,
            width: int = 3280,
            height: int = 2464,
            timeout: int = 0
    ):
        self._main_command = "libcamera-jpeg"
        self._o_parameter = "-o"
        self._w_parameter = "--width"
        self._h_parameter = "--height"
        self._timeout_parameter = "--timeout"
        self._pic_name = pic_name
        self._width = width
        self._height = height
        self._timeout = timeout

    def photograph(self, ):
        command = [self._main_command, self._o_parameter, self._pic_name]
        command.extend([self._w_parameter, str(self._width)])
        command.extend([self._h_parameter, str(self._height)])
        command.extend([self._timeout_parameter, str(self._timeout)])
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"命令执行失败: {e}")

#
# if __name__ == '__main__':
#     shot = Shot(
#         pic_name="test.jpg",
#         width=640,
#         height=480,
#         timeout=5
#     )
#     shot.photograph()
