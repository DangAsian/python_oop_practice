class BankAccount:
    pass

    interest_rate = 1.13
    account = []

    @classmethod
    def create(cls):
        ac = BankAccount()
        cls.account.append(ac)
        return ac

    @classmethod
    def total_funds(cls):
        total = 0
        for account in cls.account:
            total += account.balance
        return total


    @classmethod
    def interest_time(cls):
        for account in cls.account:
            account.balance *= cls.interest_rate

    def __init__(self, balance=0):
        self.balance = balance

    def __repr__(self):
        return "BankAccount: {}".format(self.balance)

    def deposit(self, number):
        self.balance += number

    def withdraw(self, number):
        self.balance -= number

my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
