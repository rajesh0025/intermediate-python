#random_examples
import random 
a=random.uniform(1,10)#it will generate float random value
b=random.randint(1,10)#it will generate inter value it inclue both 1 and 10
c=random.randrange(1,10)#it wont inclue include 1 and 10 
d=random.normalvariate(0,1)#(mean value,standard deviation)
print(a)
print(b)
print(c)
print(d)

import random

mylist=list("ABCDEFGH")

a=random.choice(mylist)
b=random.sample(mylist,3)#here set of any 3 nums of list here no multiple nums occurs.
c=random.choices(mylist,k=3)#same as of sample but multiple times ocurs a single value.
d=random.shuffle(mylist)
print(a)
print(b)
print(c)
print(d)

#used to save that random value after running.
import random
random.seed(1)#we need to give a num like index so that we may call it later.
a=random.uniform(1,10)#it will generate float random value.
print(a)
random.seed(1)#we need to give a num like index so that we may call it later.
a=random.uniform(1,10)#it will generate float random value.
print(a)

random.seed(2)
a=random.uniform(1,10)# it will generate float random value.
print(a)
random.seed(2)
a=random.uniform(1,10)#it will generate float random value.
print(a)
