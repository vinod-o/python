import re 

txt = " i am vinod kumar reddy "
pattern = r"kumar"
search = re.search(pattern, txt)
if search:
    print("pattern found:", search.group())
else:
    print("not found")


