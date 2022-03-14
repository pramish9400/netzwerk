###                 TASK 4
#add sublist [7,8] after 6
#input = l2 = [1,2,[3,4,5,6],9]
#output = [1,2,[3,4,5,6,[7,8]],9]


l2 = [1,2,[3,4,5,6],9]
l3= [7,8]
l2[2].append(l3)
print (l2)
