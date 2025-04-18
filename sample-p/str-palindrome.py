num = 121
str_num = str(num)
#print(num)
#print(type(str_num))
rev=' '
for char in str_num:
    rev= char+rev 
n= int(rev)
if n==num:
    print("palindrome")
else:
    print("not palindome")

