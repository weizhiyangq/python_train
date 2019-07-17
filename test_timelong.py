import time
a=list(range(0,100000000))
a_len=len(a)
num=0
start=time.time()
'''
for i in range(0,a_len):
    if a[i]>10000:
        num+=1
'''
for i in a:
    if i >10000:
        num+=1

stop=time.time()
long=stop-start
print(long)
print(num)
