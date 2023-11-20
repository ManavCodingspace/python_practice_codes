myint = 78
print(myint)
# **floating no**
myfloat1 = 789.23
myfloat2 = 554.54
print(myfloat1 + myfloat2)
# **making string**
name = "manav gaur"
myschool = "JMPS"
myage = 18
print(name)
print(myschool)
print(myage)
# **making lists**
list =("arjun", "rohan", "kapil")
print(list)
# **python automaticaly converts** 
# **a into string**
a = 7
print(type(a))
  
# **python automaticaly converts** 
# **b into float**
b = 3.0
print(type(b))

# **python converts** 
#**d to float  as it is a float multilication**
d = a * b
print(d)
print(type(d))

# **python converts** 
# **c to float as a float addition**
c = a + b
print(c)
print(type(c))

# **creating an empty tuple**
tuple = ()
print("intial empty tuple: ")
print(tuple)

# **creating  a tuple with use of string**
tuple1 = ('greeks', 'for')
print("/ntuple with the use of string: ")
print(tuple1)
 
# **creating a tuple with**
# **the use of  list**
list1 = [1, 2, 3, 4, 5]
print("/n/tuple using list: ")
print(list1) 
 
import keyword

# **printing all keywords at once using"kwlist()"**
print("The list of keywords is : ")
print(keyword.kwlist)

# **true, false, none**
print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None ==  [])
# **if, else, elif**

i = 20
if (i == 10):
     print("i is 10")

if (i ==20):
     print("i is 20")
    
else: 
     print("i is not present") 
# def function
def fun():
    print("Inside Function")

fun()         
number = input("Enter a Number ")
x = int(number)%2
if x == 0:
    print("The number is even")
else:
    print("The number is odd")   
