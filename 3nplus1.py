n = int(input())
result = ""

while n > 1:
  result += str(n) + " "
  if n % 2 == 0:
    n = int(n / 2)
  else:
    n = n * 3 + 1
result += "1"
print(result)
