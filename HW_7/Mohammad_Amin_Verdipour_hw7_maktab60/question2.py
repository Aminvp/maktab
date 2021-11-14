import question1

A = question1.Account('amin', 25000)
B = question1.Account('hamid', 35000)
print('User page amin :') 
A.deposite(5000)
A.permit(B)
print('_'*60)
print('User page hamid :')
B.deposite(2000)
B.permit(A) 
print('#'*60)
print(A)
print(B)
print('#'*60) 
print(A.__dict__)
print(B.__dict__)

