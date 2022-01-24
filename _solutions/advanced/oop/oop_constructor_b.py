
from dataclasses import dataclass


@dataclass
class Account:
    username: str
    uid: int

    def __new__(cls, username: str, uid: int):
        if uid < 1000:
            return object.__new__(SystemAccount)
        else:
            return object.__new__(UserAccount)


class UserAccount(Account):
    pass

class SystemAccount(Account):
    pass


result = [Account(username, int(uid))
          for line in DATA.splitlines()
          if (record := line.strip().split(':'))
          if (username := record[0])
          and (uid := record[2])]
