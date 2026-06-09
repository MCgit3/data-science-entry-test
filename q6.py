#q6
#task 1
def find_first_negative(lst):
 i=0
 while i<len(lst):
  if lst[i] < 0:
   return lst[i]
  else:
   i+=1
   continue
 
 return "No negatives"
   
#task 2
print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))