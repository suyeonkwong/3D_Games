first = (int)(input("첫째수를 입력하세요"))
last = (int)(input("끝수를 입력하세요"))
sum = 0
for i in range(first, last+1): #자바와 다르게 range안쓰면 for문 쓸 수 없음
    sum+=i
print("sum",sum)