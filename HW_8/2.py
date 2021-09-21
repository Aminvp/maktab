import datetime

def func(y, m, d):#تابعی که سال و ماه و روز را دریافت میکند وآنرا به فرمت سال و اسم ماه و اسم روز هفته تبدیل میکند
    try:
        today = datetime.datetime(y, m, d)
        print(today.strftime('%A-%B-%Y')) 
    except Exception as e:
        print(e)

func(2021, 4, 15)
func(2021, 8, 18) 
func(2021, 2, 28)

# def func(): #تابعی که سال و ماه و روز را دریافت میکند وآنرا به فرمت سال و اسم ماه و اسم روز هفته تبدیل میکند
#     y = int(input('enter year:'))
#     m = int(input('enter month:'))
#     d = int(input('enter day:'))
#     try:
#        today = datetime.datetime(y, m, d)
#        print(today.strftime('%A-%B-%Y')) 
#     except Exception as e:
#        print(e)
    
# func()
