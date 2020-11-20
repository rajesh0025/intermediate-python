#tuple ordered immutable allows duplicate elements 
mytuple =tuple(['max',29,29,"nan",10])
print(type(mytuple))

item = mytuple[1]# index
print(item)
#rep=mytuple.replace("max","raj")#it it gives u error coz tuples are immutable
#print(rep)
#ind=mytuple.find("max") no file attribute for tuples we need use index in place of find
#print(ind)
for i in mytuple:
    print(i)
if 29 in mytuple:
    print('29 is inside')

print(mytuple.count(29)) #count no of given items
print(mytuple.index(29)) # giving index value 
print(mytuple.index("max"))
print(mytuple[2])
#print(mytuple.add("duu"))
 
my_tuple=tuple(["rajesh","m s dhoni", "virat","jadeja"])
first , second ,third , fouth = my_tuple # unpacking tuples
print(first)
print(second)
print(third)
print(fouth)

my_tuple=("rajesh","m s dhoni", "virat","jadeja")
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

tupl=('rajsh',)
print((tupl))