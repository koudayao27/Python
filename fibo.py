n = int(input())
i = 0

a = 0;
b = 1;
while i <= n:
  if i == 0:
    print(a)
  elif i == 1:
    print(b)
  else:
    c = a + b
    a = b
    b = c
    print(c)
  i += 1
