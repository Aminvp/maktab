from random import randint

def chek(str) :
  if "'H', 'H', 'H'" in str or "'T', 'T', 'T'" in str :
    return True
  else :
    return False

sum = 0
i = 0
while i < 10 :
  i += 1
  lst = []
  c = chek(lst)
  while c == False :
    a = randint(1,2)
    if a%2 == 0 :
      lst.append("H")
    else :
      lst.append("T")
    s = str(lst)
    s = s[1:len(s)-1]
    c = chek(s)
  print(s,f"({len(lst)} flips)")
  sum += len(lst)
print(f"On average, {sum/10} flips were needed.")