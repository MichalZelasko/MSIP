from project import Configuration

conf = Configuration()

def zip_arrays(A, B):
    assert len(A) == len(B)
    C             =  []
    for i, a in enumerate(A):
        C.append((a, B[i]))
    return C

def rescale_x(a):
    low   = conf.min_x
    range = conf.max_x - low
    res   = low + range * a / conf.scale
    return res

def rescale_y(a):
    low   = conf.min_y
    range = conf.max_y - low
    res   = low + range * a / conf.scale
    return res

def do_rescale_x(a):
    if a >= 0.0        and a <= conf.scale:
        return rescale_x(a)
    if a >= conf.min_x and a <= conf.max_x:
        return a
    return None

def do_rescale_y(a):
    if a >= 0.0        and a <= conf.scale:
        return rescale_y(a)
    if a >= conf.min_y and a <= conf.max_y:
        return a
    return None