def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)
  
txt = input()
lst = txt.split()
a = int(lst[0])
b = int(lst[1])

if a > b:
  result = gcd(a, b)
else:
  result = gcd(b, a)

print(result)
