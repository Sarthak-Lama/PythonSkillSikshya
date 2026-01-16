#Basic Data Types
age = 21            #int
height = 5.9        #float
name ="Sarthak"     #string
is_student = True   #bool

#control structures 

#conditionals
if age>18:  
    print("Adult")
elif age == 18:
        print("Just became an adult!")
else:
      print("Minor")


# For loop
for i in range(5):  #iterates from 0 to 4
        print(f"Number:{i}")


# While loop
count = 0
while count <3:
        print ("Counting :", count)
        count +=1

#Functions
def greet(name):
       return f"hello,{name}!"
#Function call
print (greet(name))