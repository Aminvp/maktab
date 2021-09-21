import re

def Validation_phone_number(txt): #تابعی که یک شماره تلفن به صورت رشته دریافت میکند و آنرا به فرمت .......09 تبدیل میکند
    m = re.sub('^(\+098|\+98|\+0098|0|98|098|0098)?', '0', txt)
    if '9' in m: 
        print(m) 
    else:
        print('invalid phone number')
    
            
Validation_phone_number("+989125896598")
Validation_phone_number("+00989106598325")
Validation_phone_number("09355698563")
Validation_phone_number("+981121111111")
Validation_phone_number("+0989392563984")
Validation_phone_number("+0989192045896")

# m = re.sub('\+098|\+98|\+0098|0', '0', "+0989192045896")
# print(m)

