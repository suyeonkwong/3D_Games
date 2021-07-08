import numpy as np

arr = [1,2,3]
arr_n = np.array(arr) #원래는 [1,2,3] 인데 np의 array함수를 쓰면 [1 2 3]

arr_n = arr_n % 2

print(arr_n) 