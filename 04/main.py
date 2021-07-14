#贪婪算法

li=[['a',200,20],['b',20,4],['c',175,10],['d',50,2],['e',10,1],['f',90,9]]
load=20
pac=[]
for x in li:
    pr=x[1]/x[2]
    x.append(pr)
li.sort(key=lambda x:x[3],reverse=True)
print(li)
for x in li:
    if load-x[2]>=0:
        load-=x[2]
        pac.append(x)
    else :
        break
print(pac)