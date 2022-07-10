#tuple is one of the 4 inbuilt data type, other 3 are set, list, dictionary

#tuple is denoted by parathesis/small brackets "()"

#tuple items are ordered and unchangeable.

#tuple is used to store multiple items in a single variable

my_tuple = ("Banana", "Apple", "Grapes", "Orange")
print(my_tuple)

for x in my_tuple:
    print("\n",x)

# my_tuple.append("Watermelon")                      #This code will throw AttributeError
                                                     # my_tuple.append("Watermelon")
                                                     # AttributeError: 'tuple' object has no attribute 'append'


print("\n\t\tMethods of Tuples\n")
#---------------------METHODS OF TUPLES---------------------

#-----------------------------------------------------------

#Tuples consist of only 2 methods.

#count --> returns the number of times the specified value occurred in the tuple.

print("\n\t\tCount Method\n")
tup_count = (2,4,4,5,6,4,7,8,9)
print("The number of times 4 is repeated in the tuple is: ", tup_count.count(4))

#index --> returns the first occuring index number of the specified element of the tuple.

print("\n\t\tIndex Method\n")
tup_index = (2,3,4,5,5,6,7)
print("The 5 firstly occured at index position: ",tup_index.index(5))