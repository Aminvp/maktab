from operator import itemgetter 

lst = [(19542209, "New York"), (4887871, "Alambaz"), (5462579, "Tokyo"), (8563259, "Tehran"), (45756325, "Aeola"), (58693218, "Pekan")]

lst_2 = list(map(lambda x : lst[len(lst)::-1], lst))[0]

print(sorted((lst_2), key = [itemgetter(1)][-1]))








