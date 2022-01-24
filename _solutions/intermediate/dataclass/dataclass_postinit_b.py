
@dataclass
class User:
    firstname: str
    lastname: str
    role: str
    username: str
    password: str
    email: str
    born: date
    last_login: Optional[datetime]
    is_active: bool
    is_staff: bool
    is_superuser: bool
    user_permissions: list[dict]

    def __post_init__(self):
        self.last_login = datetime.fromisoformat(self.last_login) if self.last_login else None
        self.born = date.fromisoformat(self.born) if self.born else None
