#Task1
def swap(x,y):
  if (isinstance(x,(int, float))) and      (isinstance(y, (int, float))):
   x,y = y,x
   print(x,y)
  else:
   return -1
   
#Task2
print(swap("Apple",10))
swap(9,17)
