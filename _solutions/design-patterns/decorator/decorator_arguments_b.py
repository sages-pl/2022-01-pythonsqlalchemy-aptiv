
def check_astronauts(field, value):
    def decorator(func):
        def wrapper(crew):
            for member in crew:
                if member.get(field) != value:
                    name = member['name']
                    raise PermissionError(f'{name} is not an astronaut')
            return func(crew)
        return wrapper
    return decorator
