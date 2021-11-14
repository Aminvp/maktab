def is_ord_sub(smal, big):
    for i in range(len(smal)):
        for j in range(i, len(big)):
            if smal[i] == big[j]:
                flag = True
            else:
                flag = False
    return flag
smal = list(map(int, input().split()))
big = list(map(int, input().split()))

print(is_ord_sub(smal, big)) 
    
        