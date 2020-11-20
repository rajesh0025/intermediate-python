#strings orederd immutable text representation
# we can use sclicese in strings
my_string ="hello world"
sub=my_string[5:2:-1] #[start::end::gap b/w each char]
print(sub)

my_string ="hello world"
print(my_string.startswith("hello"))
print(my_string.startswith("world"))
print(my_string.endswith("world"))
print(my_string.find("l"))#index
print(my_string.count("l"))#count
print(my_string.replace("world","universe"))
print(my_string)


my_string='how are you doing'
print(my_string)#gives string
my_list=my_string.split(" ")#where to split here space is to split 
print(my_list)#gives list
join='   '.join(my_list) #to join listn with given space like split
print(join) #gives string
print("rajesh")
join='   '.join(my_list) #to join listn with given space like split
print(join)


nums="""1 
2
3
4
5 """
numms=nums.split("""
""")
print(numms)
join=" ".join(numms)
print(join)


my_string='how are you doing and where are you and whats up'
my_list=my_string.split("and")#here and is the point to split
print(my_list)
for ti in my_list:
    print(ti)


  
my_list= ['a'] *10
print(my_list)

  #to print like a string (aaaaaaaaaa)(BAD METHOD)
my_string=''
for i in my_list:
    my_string+=i
print(my_string)  

#GOOD METHOD TO PRINT LIKE A STRING
my_string=''.join(my_list)
print(my_string)

#to know the time taken by each method
from timeit import default_timer as timer 
#we can calculate time in this way 
staet=timer()
my_list= ['a'] *1000000
print(my_list)
stop=timer()
print(stop-staet)

#to print like a string (aaaaaaaaaa)(BAD METHOD)
start=timer()
my_string=''
for i in my_list:
    my_string+=i
stop=timer()
print(stop-start)

#GOOD METHOD TO PRINT LIKE A STRING
start=timer()
my_string=''.join(my_list)
stop=timer()
print(stop -start)

#% in string
var="rajesh"
bar=10.12345
my_string='%s is the student'%var
my_bring='%.3s is the student'%var
my_list="the percetage is  %f"%bar
my_fist="the percetage is  %.3f"%bar
print(my_string)
print(my_bring)
print(my_list)
print(my_fist)

