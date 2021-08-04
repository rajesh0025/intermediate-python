#its useful in generating items only one at a time when we ask 
# yield keyword instead of return.
def mygenerator():
    yield 1
    yield 2 
    yield 3

g=mygenerator()

#for i in g:#it prints all the items.
#    print(i)
#we can print one by one
value=next(g)#first value
print(value)

value=next(g)#if execute again then the next value print.
print(value)

value=next(g)
print(value)

# yield keyword instead of return.
def mygenerator():
    yield 1
    yield 2 
    yield 3

g=mygenerator()

print(sum(g))

# yield keyword instead of return.
def mygenerator():
    yield 1
    yield 2 
    yield 3

g=mygenerator()

x=sorted(g)
print(x)

#
def countdown(num):
    print('starting ')
    while num > 0:
        yield num
        num -= 1

cd=countdown(10) 

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
#normal vs generator.
#normal.
import sys
def firstn(n):
    nums =[]
    num=0
    while num<n:
        nums.append(num)
        num+=1
    return nums

#generator.
def firstn_generator(n):
    num=0
    while num<n:
        yield num
        num+=1

print(firstn(10))
print(firstn_generator(10))#here we need to use for loop to print all items


print(sum(firstn(10)))
print(sum(firstn_generator(10)))


print(sys.getsizeof(firstn(10)))
print(sys.getsizeof(firstn_generator(10)))

#febonacci series
#o,1,1,2,3,5,8,13
def fibonacci(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b

fib=fibonacci(30)
for i in fib:
    print(i)        

##
#generator vs list comprehendions
import sys
mygenerator=(i for i in range(10) if i%2==0)
for i in mygenerator:
    print(i)
print(sys.getsizeof(i))
#list comph
mylist=[i for i in range (10) if i%2==0]
print(mylist)
print(sys.getsizeof(mylist))
