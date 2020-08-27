import pytest
from bank.account import Account


@pytest.fixture
def new_account():
    account = Account()
    return account


@pytest.fixture
def opened_account():
    account = Account()
    account.open()
    return account


@pytest.fixture
def closed_account():
    account = Account()
    account.open()
    account.close()
    return account
