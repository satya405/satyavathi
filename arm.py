n = int(input())
order = len(str(n))
sum = 0
temp = n
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
if n == sum:
   print("yes")
else:
   print("no")
