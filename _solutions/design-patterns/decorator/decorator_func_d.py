
def check_astronauts(func):
    def wrapper(crew):
        for member in crew:
            if not member['is_astronaut']:
                raise PermissionError(f'{member["name"]} is not an astronaut')
        return func(crew)
    return wrapper
