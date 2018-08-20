sum = 0
num=input()
temp1 = num
while temp1 > 0:
   digit = temp1 % 10
   sum += digit ** 3
   temp1 //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
