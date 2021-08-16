global X, Y, Alt


def init(alt):
    X.set = 0
    Y.set = 0
    Alt.set = alt | 0


def update(x, y, alt):
    X.set = x
    Y.set = y
    Alt.set = alt


def movecoords(x, y, alt):
    X.set = x
    Y.set = y
    Alt.set = alt


def move(code, dist):
    match code:
        case "forward":
            movecoords(dist)
        case "back":
            movecoords(-dist)
        case "left":
            movecoords(0, dist)
        case "right":
            movecoords(0, -dist)
        case "up":
            movecoords(0, 0, dist)
        case "down":
            movecoords(0, 0, -dist)


def get_coords():
    return {
        "x": X,
        "y": Y,
        "alt": Alt
    }


def get_x(): return X


def get_y(): return Y


def get_alt(): return Alt
