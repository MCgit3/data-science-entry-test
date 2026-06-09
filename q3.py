#q3
#task 1
def update_dictionary(dct, key, value):
 if key in dct:
  print("Original value = ", dct[key])
  dct[key]=value
 else:
  dct[key]=value
 return(dct)
#task 2
print(update_dictionary({},"name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))