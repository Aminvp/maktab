import csv

with open('grades.csv', 'r') as dr:
    csv_reader = csv.reader(dr)
    lst_r = []
    for x in csv_reader:
        lst_r.append([x[0]]+[x[2]]+[x[1]])
    
with open('grades_2.csv', 'r+', newline='') as dw:
    csv_writer = csv.writer(dw)
    lst_w = []
    lst_ww = []
    csv_writer.writerows(lst_r)
    for x in lst_r:
        lst_w.append(sum(map(int, x[:1]+x[1:2]+x[2:3])))
    for x in lst_w:
        lst_ww.append(str(x))
    csv_writer.writerows(lst_ww)
        
        
    

    
    
    

    



