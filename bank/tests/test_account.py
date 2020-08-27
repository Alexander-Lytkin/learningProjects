import pytest


class TestAccount:
    def test_open_account(self, opened_account):
        assert opened_account.is_opened

    def test_new_account_has_zero_balance(self, opened_account):
        assert opened_account.get_balance() == 0

    def test_open_already_opened_account(self, opened_account):
        with pytest.raises(ValueError):
            opened_account.open()

    def test_close_opened_account(self, opened_account):
        opened_account.close()
        assert not opened_account.is_opened

    def test_close_already_closed_account(self, new_account):
        with pytest.raises(ValueError):
            new_account.close()

    def test_open_closed_account(self, closed_account):
        closed_account.open()
        closed_account.deposit(120)
        assert closed_account.is_opened
        assert closed_account.get_balance() == 120

    def test_get_balance_if_account_is_closed(self, new_account):
        with pytest.raises(ValueError):
            new_account.get_balance()

    def test_get_balance_if_account_is_opened(self, opened_account):
        assert opened_account.get_balance() == 0

    def test_get_balance_after_deposit(self, opened_account):
        opened_account.deposit(20)
        assert opened_account.get_balance() == 20

    def test_get_balance_after_withdraw(self, opened_account):
        opened_account.deposit(120)
        opened_account.withdraw(50)
        assert opened_account.get_balance() == 70

    def test_deposit_if_account_is_closed(self, new_account):
        with pytest.raises(ValueError):
            new_account.deposit(10)

    def test_deposit_with_negative_amount(self, opened_account):
        with pytest.raises(ValueError):
            opened_account.deposit(-1)
        assert opened_account.get_balance() == 0

    def test_deposit_for_closed_account(self, new_account):
        with pytest.raises(ValueError):
            new_account.deposit(120)

    def tests_add_deposit_if_account_is_opened(self, opened_account):
        opened_account.deposit(120)
        assert opened_account.get_balance() == 120

    def test_withdraw_from_opened_account_if_balance_is_below_zero(
        self, opened_account
    ):
        with pytest.raises(ValueError):
            opened_account.withdraw(120)
        assert opened_account.get_balance() == 0

    def test_withdraw_from_opened_account(self, opened_account):
        opened_account.deposit(120)
        opened_account.withdraw(50)
        assert opened_account.get_balance() == 70

    def test_withdraw_negative_amount(self, opened_account):
        opened_account.deposit(120)
        with pytest.raises(ValueError):
            opened_account.withdraw(-1)
        assert opened_account.get_balance() == 120
