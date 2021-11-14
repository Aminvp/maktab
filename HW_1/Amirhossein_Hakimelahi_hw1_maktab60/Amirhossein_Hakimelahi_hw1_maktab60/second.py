from random import randint

lst = ['H', 'T']
flipsNums = list()
for i in range(10):
    counter = 1
    pre = -1
    flipsNum = 0
    while counter < 3:
        randNumber = randint(1, 1000) % 2
        print(lst[randNumber], end=' ')
        if randNumber == pre:
            counter += 1
        else:
            counter = 1
        pre = randNumber
        flipsNum += 1
    flipsNums.append(flipsNum)
    print(f'({flipsNum} flips)')
av = sum(flipsNums) / len(flipsNums)
print('On average, %.1f flips were needed.' % av)
