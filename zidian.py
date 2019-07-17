xinxi={'姓氏':'杨','名字':'靓仔','住址':'广东','年龄':str(20),'爱好':'数据挖掘'}
for i,j in xinxi.items():
    print('i: '+i)
    print('j: '+j)
    print("\n")
print(xinxi['姓氏'])
xinxi['学历']='研究生'
print(xinxi['学历'])
print(xinxi)