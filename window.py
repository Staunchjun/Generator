from resolution import Resolution, init_resolution
from common import mm_to_resolution, singleton


@singleton
class Window:
    """
    开窗设置类
    x,y默认为mm
    """

    @property
    def x(self) -> float:
        return self._size_x

    @property
    def y(self) -> float:
        return self._size_y

    @init_resolution
    def __init__(self, x: float, y: float, resolution: Resolution = None):
        self._size_x = x
        self._size_y = y
        self._resolution = resolution

    def get_x_resolution(self) -> int:
        """
        获取x方向像素
        :return: x resolution
        """
        return mm_to_resolution(self._size_x, self._resolution.x)

    def get_y_resolution(self):
        """
        获取y方向像素
        :return: y resolution
        """
        return mm_to_resolution(self._size_y, self._resolution.y)

    def __str__(self):
        print("======Print window var:======")
        print("size_x_mm: ", self._size_x)
        print("size_y_mm: ", self._size_y)
        print("x_resolution: ", self.get_x_resolution())
        print("y_resolution: ", self.get_y_resolution())
        self._resolution.__str__()


