import time

def printed(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s}: {} - took {:.3f} ms'.format(f.__name__, ret, (time2 - time1) * 1000.0))

        return ret
    return wrap