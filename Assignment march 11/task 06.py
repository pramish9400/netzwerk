###                 TASK 6
###Add and remove the elements from a tuple.
# tuples are immutable, so you can not add elements
#one way is to convert the tuple into a list, do the required operations
#and then change the list back into the tuple

#sample code to demonstrate add & remove the elements from the tuple

tupley = "a", "b", "c"
print ("The tuple is: ", tupley)
listy = list(tupley)
listy.append("d")
tupley = listy
print (tupley)
print ("element d is added to the tuple")
print ("The tuple is: ", tupley)
listy = list(tupley)
listy.remove("d")
tupley = listy
print (tupley)
print ("element d is removed from the tuple")
