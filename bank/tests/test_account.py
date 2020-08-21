import pytest
from bank.account import Account


class TestAccount:
    def test_newly_opened_account_has_zero_balance(self):
        account = Account()
        account.open()
        assert account.get_balance() == 0

    def test_close_already_closed_account(self):
        account = Account()
        with pytest.raises(ValueError):
            account.close()
