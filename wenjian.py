
with open('pi_digits.txt','a') as file_object:
    #contents=file_object.read()
    #print(contents.rstrip())
    #lines=file_object.readlines()
    #for line in lines:
        # print(line.rstrip())
        file_object.write("\nI LOVE YOU QQ\n")
        file_object.write("I LOVE YOU WEIXIN")
        file_object.write("我爱你python")
'''
while True:
    print ("beichushu:")
    beichushu=input()
    if beichushu=='quit':
        break
    print("chushu:")
    chushu=input()
    if chushu=='quit':
        break
    try:
        answer=int(beichushu)/int(chushu)
    except ZeroDivisionError:
        print("chushu can't be zero")
    else:
        print(answer)
'''



