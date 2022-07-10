#List is similar to an Array but they allow us to create
#  micellaneous collection of items inside a list.

list_proper = ["cake","pastery","popcorn","chocolates","ice cream"]
print("The list consist of: ",list_proper,"\n")

#You can store integer, float, boolean, list, set, string, dictionary inside a list.
list_ = [7,"Hello",True,{2.3,5.6},None,{"Dev":"Barot","College":"University"}]

print(list_)






print("\n\t\tMethods of List\n")
#---------------------METHODS OF LIST---------------------

#----------------------------------------------------------
#append --> Adds an element at end of the list
print("\n\t\tAppend Method\n")
list1 = [2,4,6,8]
list1.append(10)
print(list1)

#----------------------------------------------------------
#clear --> Removes all elements from the list
print("\n\t\tClear Method\n")
list1.clear()
print(list1)

#----------------------------------------------------------
#copy --> Returns a copy og the list
print("\n\t\tCopy Method\n")
a_list = ["Hello,","This","is","Dev."]
copy_list = a_list.copy()
print(copy_list)

#----------------------------------------------------------
#count --> Returns number of elements with the specified value.

print("\n\t\tCount Method\n")
count_list = ["Hey","You","That?","No","You","Did","That"]
print(count_list.count("You"))

#----------------------------------------------------------
#extend --> Adds the specified list elemts to the end of current list.

print("\n\t\tExtend Method\n")
pledge_list = ["India is", "My", "Country"]
extend_pledge = ["All Indians", "Are My", "Friends"]
conclude_list = ["Jai", "Hind"]
pledge_list.extend(extend_pledge)
print("This is extended list method: ",pledge_list)

#You will find th output different and this will clear your logic
#  in differing between extend and append.
pledge_list.append(conclude_list)
print("This is the appended list: ",pledge_list)

#----------------------------------------------------------
#index --> returns the first index of the specified element

print("\n\t\tIndex Method\n")
in_list = [1,5,6,7,3,8,5,3]                        #multiple elements of 3,5
print("The 5 occured for the first time at index: ", in_list.index(5))
print("The 3 occured for the first time at index: ", in_list.index(3))

#----------------------------------------------------------
#pop --> Removes the element from the list at specified position

print("\n\t\tPop Method\n")
in_list.pop(3)
print("The new in_list after popping element at index 3: ",in_list)

#----------------------------------------------------------
#remove --> Removes the item with specified value

print("\n\t\tRemove Method\n")
cars = ["Tata", "Toyota", "Tesla", "Maruti"]
cars.remove("Toyota")

#----------------------------------------------------------
#reverse --> It will reverse the order of elements inside the list.

print("\n\t\tReverse Method\n")
rev_list = ["Dev", "Is", "Name", "My"]
rev_list.reverse()
print("The reversed rev_list is here: ",rev_list)

#----------------------------------------------------------
#sort --> It will sort the list
print("\n\t\tSort Method\n")
rev_list.sort()
print("The rev_list got sorted by alphabetical order(A,B,C,D,...): ",rev_list)