import math
s = input("Enter your float list:")
o = list(map(float,s.split()))
print(o)
for i in o:
    print(math.sin(i))