num = input("입력해주세요")

for i in range(1,10):
    print("{} x {} = {}".format(num,i,(int(num)*i)))
    
int_num = int(num)
print("{}*{}={}".format(int_num,1,int_num*1))
print("{}*{}={}".format(int_num,2,int_num*2))
print("{}*{}={}".format(int_num,3,int_num*3))
print("{}*{}={}".format(int_num,4,int_num*4))
print("{}*{}={}".format(int_num,5,int_num*5))
print("{}*{}={}".format(int_num,6,int_num*6))
print("{}*{}={}".format(int_num,7,int_num*7))
print("{}*{}={}".format(int_num,8,int_num*8))
print("{}*{}={}".format(int_num,9,int_num*9))    