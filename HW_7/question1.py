class Account:
    
    minimum = 10000
    
    def __init__(self, name, remaining):
        self.name = name
        self.remaining = remaining
    
    def deposite(self, x):
        self.remaining += x
        print(f'The amount {x} has been credited to your account and your account balance is : {self.remaining}')
        return self.remaining 
    
    def permit(self, other):
        amount = int(input('Enter the amount : '))
        task = input('Enter the number 1 to withdraw from the account and the number 2 to transfer to another card and the number 0 to cancel? ')
        if task == '1':
            if self.remaining - amount >= Account.minimum: 
                self.remaining -= amount
                print(f'The amount {amount} was withdrawn from your account and your account balance is : {self.remaining}')
                return self.remaining
            else:
                print('The desired amount to withdraw from the account is more than the card balance!')
        elif task == '2':
            if self.remaining - amount >= Account.minimum:
                self.remaining -= amount
                other.remaining += amount
                print(f'The amount {amount} was withdrawn from your account for the transfer and your account balance is : {self.remaining}')
                return other.remaining
                return self.remaining 
            else:
                print('The desired amount to withdraw from the account is to transfer more than the card balance!')
        elif task == '0':
            print('You have been removed from the withdrawal or transfer operation!')
            
    def __str__(self):
        return (f'Name of account holder : {self.name}, account balance : {self.remaining}')            

            
  