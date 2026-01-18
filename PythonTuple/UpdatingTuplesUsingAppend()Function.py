
T1 = (10, 20, 30, 40)
list_T1 = list(T1)
new_elements = [50, 60, 70]
for element in new_elements:
    list_T1.append(element)
updated_tuple = tuple(list_T1)
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)