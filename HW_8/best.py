from datetime import datetime, timedelta


class BankAccount:
    min_balance = 10000

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        # a dictionary, key: datetime of transaction and value: kind and amount of transaction
        self.history = {}
        self.transfer_flag = False  # This flag prevent double log history for 'transfer'
        # without it both 'transfer' and 'withrow' saved in history of source account

    def overdraw(self, amount):
        if self.balance - amount < BankAccount.min_balance:
            return False
        else:
            return True

    def withdraw(self, amount):
        if self.overdraw(amount):
            self.balance -= amount
            if not self.transfer_flag:
                self.history[datetime.now()] = f'Withdraw {amount}'
            else:
                self.transfer_flag = False
            print(
                f'The Withdraw was successful, {self.name}\'s balance: {self.balance}')
            return amount   # pass amount to 'transfer' method for withdraw from source and deposit that to destination account
        else:
            print('The amount entered is more than your print (two_min_after)balance')
            return 0

    def deposit(self, amount):
        if amount != 0:
            self.balance += amount
            self.history[datetime.now()] = f'Deposit {amount}'
            print(
                f'The Deposit was successful, {self.name}\'s balance: {self.balance}')

    def transfer(self, account, amount):
        if isinstance(account, BankAccount):
            if self.overdraw(amount):
                # if this flag was True, log of transfer will saved in history else withrow log will saved
                self.transfer_flag = True
                self.history[datetime.now()] = f'Transfer {amount} to {account.name}'
            cash = self.withdraw(amount)  # passed amount from 'withrow' method
            account.deposit(cash)
        else:
            print('Invalid bank account.')

    def print_history(self, time):
        duration = timedelta(minutes=2)
        print(f'\n{self.name}\'s Transaction history:')
        print(50 * '=')
        for item in self.history:
            if time - duration <= item <= time + duration:  # check entered time is in range of two minutes or not
                print(
                    f'{datetime.strftime(item,"%Y-%m-%d %H:%M:%S")}: {self.history[item]}')
                print(50 * '-')

    def __str__(self):
        return f'Bank account - Name: {self.name}, Balance: {self.balance}'

    def __repr__(self):
        return self.__str__()


ali = BankAccount('ali', 50000)
john = BankAccount('john', 80000)

duration = timedelta(minutes=1)
now = datetime.now()
two_min_after = now + 2*duration
two_min_before = now - 2*duration
four_min_after = now + 4*duration

ali.deposit(20000)
ali.withdraw(10000)
ali.withdraw(20000)
john.withdraw(50000)
ali.withdraw(80000)
ali.transfer(john, 10000)
john.transfer(ali, 85000)
john.transfer(ali, 5000)

ali.print_history(two_min_after)
john.print_history(two_min_after)

ali.print_history(four_min_after)
john.print_history(four_min_after)
