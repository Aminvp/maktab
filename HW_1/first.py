def is_ord_sub(Large, Small):
    a = 0
    count = 0
    for i in Small:
        for j in range(a, len(Large)):
            if Large[j] == i:
                a = j
                count += 1
    if count == len(Small):
        return ("True")
    else:
        return ("False")

a = list(map(int, input("Enter Large list : ").split()))
b = list(map(int, input("Enter Small list : ").split())) 

print(is_ord_sub(a, b))         