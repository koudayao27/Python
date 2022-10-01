days = int(input())
txt = input()
lst = txt.split()

sum = 0

i = 0
while i < days:
  sum += int(lst[i])
  i += 1

print(sum)
