###                     TASK 3
#Add item 70 after 60 in the following Python List
#input :l1 = [10, 20, [30, 40, [50, 60], 80], 90, 100]

#output =[10, 20, [30, 40, [50, 60, 70], 80], 90, 100]


l1 = [10, 20, [30, 40, [50, 60], 80], 90, 100]
l1[2][2].insert(2, 70)
print (l1)
