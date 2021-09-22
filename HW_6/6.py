from operator import itemgetter 

lst = [(19542209, "New York"), (4887871, "Alabama"), (5462579, "Tokyo"), (8563259, "Tehran"), (45756325, "Seol"), (58693218, "Pekan")]

print(lst[::-1])


print(sorted((lst), key = [itemgetter(1)][-1]))








