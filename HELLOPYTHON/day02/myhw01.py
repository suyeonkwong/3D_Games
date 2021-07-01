from random import random
mine = input("가위/바위/보를 고르시오")
com = ""
result = ""

print(mine)

rnd = random()
if rnd>0.66:
    com = "가위"
elif rnd>0.33:
    com = "바위"
else:
    com = "보"
     
    
print("mine", mine)
print("com", com)
print("result", result)