student_info={
    "name ": "Alice",
    "age":21,
    "Major":"Comp Science"

}
all_items = student_info.items()
print("Items:", all_items)
print("Iterating thorugh key_values pairs:")
for key , value in all_items:
    print (f"{key}:{value}")