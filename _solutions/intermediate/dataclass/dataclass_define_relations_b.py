
@dataclass
class User:
    firstname: str
    lastname: str
    role: str
    username: str
    password: str
    email: str
    born: date
    last_login: datetime | None
    is_active: bool
    is_staff: bool
    is_superuser: bool
    user_permissions: list[dict]
