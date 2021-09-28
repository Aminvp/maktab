from datetime import date

#A one-time ticket card 
class single_table_card:

    #We considered the cost of each trip as one unit
    def __init__(self, credit=1):
        self.credit = credit
        self.number = 1
    
    #Method for using the card
    def use(self):
        if self.number > 0:
            self.number -= 1
            print('You can log in.')
            return self.number
        else:
            print('You are not allowed to log in!')
    
    def __str__(self):
        return 'This card was created for a trip can no longer be used please throw it away!'
            
     
#Credit card for multiple use
class credit_card(single_table_card):
    
    #We considered the cost of each trip as one unit
    def __init__(self, credit:int):
        super().__init__(credit)
        self.number = credit//1 
    
    #Method for charging credit card    
    def charge(self, amount:int):
        self.credit += amount
        self.number += amount//1
        return self.credit, self.number
    
    def __str__(self):
        return f'This card can be used for {self.number} another trip!'

    
#Long-term credit card for multiple use
class credit_card_time(single_table_card):
    
    #We considered the cost of each trip as one unit
    def __init__(self, credit:int, date):
        super().__init__(credit) 
        self.number = credit//1
        self.date = date
        
    #Method for charging credit card and updating card time    
    def charge(self, amount:int, update):
        self.credit += amount
        self.number += amount//1
        self.date = update
        return self.credit, self.number, self.date 
    
    #Method for using credit card
    def use(self, usedate):
        if self.number > 0 and usedate < self.date:
            self.number -= 1
            print('You can log in.')
            return self.number
        else:
            print('you are not allowed to log in!')
            
    def __str__(self):
        return f'This card can be used for {self.number} another trip and its validity is {self.date} up to date!'

print('For single table card:')
ob = single_table_card()
ob.use()
print(ob) 

print('#'*20)
print('For credit card:')
ob1 = credit_card(5)
ob1.use()            
ob1.charge(5)
ob1.use()
print(ob1)        
        
print('#'*20)
print('For credit card time:') 
ob2 = credit_card_time(3, date(2021, 9, 5))
ob2.use(date(2021, 9, 2)) 
ob2.charge(5, date(2021, 10, 5))
ob2.use(date(2021, 9, 20))
print(ob2)
    
    