tup = ()
print(type(tup),tup)
tup = (1)
print(type(tup),tup)
tup = (1,)
print(type(tup),tup)
tup = (1,2,3,"Maitri",4.5, True)
print(type(tup),tup)
#conditional check
if 4.5 in tup:
    print("4.5 is present in tuple")    
#tuple unpacking
a,b,c,d,e,f = tup
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#nested tuple
tup1 = (1,2,3)
tup2 = ("Maitri",4.5, True)
tup3 = (tup1, tup2)
print(tup3)

#tuple methods
tup = (1,2,3,4,2,5,2)
print(tup.count(2))
print(tup.index(5))
#immutable
#tup[0] = 10 #TypeError: 'tuple' object does not support item assignment
#slicing
print(tup[1:5])
print(tup[:4])
print(tup[3:])
print(tup[:])
#concatenation
tup4 = tup + (6,7,8)
print(tup4)
#repetition
tup5 = tup * 2
print(tup5)
#length
print(len(tup))
#iteration
for item in tup:
    print(item)
#nested tuple unpacking
(t1, t2) = tup3
print(t1)
print(t2)
(x1, x2, x3) = t1
print(x1)
print(x2)
print(x3)

(y1, y2, y3) = t2
print(y1)
print(y2)
print(y3)

#tuple with single element
single_element_tup = (42,)
print(type(single_element_tup), single_element_tup)
#empty tuple
empty_tup = ()
print(type(empty_tup), empty_tup)
#tuple with mixed data types
mixed_tup = (1, "Hello", 3.14, False)
print(type(mixed_tup), mixed_tup)
#tuple nesting
nested_tup = (1, (2, 3), (4, (5, 6)))
print(type(nested_tup), nested_tup)
#tuple slicing
slice_tup = mixed_tup[1:3]
print(type(slice_tup), slice_tup)
#tuple concatenation
concat_tup = single_element_tup + mixed_tup
print(type(concat_tup), concat_tup)
#tuple repetition
repeat_tup = single_element_tup * 3
print(type(repeat_tup), repeat_tup)
#tuple length
length = len(nested_tup)
print("Length of nested_tup:", length)
#iterating through a tuple
for element in mixed_tup:
    print("Element:", element)
#checking membership
if "Hello" in mixed_tup:
    print("'Hello' is in mixed_tup")
print("'World' is not in mixed_tup" if "World" not in mixed_tup else "'World' is in mixed_tup")
