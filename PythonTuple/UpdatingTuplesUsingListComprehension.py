
T1 = (10, 20, 30, 40)

list_T1 = list(T1) #Using Type casting
updated_list = [item + 100 for item in list_T1]
updated_tuple = tuple(updated_list)

print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)