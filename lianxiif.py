car='subaru'
print("请输入您的答案：")
#daan=(car==answer)
i=0
while(i<3):
    answer=input()
    answer=answer.lower()
    i+=1
    if((i!=3)&(answer!=car)):
        print("错误，请重新输入：")
    if((i==3)&(answer!=car)):
        print("错误,您的机会已用完")
    if(answer==car):
        print("恭喜您，答案正确，请与工作人员兑换奖品")

