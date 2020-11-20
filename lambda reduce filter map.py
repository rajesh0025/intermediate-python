#lambda  argementsv: expression
add= lambda x: x+10
print(add(10))

mult = lambda x,y:x*y
print(mult(2,4))

points=[(1,2),(15,3),(5,-1),(10,4)]
sorted_points=sorted(points)

print(points)
print(sorted_points)#first value is sorted 

#we can use lambda to sort y point 

mult = lambda x,y:x*y
print(mult(2,4))

points=[(1,2),(15,3),(5,-1),(10,4)]
sorted_points=sorted(points ,key=lambda x:x[1])#index value
#we can also sort by addition of both
add_both=sorted(points,key=lambda x:x[0]+x[1])#index value

print(points)
print(sorted_points)
print(add_both)

#""groupby"""  groups the desired data
from itertools import groupby
persons=[{'name':'tim','age':12},{'name':'lisa','age':11},
{'name':'candice','age':12}]
#we can group desired set of data od dict
group=groupby(persons,key=lambda x:x['age'])
for key ,value in group:
    print(key,list(value))



#in maps or filter or reduce is same as lambda but the uses a list like iterations and conditionsinstead 
#map(func,seq) two arguements   the diff b/t filter and map is that filter is used in control statements and map is used for loops
a=[1,2,3,4,5]
b=map(lambda x:x*2,a)  
print(tuple(b))
#the diff b/t filter and map is that filter is used in control statements and map is used for loops
#its represents bool values not the ans that was getting by filter 
#filter condition(if stat) is used in maps
a=[1,2,3,4,5]
b=map(lambda x:x%2==0,a)  
print(tuple(b)) 


#for above we can also
c=[x*2 for x in a]
print(list(c))

#filter(func,seq) the diff b/t filter and map is that filter is used in control statements and map is used for loops
a=[1,2,3,4,5]
b=filter(lambda  x: x%2==0,a)
print(list(b))
#wont work
#map condition(loops) used in filter
a=[1,2,3,4,5]
b=filter(lambda  x: x*2,a)
print(list(b))

c=[x%2==0 for x in a ]
c2=[x for x in a if x%2==0]
print(list(c))
print(list(c2))

#if you wanna multiply both x n y 
# reduce(func,seq)
from functools import reduce
a=[1,2,3,4,5]
b=reduce(lambda x,y:x*y,a)
print(b)

