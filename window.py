from functools import wraps

from conf import inject_window_conf, WindowConf
from resolution import Resolution, inject_resolution
from common import mm_to_resolution


def inject_window(f):
    """
    window类的依赖注入包装方法
    :param f: 注入对象函数
    :return:
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        if not kwargs.get('window'):
            # todo load window conf
            kwargs['window'] = Window()
        f(*args, **kwargs)

    return decorated


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

    @inject_window_conf
    @inject_resolution
    def __init__(self, conf: WindowConf = None, resolution: Resolution = None):
        self._size_x = conf.window_size_x
        self._size_y = conf.window_size_y
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
