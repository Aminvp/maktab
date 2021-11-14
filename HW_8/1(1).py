from datetime import datetime

class Account:
    
    minimum = 10000
    
    def __init__(self, name, remaining):
        self.name = name
        self.remaining = remaining
        self.lst=list()
    
    def deposite(self, x, Y, M, D, h, m):
        self.remaining += x
        print(f'The amount {x} has been credited to your account and your account balance is : {self.remaining}')
        self.lst.append(f'deposit:{x}, remaining:{self.remaining}, date&time:{datetime(Y, M, D, h, m)}')
        return self.remaining  
    
    def permit(self, other, Y, M, D, h, m):
        amount = int(input('Enter the amount : ')) 
        task = input('Enter the number 1 to withdraw from the account and the number 2 to transfer to another card and the number 0 to cancel? ')
        if task == '1':
            if self.remaining - amount >= Account.minimum: 
                self.remaining -= amount
                print(f'The amount {amount} was withdrawn from your account and your account balance is : {self.remaining}')
                self.lst.append(f'withdrawn:{amount}, remaining:{self.remaining}, date&time:{datetime(Y, M, D, h, m)}')
                return self.remaining
            else:
                print('The desired amount to withdraw from the account is more than the card balance!')
        elif task == '2':
            if self.remaining - amount >= Account.minimum:
                self.remaining -= amount
                other.remaining += amount
                print(f'The amount {amount} was withdrawn from your account for the transfer and your account balance is : {self.remaining}')
                self.lst.append(f'transfer:{amount}, remaining:{self.remaining}, date&time:{datetime(Y, M, D, h, m)}')
                return other.remaining
                return self.remaining  
            else:
                print('The desired amount to withdraw from the account is to transfer more than the card balance!')
        elif task == '0':
            print('You have been removed from the withdrawal or transfer operation!')
            
    def __str__(self):
        return (f'Name of account holder : {self.name}, account balance : {self.remaining}, details:{self.lst}')            

A = Account('amin', 25000)
B = Account('hamid', 35000)
print('User page amin :') 
A.deposite(5000, 2021, 4, 8, 22, 8)
A.permit(B, 2021, 5, 2, 13, 38)
print('_'*60)
print('User page hamid :')
B.deposite(2000, 2021, 3, 2, 15, 29) 
B.permit(A, 2021, 8, 4, 10, 20) 
print('#'*60)
print(A)
print(B)
print('#'*60) 
print(A.__dict__)
print(B.__dict__)
            
  