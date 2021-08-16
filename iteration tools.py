for w in range(1,33):
   print(w,end=',,')

#here """product """ gives you all possible pairs.
from itertools import product
a = [1,2]
b = [3,4]
prod=product(a,b)
print(list(prod))
#we can repeat each set of values in single one.
from itertools import product
a = [1,2]
b = [3]
prod=product(a,b,repeat=2)
print(list(prod))

#""permutations""" is used to get all possible order of a list .
from itertools import permutations
a = [1,2,3]
perm=permutations(a)
print(list(perm))
#we can repeat this in limiting values.
from itertools import permutations
a = [1,2,3]
perm=permutations(a,2)
print(list(perm))

#""""combination """" different cobination argument value is mandetory.
from itertools import combinations,combinations_with_replacement
a=[1,2,3]
comb =combinations(a,2)
print(tuple(comb))
comb_wr=combinations_with_replacement(a,2)
print(list(comb_wr))

#""accumulate""" is used get the sum of 2 nums x y in a list
from itertools import accumulate
a=[1,2,3,4]
acc=accumulate(a)
print(a)
print(list(acc))

#operator with accumulate
from itertools import accumulate
import operator
a=[1,2,3,4]
acc=accumulate(a,func=operator.mul)#multiply operator #we can also use max for maximum of respective  value.
print(a)
print(list(acc))

#""groupby"""  groups the desired data
from itertools import groupby
persons=[{'name':'tim','age':12},{'name':'lisa','age':11},
{'name':'candice','age':12}]
#we can group desired set of data od dict
group=groupby(persons,key=lambda x:x['age'])
for key ,value in group:
    print(key,list(value))

#infinite loop::count cycle repeat
from itertools import count,cycle,repeat
for i in count(5):#initial value which is starts from 5
    print(i)
    if i==100:
        break
a=[1,2,3] 
#for i in cycle(a):
#    print(i)  #infinite loop

for i in repeat(2,10):#2 arguments (value,no of times to repeat)
    print(i)


