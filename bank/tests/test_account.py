import pytest
from bank.account import Account


class TestAccount:
    def test_newly_opened_account_has_zero_balance(self):
        account = Account()
        account.open()
        assert account.get_balance() == 0

    def test_open_account(self):
        account = Account()
        account.open()
        assert account.is_opened

    def test_open_already_opened_account(self):
        account = Account()
        account.open()
        with pytest.raises(ValueError):
            account.open()

    def test_close_opened_account(self):
        account = Account()
        account.open()
        account.close()
        assert not account.is_opened

    def test_close_already_closed_account(self):
        account = Account()
        with pytest.raises(ValueError):
            account.close()

    def test_open_closed_account(self):
        account = Account()
        account.open()
        account.deposit(10)
        account.close()
        account.open()
        assert account.is_opened
        assert account.get_balance() == 10

    def test_get_balance_if_account_is_closed(self):
        account = Account()
        with pytest.raises(ValueError):
            account.get_balance()

    def test_get_balance_if_account_is_opened(self):
        account = Account()
        account.open()
        assert account.get_balance() == 0

    def test_get_balance_after_deposit(self):
        account = Account()
        account.open()
        account.deposit(120)
        assert account.get_balance() == 120

    def test_get_balance_after_withdraw(self):
        account = Account()
        account.open()
        account.deposit(150)
        account.withdraw(120)
        assert account.get_balance() == 30

    def test_deposit_if_account_is_closed(self):
        account = Account()
        with pytest.raises(ValueError):
            account.deposit(10)

    def test_deposit_with_negative_amount(self):
        account = Account()
        account.open()
        with pytest.raises(ValueError):
            account.deposit(-1)
        assert account.get_balance() == 0

    def test_deposit_for_closed_account(self):
        account = Account()
        with pytest.raises(ValueError):
            account.deposit(120)

    def tests_add_deposit_if_account_is_opened(self):
        account = Account()
        account.open()
        account.deposit(120)
        assert account.get_balance() == 120

    def test_withdraw_from_opened_account_if_balance_is_below_zero(self):
        account = Account()
        account.open()
        with pytest.raises(ValueError):
            account.withdraw(120)
        assert account.get_balance() == 0

    def test_withdraw_from_opened_account(self):
        account = Account()
        account.open()
        account.deposit(120)
        account.withdraw(70)
        assert account.get_balance() == 50

    def test_withdraw_negative_amount(self):
        account = Account()
        account.open()
        account.deposit(10)
        with pytest.raises(ValueError):
            account.withdraw(-1)
        assert account.get_balance() == 10
