#list
list1 = [2, 4, 9, 1, 5]
print("Original list:", list1)
#add
list1.append(6)
print("List after adding an element:", list1)
#del
list1.remove(1)
print("List after removing an element:", list1)
#modify
list1[2] = 10
print("List after modifying an element:", list1)

#dictionary
dict1 = {'a': 5, 'b': 8, 'c': 10}
print("\nOriginal dictionary:", dict1)
#add
dict1['d'] = 4
print("Dictionary after adding an element:", dict1)
#delete
del dict1['b']
print("Dictionary after removing an element:", dict1)
#modify
dict1['c'] = 30
print("Dictionary after modifying an element:", dict1)

#set
set1 = {1, 6, 7, 9, 2}
print("\nOriginal set:", set1)
#add
set1.add(5)
print("Set after adding an element:", set1)
#delete
set1.remove(6)
print("Set after removing an element:", set1)
#modify
set1.discard(7)
set1.add(10)
print("Set after modifying an element:", set1)

