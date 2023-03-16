#replacement 
from dataclasses import replace
import re
# c=a.replace("sundaram","paro")
# print (c)
a="a.my name isxyy sundaram"
# if (a.count("m")>0):
#     print("Match found")
# else:
#     print("Match not found")
a = a.replace("sundaram", "Parikshit")
y=re.search("d",a)
if y:
    print("match")
else:
    print ("not match")
print(a)