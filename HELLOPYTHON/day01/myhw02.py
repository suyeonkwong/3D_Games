first = (int)(input("첫째수를 입력하세요"))
last = (int)(input("끝수를 입력하세요"))
sum = 0
for i in range(first, last+1):
    sum+=i
print("sum",sum)