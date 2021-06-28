from random import random
mine = input("가위/바위/보 고르시오")
com = ""
result = ""

print(mine)

rnd = random()
if rnd>0.5:
    com = "가위"
elif rnd>0.66:
    com = "바위"
else :
    com = "보"
    
if mine=="가위" and com=="보" or mine=="바위" and com=="가위" or mine=="보" and com=="바위":
    result = "승리"
elif mine == com:
    result = "비김"
else :
    result = "패배"

print("mine", mine)
print("com", com)
print("result", result)    