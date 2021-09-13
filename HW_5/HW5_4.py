def add_to_list_in_dict(thedict, listname, element):
    if thedict[listname]:
        l = thedict[listname]
        print('%s already has %d elements.' %(listname, len(l)))
    else:
        thedict[listname] = []
        print('Created %s.' %listname)
    
    thedict[listname].append(element)
    
    print('Aded %s to %s.' %(element, listname))


dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
lst = []




