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
        pass

    def get_balance(self):
        pass

    def open(self):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def close(self):
        pass