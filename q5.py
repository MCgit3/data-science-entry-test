#q5
#task1
def check_divisibility(num, divisor):
 if isinstance(num, (int, float)) and isinstance(divisor, (int, float)):
  if(num%divisor)==0:
   return True
  else:
   return False
 else:
  return False
#task2
print(check_divisibility(10,2))
print(check_divisibility(7,3))
