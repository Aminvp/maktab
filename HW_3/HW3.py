import random

class Player:
    target = 500 
    
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.fault = (self.height - self.weight) * (random.uniform(0.5, 2))

l=[]
for i in range(5):
    l.append(Player(int(input('height:')), int(input('weight:'))))

fault = []
for item in l:
    fault.append(item.fault)

print('average fault :',sum(fault)/5)
fault.sort()
fault.reverse()
for item in fault:
    print(item, end=' ')