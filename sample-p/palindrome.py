n =121
rev = 0
while n>0:
    dig = n%10
    rev = rev*10+dig
    n = n//10
if rev == 121:
  print("palindrome number")
else:
  print("not palindrome num,ber")