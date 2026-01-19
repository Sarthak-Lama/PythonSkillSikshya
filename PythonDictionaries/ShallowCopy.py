orginal_dict = {"name":"Alice",
                "age":35,
                "skills":["Pyhton","Data Science"]
                }
shallow_copy = orginal_dict.copy()

shallow_copy["age"]=26
shallow_copy["skills"].append("Machine Learning")

print("Orginal dictionary:",orginal_dict)
print("Shallow copy:",shallow_copy)