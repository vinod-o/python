import re 
txt = " hello i am brown bread"

pattern = r"brown"

new = "red"
sub= re.sub(pattern,new,txt)
print("new txt:",sub)