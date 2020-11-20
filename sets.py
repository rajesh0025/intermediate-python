# sets unordered mutable no duplicates 
myset={"hello"}
print(myset)

myset=set("hello")
print(myset)

setnum =set()#empty set must rpresent like this 

setnum.add(1)
setnum.add(2)
setnum.add(3)

#we we use remove function then there would be an error coz 4 element was not in the set

setnum.discard(4)

# .clear() empties set
 
print(setnum)


setA ={1,2,3,4,5,6,7}
setB={1,2,3,8,9,10,11}
# union method to attach 2 sets
attach=setA.union(setB)
print(attach)


#intersection to know common items of set A
common=setA.intersection(setB)
print(common)

#difference of sets of setA
difference=setA.difference(setB)
print(difference)

#differnt iteems in both sets
difference=setA.symmetric_difference(setB)
print(difference)

#updating the original set 
setA ={1,2,3,4,5,6,7}
setB={1,2,3,8,9,10,11}

setA.difference_update(setB)
print(setA)
#
setA ={1,2,3,4,5,6,7}
setB={1,2,3,8,9,10,11}
#
setA.intersection_update(setB)
print(setA)

setA ={1,2,3,4,5,6,7}
setB={1,2,3}

print(setA.issubset(setB))

setA ={1,2,3,4,5,6,7}
setB={1,2,3}

print(setB.issubset(setA))


setA ={1,2,3,4,5,6,7}
setB={1,2,3}
print(setA.issuperset(setB))


setA ={1,2,3,4,5,6,7}
setB={1,2,3}
print(setB.issuperset(setA))

#bool false if there is any comon
setA ={1,2,3,4,5,6,7}
setB={1,2,3}
setC={9,10}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))