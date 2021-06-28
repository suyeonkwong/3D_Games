from random import random
mine = input("홀/짝을 고르시오")
com = ""
result = ""

print(mine)

rnd = random()
if rnd>0.5:
    com = "홀"
else:
    com = "짝"
    
if mine == com:
    result = "승리"
else :
    result = "패배"
    
print("mine", mine)
print("com", com)
print("result", result)

#myhw01
#가위 바위 보
#myhw02
#첫째수를 입력하시오 1 input
#끝수를 입력하시오 3
#my03 구구단을 선택하시오 3

