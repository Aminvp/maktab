import pickle
from datetime import datetime 
import time



class Bank :
    minimal_money = 10000
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.detail = {}
        self.detail['name'] = self.name
        self.detail['money'] = self.money
        global lst  
        lst.append(self.detail) 
        with open('data.pickle', 'wb') as writer :
            pickle.dump(lst, writer)
        globals()['lst_'+self.name] = []

    
    def add(self, add):
        with open('data.pickle', 'rb') as reader :
            lst = pickle.load(reader)
            for person_goal in lst :
                if person_goal['name'] == self.name :
                    self.money += add
                    print(f'cash of {self.name} : {self.money}')
                    person_goal['money'] = self.money
        with open('data.pickle', 'wb') as writer :
            pickle.dump(lst, writer)
        transaction = {}
        t = datetime.now()
        transaction[t.strftime('%Y/%m/%d - %H:%M:%S')] = f'deposit:{add} - cash:{self.money}'
        globals()['lst_'+self.name].append(transaction)

    
    def sub(self, sub) :
        with open('data.pickle', 'rb') as reader :
            lst = pickle.load(reader)
            for person_origin in lst :
                if person_origin['name'] == self.name :
                    self.money -= sub
                    print(f'cash of {self.name} : {self.money}')
                    person_origin['money'] = self.money
        with open('data.pickle', 'wb') as writer :
            pickle.dump(lst, writer)
        transaction = {}
        t = datetime.now()
        transaction[t.strftime('%Y/%m/%d - %H:%M:%S')] = f'withdraw:{sub} - cash:{self.money}'
        globals()['lst_'+self.name].append(transaction)


    def __check(self, request) :
        with open('data.pickle', 'rb') as reader :
            for person_origin in pickle.load(reader) :
                if person_origin['name'] == self.name :
                    if person_origin['money']-request >= Bank.minimal_money :
                        print('Your transaction was successful !!!')
                        return True
                    else :
                        print('Your inventory is not enough !!!')
                        return False


    def send_money(self, person1, request, person2) :
        if person1._Bank__check(request) == True :
            person1.sub(request)
            person2.add(request)
        else :
            transaction = {}
            t = datetime.now()
            transaction[t.strftime('%Y/%m/%d - %H:%M:%S')] = f'the transaction failed - cash:{self.money}'
            globals()['lst_'+self.name].append(transaction)


    def sub_money(self, person1, request) :
        if person1._Bank__check(request) == True :
            person1.sub(request)
        else :
            transaction = {}
            t = datetime.now()
            transaction[t.strftime('%Y/%m/%d - %H:%M:%S')] = f'the transaction failed - cash:{self.money}'
            globals()['lst_'+self.name].append(transaction)


    def add_money(self, person1, request) :
        person1.add(request)


    def transaction(self) :
        for t in globals()['lst_'+self.name] :
            print(t)



    def tow_min(self, user_time) :
        user_time = time.mktime(user_time)  
        start_time = user_time - 120
        start_time = datetime.fromtimestamp(start_time)
        stop_time = user_time + 120
        stop_time = datetime.fromtimestamp(stop_time)
        for dic in globals()['lst_'+self.name] :
            for key in dic.keys() :
                t = datetime.strptime(key, '%Y/%m/%d - %H:%M:%S')
                if t >= start_time and t <= stop_time :
                    print(dic)
                    
                    
lst = []
person1 = Bank('ali', 50000)
person2 = Bank('reza', 10000)
person3 = Bank('ahmad', 20000)
person4 = Bank('hasan', 300000)
person5 = Bank('mohammad', 75000)
person6 = Bank('iman', 130000)
person7 = Bank('mahan', 900000) 

print(person7.send_money(person7, 8710000, person1))  

print(person4.sub_money(person4, 285000))

print(person4.add_money(person4, 15000))    

person4.transaction()         

person4.tow_min((2021, 9, 21, 6, 38, 0, 0, 0, -1))    