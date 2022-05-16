from functools import wraps

from conf import ResolutionConf, inject_resolution_conf


def inject_resolution(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not kwargs.get('resolution'):
            kwargs['resolution'] = Resolution()
        f(*args, **kwargs)

    return decorated


class Resolution:
    """
    分辨率设置类
    """

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @inject_resolution_conf
    def __init__(self, conf: ResolutionConf = None):
        self._x = conf.resolution_x
        self._y = conf.resolution_y

    def __str__(self):
        print("======Print resolution var:======")
        print("x: ", self._x)
        print("y: ", self._y)
