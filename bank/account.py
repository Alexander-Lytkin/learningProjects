"""
Банковский счет поддерживает:
 - открытие - open,
 - закрытие - close,
 - пополнение - deposit,
 - списание - withdraw,
 - получение баланса - get_balance.
При открытии счет имеет баланс 0. Баланс счета не может быть меньше 0.
Операции пополнения, списания и получение баланса невозможно выполнить для
неоткрытого или закрытого счета. Нельзя выполнить открытие открытого или
закрытие закрытого или неоткрытого счета. В этих случаях получеаем
исключение ValueError.
Закрытый счет равен неоткрытому счету, его можно повторно открыть.
Необходимо релизовать методы класса Account, а также тестовые кейсы
в bank/tests/test_account.py, используя pytest (несколько примеров уже имеется)
Рекомендуется все необходимые условия описать сначала в тестах, проверить что
тесты не проходят и только затем реализовывать методы класса Account.
"""


class Account:
    def __init__(self):
        self._balance = 0
        self._is_opened = False

    @property
    def is_opened(self):
        return self._is_opened

    def get_balance(self):
        self._check_opened()
        return self._balance

    def open(self):
        self._check_if_account_is_already_opened()
        self._is_opened = True

    def deposit(self, amount):
        self._check_opened()
        self._check_amount_more_than_zero(amount)
        self._balance += amount

    def withdraw(self, amount):
        self._check_opened()
        self._check_amount_more_than_zero(amount)
        self._check_balance_before_withdraw(amount)
        self._balance -= amount

    def close(self):
        self._check_opened()
        self._is_opened = False

    def _check_opened(self):
        if not self._is_opened:
            raise ValueError("Для операции счёт должен быть открыт")

    @staticmethod
    def _check_amount_more_than_zero(amount):
        if amount < 0:
            raise ValueError("Нельзя ввести отрицательное значение")

    def _check_balance_before_withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Недостаточно средств для списания")

    def _check_if_account_is_already_opened(self):
        if self._is_opened:
            raise ValueError("Счет уже открыт")
