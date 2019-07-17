hao=1
caidan=['米饭','番茄炒鸡蛋','白切鸡','排骨','白菜','茄子']
while True:

    num=1
    liao=[]
    print("What do you want to add:\n"+str(num)+".")
    while True:
        zeng=input()
        if zeng in caidan:
            liao.append(zeng)
            num+=1
            print("OK\n"+str(num)+".")


        elif zeng=='quit':

            hao+=1
            print(str(hao)+"号"+"That's all,you need")
            for u in liao:
                print(u)
            break
        elif zeng=='delete':


            print("Which do you want to delete")
            while True:

                jian=input()
                if jian in liao:
                    liao.remove(jian)
                    num-=1

                elif jian=='back':
                    break


                else:
                    print("请重新输入")
          #  print(str(num)+".")
        else:
            print("对不起，没有这个菜")
            print(str(num)+".")




