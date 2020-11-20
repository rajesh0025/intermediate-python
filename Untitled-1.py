#tuple ordered immutable allows duplicate elements 
mytuple =tuple(['max',29,29,"nan",10])
print(mytuple)

item = mytuple[1]# index
print(item)

for i in mytuple:
    print(i)
if 29 in mytuple:
    print('29 is inside')

print(mytuple.count(29)) #count no of given items
print(mytuple.index(29)) # giving index value 
 
my_tuple=tuple(["rajesh","m s dhoni", "virat","jadeja"])
first , second ,third , fouth = my_tuple # unpacking tuples
print(first)
print(second)
print(third)
print(fouth)

my_tuple=tuple(["rajesh","m s dhoni", "virat","jadeja"])
first ,*middle,last=my_tuple
print(first)
print(last)
print(*middle)
