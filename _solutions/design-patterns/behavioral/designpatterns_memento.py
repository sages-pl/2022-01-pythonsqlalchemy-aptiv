
@dataclass
class Transaction:
    __amount: Final[float]

    def get_amount(self):
        return self.__amount


@dataclass
class History:
    __transactions: list[Transaction] = field(default_factory=list)

    def push(self, transaction: Transaction) -> None:
        self.__transactions.append(transaction)

    def pop(self) -> Transaction:
        return self.__transactions.pop()


@dataclass
class Account:
    __balance: float = 0

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance

    def save(self):
        return Transaction(self.__balance)

    def undo(self, transaction: Transaction):
        self.__balance = transaction.get_amount()
