#q2
#task 1
def find_and_replace(lst, find_val, replace_val):
 if isinstance(lst,list):
  for i in range(len(lst)):
   if find_val == lst[i]:
    lst[i]=replace_val
  print(lst)
 else:
  return None
#task 2
find_and_replace([1,2,3,4,2,2],2,5)
find_and_replace(["apple","banana","apple"],"apple","orange")
