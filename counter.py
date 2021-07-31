#collection : counter,namedtuple,orderedDict,defaultdict,deque
from collections import Counter
a ="aaaaaaaaaaaaabbbbbbbbbcccdddddd"
my_counter=Counter(a)#counting  each
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2))#first2  
print(list(my_counter.elements()))
