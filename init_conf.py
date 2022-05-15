from functools import wraps

from resolution import Resolution
from window import Window


def init_window(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not kwargs.get('window'):
            # todo load window conf
            kwargs['window'] = Window(0.72, 0.41)
        f(*args, **kwargs)

    return decorated


def init_resolution(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not kwargs.get('resolution'):
            # todo load resolution conf
            kwargs['resolution'] = Resolution(1451.43, 1441.12)
        f(*args, **kwargs)

    return decorated