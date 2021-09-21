import re

def func(txt, word): #تابعی یک کلمه را دریافت میکند و وجود آنرا در آخر متن بررسی میکند
    m = re.search(word+'$', txt) 
    if m:
        print('The desired word was found.')
    else:
        print('The desired word was not found.')
        
txt = 'python is a programming language.' 
word = 'language.'

func(txt, word)
     
# def func(txt, word): #تابعی یک کلمه را دریافت میکند و وجود آنرا در آخر متن بررسی میکند
#     m = re.search(word+'\Z', txt)
#     if m:
#         print('The desired word was found.')
#     else:
#         print('The desired word was not found.')
        
# txt = 'python is a programming language.'
# word = 'language.'

# func(txt, word)