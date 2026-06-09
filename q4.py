#q4
#task 1
def string_reverse(s):
 if isinstance(s,str):
 #[start:end:step]
  new_str=s[::-1]
  return(new_str)
 else:
  return None
#task 2
print(string_reverse("Hello World"))
print(string_reverse("Python"))
