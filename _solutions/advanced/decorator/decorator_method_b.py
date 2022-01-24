
def if_alive(method):
    def wrapper(self, *args, **kwargs):
        if self.current_health > 0:
            return method(self, *args, **kwargs)
        else:
            raise RuntimeError('Hero is dead and cannot make damage')

    return wrapper
