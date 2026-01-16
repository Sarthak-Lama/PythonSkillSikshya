def testFunction (arg):
    print("Id inside the function", id(arg))
    arg = arg+1
    print("New object after increment", arg,id(arg) )

var = 10
print("Id beofre passing ", id(var))
testFunction(var)
print("Value after function call",var)