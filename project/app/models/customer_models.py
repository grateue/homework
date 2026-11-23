from models.bank_models import BankAccount





class TestCreateBankAccount:

    def test_create_account(self):

        account = BankAccount('борис')

        assert account.money == 0

        assert account.owner == 'Борис'

        assert account.id

        assert not account.transactions



    def test_create_account2(self):

        account = BankAccount('        борис2')

        assert account.money == 0

        assert account.owner == 'Борис2'

        assert account.id

        assert not account.transactions



class TestDepositMoney:

    def test_deposit_positive_summa(self):

        account = BankAccount('борис')

        account.deposit_money(200)

        assert account.money == 200

        assert len(account.transactions) == 1

        print(account.__dict__)