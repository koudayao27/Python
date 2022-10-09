txt = input()
lst = txt.split()
a = int(lst[0])
b = int(lst[1])
c = int(lst[2])
i = 1

while i <= a:
  if i % b == 0 and i % c == 0:
    print("FizzBuzz")
  elif i % b == 0:
    print("Fizz")
  elif i % c == 0:
    print("Buzz")
  else:
    print(i)
  i += 1
