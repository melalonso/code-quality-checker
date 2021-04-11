from src.utils.timer import Timer


def timed(method):
    def wrapper(self, *args, **kwargs):
        timer = Timer()
        # before the method call
        timer.start()
        # the actual method call
        result = method(self, *args, **kwargs)
        # after the method call
        timer.stop(method.__name__)

        return result

    return wrapper
