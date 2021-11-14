def is_ord_sub(smlst, biglst):
    index = -1
    for item in smlst:
        try:
            index = biglst.index(item, index + 1)
        except:
            return False
    return True


lst1 = list(map(int, input('insert the bigger list : ').split()))
lst2 = list(map(int, input('insert the smaller list : ').split()))
print(is_ord_sub(smlst=lst2, biglst=lst1))
