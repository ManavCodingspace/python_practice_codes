myint = 78
print(myint)
#floating no
myfloat1 = 789.23
myfloat2 = 554.54
print(myfloat1 + myfloat2)
# making string
name = "manav gaur"
myschool = "JMPS"
myage = 18
print(name)
print(myschool)
print(myage)
# making lists
list =("arjun", "rohan", "kapil")
print(list)
# python automaticaly converts 
# a into string
a = 7
print(type(a))
  
# python automaticaly converts 
# b into float
b = 3.0
print(type(b))

# python converts 
# d to float  as it is a float multilication
d = a * b
print(d)
print(type(d))

#python converts 
# c to float as a float addition
c = a + b
print(c)
print(type(c))

# creating an empty tuple
tuple = ()
print("intial empty tuple: ")
print(tuple)

#creating  a tuple with use of string
tuple1 = ('greeks', 'for')
print("/ntuple with the use of string: ")
print(tuple1)
 
# creating a tuple with 
# the use of  list
list1 = [1, 2, 3, 4, 5]
print("/n/tuple using list: ")
print(list1) 
 
import keyword

# printing all keywords at once using"kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

# true, false, none
print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None ==  [])
# if, else, elif

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

# STRINGS IN PYTHON
name = "manav"
surname = "gaur"
apple = '''He said,  
hi manav
"I want to eat an apple"'''

print(name)
print("HELLO", name)

print(apple)
 
# indexing
name = 'manav_gaur'

print(name[0])
print(name[2])
print(name[1])
print(name[3])

#looping through a string

print("Lets use a for loop/n")
for character in name:
     print(character)

print("Lets play a game")     
for character in apple:
     print(character)

# STRING SLICING 
nm = "HARRY" 
print(nm[-4:-2])

names = "manav, abhishek, aayush"
print(len(names))
print(names[:20])

# strings methods
# strings are immutable

name = "!!!! !Manav! !!!!!!! Manav"
print(name.upper())
print(name.lower())
print(name.rstrip("!"))
print(name.replace("Manav", "rohan"))
print(name.split(" "))

blog = "hello to my manav world"
print(blog.capitalize())

blog2  = "hello to my manav w0rld"
print(blog.capitalize())

str1= "WELCOME TO THE CONSOLE!!!"
print(str1.center(50))
print(str1.center(50, "."))

str2 = "Abracadabra"
countstr = str2.count("a")
print(countstr)
countstr = str1. count("O")

#ENDSWITH
print(str1.endswith("!!!"))
print(str2.endswith("ab"))

# FIND AND INDEX
av = "he's name is Dan. he is an honest man"
print(av.capitalize())
print(av.find("Dan"))

av2 = "he's name is Dan. he is an honest man"
print(av2.find("manav"))
print(av2.index("Dan"))

#ISALNUM
name = "WelcomeToTheConsloe"
print(name.isalnum())

name = "WelcomeToTheConsloe!!!!"
print(name.isalnum())

# ISALPHA 
name = "Welcome"
print(name.isalpha())

# ISLOWER()
name = "hello world"
print(name.islower())

name = "Hello world"
print(name.islower())

#ISPRITNABLE
name = "We wish you a Merry Christmas"
print(name.isprintable())

name = "We wish you a Merry Christmas"
print(name.isprintable())

# ISSPACE

name = "       "     #USING SPACEBAR
print(name.isspace())
name2 = "           "    # USING TAB
print(name2.isspace())

#SWAPCASE

name = "pYTHON IS A INTERPRETED LANGUAGE"
print(name.swapcase())

#TITLE
name = "pYTHON IS A INTERPRETED LANGUAGE"
print(name.title())

#IF- ELSE STATEMENT

a = int(input("Enter your age: "))
if(a>=18):
     print("You can give Vote")

else:
     print("You cannot give the vote")

#ELIF 

n = int(input("Enter your daily expenses: "))
if(n>=1000):
     print("You have too much money")

elif(n==500):
     print("Your are in the middle")

else:
     print("You are poor")

# NESTED IF
n1 = int(input("Your yearly expenses: "))
if(n1>=100000):
     print("you lie in the rich class")
elif(n1<100000):
     if(n1>=50000):
          print("you lie in the upper middle class")
     elif(10000<n1<50000):
          print("you lie in the middle class")
else:
     print("you are poor")

 # FOR LOOP

for k in range(1, 2000):
     print(k) 
 
