import uuid


class BankAccount:

    def __init__(self, customer_name: str):
        self.owner = customer_name

        self.money = 0

        self.id = str(uuid.uuid4())

        self.transactions = []

    def deposit_money(self, summa: int):
        self.money += summa

        self.transactions.append(f'deposit amount {summa}')