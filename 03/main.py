#穷举法

#百钱百鸡
#大鸡5 中鸡3 小鸡1/3
re=[]
for x in range(0,20):
    for y in range(0,33):
        z=100-x-y
        li=[x,y,z]
        if x*5+y*3+z/3==100:
            re.append(li)
print(re)

#A、B、C、D、E五人捕鱼
#A将鱼分为5份 扔掉多余的1条
#B\C、D、E依次醒来也按同样的方式分鱼
# 问他们至少捕了多少条鱼
fish=1
while True:
    total=fish
    judge=True
    for _ in range(0,5):
        if total%5!=1 or  total//5==0:
            judge = False
            break

        total=(total-1)*4/5
    if judge==True:
        print(fish)
        break

    else:
        fish+=5