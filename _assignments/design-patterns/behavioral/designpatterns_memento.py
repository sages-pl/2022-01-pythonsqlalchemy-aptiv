"""
* Assignment: DesignPatterns Behavioral Memento
* Complexity: medium
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Implement Memento pattern
    2. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec Memento
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> account = Account()
    >>> history = History()

    >>> account.deposit(100.00)
    >>> history.push(account.save())
    >>> account.get_balance()
    100.0

    >>> account.deposit(50.00)
    >>> history.push(account.save())
    >>> account.get_balance()
    150.0

    >>> account.deposit(25.00)
    >>> account.get_balance()
    175.0

    >>> account.undo(history.pop())
    >>> account.get_balance()
    150.0

"""
from dataclasses import dataclass, field
from typing import Final


@dataclass
class Transaction:
    def get_amount(self):
        raise NotImplementedError


@dataclass
class History:
    def push(self, transaction: Transaction) -> None:
        raise NotImplementedError

    def pop(self) -> Transaction:
        raise NotImplementedError


@dataclass
class Account:
    def deposit(self, amount: float) -> None:
        raise NotImplementedError

    def get_balance(self) -> float:
        raise NotImplementedError

    def save(self):
        raise NotImplementedError

    def undo(self, transaction: Transaction):
        raise NotImplementedError


