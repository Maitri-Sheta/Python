#Lists are ordered collection of data items.
#They store multiple items in a single variable.
#ist items are separated by commas and enclosed within square brackets [].
#Lists are changeable meaning we can alter them after creation.
num = [4,2,5,3,6,1,2,1,2,8,9,7]
print("Original List:", num)
#positive indexing
print("Element at index 2:", num[2])  
#negative indexing
print("Element at index -1:", num[-1])  
print("\n")


#item in list?
print("Is 3 in list?", 3 in num)
print("Is 60 in list?", 60 in num)
print("\n")


#range of indexes
print("Elements from index 1 to 3:", num[1:4])
print("Elements from start to index 2:", num[:3])
print("Elements from index 2 to end:", num[2:])
print("Elements from start to end:", num[:])
print("\n")

#list comprehension
#syntax: lst2=[exp(item) for item in lst if condition]
name = ["alice","bob","charlie","david","eda","frande"]
lst2 = [item for item in name if "a" in item]
print("Names containing 'a':", lst2)

lst2 = [item for item in name if (len(item)>4)]
print("Names with more than 4 letters:", lst2)
print("\n")

#list methods
print("Original List:", num)
print("Original List:",name)
#sort()
num.sort()
print("Sorted num List:", num)
name.sort(reverse=True)
print("Reverse Sorted name List:", name)
#index()
print("Index of bob ",name.index("bob"))
#count()
print("Count of 2 in num List:", num.count(2))
#copy()
num_copy=num.copy()
print("Copy of num List:", num_copy)
#insert()
name.insert(2,"maitri")
print("List after inserting maitri at index 2:", name)
#extend()
name.extend(["deep","hasti","harshil"])
print("List after extending with more names:", name)
#remove()
name.remove("eda")  
print("List after removing 'eda':", name)
#pop()  
popped_item = name.pop()  
print("Popped item:", popped_item)
print("List after popping last item:", name)
