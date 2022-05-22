from functools import wraps

from common import singleton


@singleton
class GraphConf:

    @property
    def window_space_x(self):
        return self._window_space_x

    @window_space_x.setter
    def window_space_x(self, a):
        self._window_space_x = a

    @property
    def window_space_y(self):
        return self._window_space_y

    @window_space_y.setter
    def window_space_y(self, a):
        self._window_space_y = a

    @property
    def window_num_x(self):
        return self._window_num_x

    @window_num_x.setter
    def window_num_x(self, a):
        self._window_num_x = a

    @property
    def window_num_y(self):
        return self._window_num_y

    @window_num_y.setter
    def window_num_y(self, a):
        self._window_num_y = a

    @property
    def padding_x(self):
        return self._padding_x

    @padding_x.setter
    def padding_x(self, a):
        self._padding_x = a

    @property
    def padding_y(self):
        return self._padding_x

    @padding_y.setter
    def padding_y(self, a):
        self._padding_y = a

    def __init__(self):
        self._window_space_x = 1562.5 / 1000
        self._window_space_y = 1562.5 / 1000
        self._window_num_x = 108
        self._window_num_y = 96
        self._padding_x = 1
        self._padding_y = 1


@singleton
class WindowConf:
    @property
    def window_size_x(self):
        return self._window_size_x

    @window_size_x.setter
    def window_size_x(self, a):
        self._window_size_x = a

    @property
    def window_size_y(self):
        return self._window_size_y

    @window_size_y.setter
    def window_size_y(self, a):
        self._window_size_y = a

    def __init__(self):
        self._window_size_x = 0.72
        self._window_size_y = 0.41


@singleton
class ResolutionConf:
    @property
    def resolution_x(self):
        return self._resolution_x

    @resolution_x.setter
    def resolution_x(self, a):
        self._resolution_x = a

    @property
    def resolution_y(self):
        return self._resolution_y

    @resolution_y.setter
    def resolution_y(self, a):
        self._resolution_y = a

    def __init__(self):
        self._resolution_x = 1080.86
        self._resolution_y = 1441.13


def inject_resolution_conf(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not kwargs.get('conf'):
            kwargs['conf'] = ResolutionConf()
        f(*args, **kwargs)

    return decorated


def inject_window_conf(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not kwargs.get('conf'):
            kwargs['conf'] = WindowConf()
        f(*args, **kwargs)

    return decorated


def inject_graph_conf(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not kwargs.get('conf'):
            kwargs['conf'] = GraphConf()
        f(*args, **kwargs)

    return decorated
