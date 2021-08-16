global X, Y, Alt


def init(alt):
    X.set = 0
    Y.set = 0
    Alt.set = alt | 0


def update(x, y, alt):
    X.set = x
    Y.set = y
    Alt.set = alt


def shift(x, y, alt):
    X.set = x
    Y.set = y
    Alt.set = alt


def get_coords():
    return {
        "x": X,
        "y": Y,
        "alt": Alt
    }


def get_x(): return X


def get_y(): return Y


def get_alt(): return Alt
