
@dataclass
class HasHealth:
    HEALTH_MIN: int = 10
    HEALTH_MAX: int = 20
    _health: int = 0

    def __post_init__(self) -> None:
        self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

    def is_alive(self) -> bool:
        return self._health > 0

    def is_dead(self) -> bool:
        return self._health <= 0


@dataclass
class HasPosition:
    _position_x: int = 0
    _position_y: int = 0

    def position_set(self, x: int, y: int) -> None:
        self._position_x = x
        self._position_y = y

    def position_change(self, right=0, left=0, down=0, up=0):
        x = self._position_x + right - left
        y = self._position_y + down - up
        self.position_set(x, y)

    def position_get(self) -> tuple:
        return self._position_x, self._position_y


class Hero(HasHealth, HasPosition):
    pass
