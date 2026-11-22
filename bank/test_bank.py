import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount("ნინო", 100)


def test_initial_state(account):
    assert account.owner == "ნინო"
    assert account.balance == 100


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70


def test_withdraw_too_much(account):
    with pytest.raises(ValueError):
        account.withdraw(500)
    assert account.balance == 100


@pytest.mark.parametrize("amount", [0, -50])
def test_deposit_invalid(account, amount):
    with pytest.raises(ValueError):
        account.deposit(amount)