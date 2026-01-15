age = 21 
height = 5.9
name ="Sarthak"
is_student = True


if age>18:  
    print("Adult")
elif age == 18:
        print("Just became an adult!")
else:
      print("Minor")

for i in range(5):
        print(f"Number:{i}")

count = 0
while count <3:
        print ("Counting :", count)
        count +=1

def greet(name):
       return f"hello,{name}!"

print (greet(name))