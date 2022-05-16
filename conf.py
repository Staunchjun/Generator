from functools import wraps

from common import singleton


@singleton
class GraphConf:
    def __init__(self):
        self.window_space_x = 1562.5 / 1000
        self.window_space_y = 1562.5 / 1000
        self.window_num_x = 108
        self.window_num_y = 96
        self.padding_x = 1
        self.padding_y = 1


@singleton
class WindowConf:
    def __init__(self):
        self.window_size_x = 30
        self.window_size_y = 23


@singleton
class ResolutionConf:
    def __init__(self):
        self.resolution_x = 1080.86
        self.resolution_y = 1441.13


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
