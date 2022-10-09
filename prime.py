import math 

result = "Prime"
n = int(input())
a = int(math.sqrt(n))
b = 2
if n <= 1:
  print("Not Prime")
else:
  while b <= a:
    if n % b == 0:
      result = "Not Prime"
      break
    b += 1
  print(result)
