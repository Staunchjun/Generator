from common import singleton


@singleton
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

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __str__(self):
        print("======Print resolution var:======")
        print("x: ", self._x)
        print("y: ", self._y)


