info = {}
print(type(info))  #return dict class

info ={"Maitri" , 19 , "Single", "51.6kg", 19 }
for item in info:
    print(item) #set also not allow duplicate values

#set methods
items1 = {"Maitri","Hasti","Riyen","Dipali"}
items2 = {"Maitri","Harshil","Hasti","Deep"}

#union
all_items = items1.union(items2)
print(all_items)
#update
items1.update(items2)
print(items1)
print("\n")

#intersection
common_items = items1.intersection(items2)
print(common_items)  
#intersection update
items1.intersection_update(items2)
print(items1)  
print("\n")

#difference
diff_items = items1.difference(items2)
print(diff_items)  #no common items
#difference update
items2.difference_update(items1)
print(items1)  #no common items
print("\n")

#symmetric difference
sym_diff_items = items1.symmetric_difference(items2)
print(sym_diff_items)  #all items since no common items
#symmetric difference update
items1.symmetric_difference_update(items2)
print(items1)  #all items since no common items
print("\n")


setA={"Maitri","Hasti"}
setB={"Harshil","Riyen"}
#isdisjoint
print(setA.isdisjoint(setB))

#issubset and issuperset
print(setA.issubset(items1))
print(items1.issuperset(setA))

#add
setA.add("Dipali")
print(setA)

#remove and discard
setA.remove("Hasti")    
print(setA)
setA.discard("XYZ")  #no error if item not found
print(setA)

#pop
removed_item = setA.pop()
print("Removed item:", removed_item)
print(setA)

#clear
setA.clear()
print(setA)

