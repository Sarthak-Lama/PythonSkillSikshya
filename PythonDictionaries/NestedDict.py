nested_dict={}

outer_keys = ["outer_key1","outer_key2"]
for key in outer_keys:
    nested_dict[key]={"inner_key1":"value1","inner_key2":"value2"}
    
print(nested_dict)