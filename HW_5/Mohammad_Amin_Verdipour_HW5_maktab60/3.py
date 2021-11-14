def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as ie:
        print(ie)
        
    

lst = [1, 2, 3, 4, 5]
print_list_element(lst, 8)