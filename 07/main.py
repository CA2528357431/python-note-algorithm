import time

li = [{1, 2}, {1, 3}, {1, 4}, {2, 3}, {4, 5},{5,6}]
total = set()
for x in li :
    total = x|total

def do(li,total):
    def check(x, te):
        judge = True
        for y in te:
            if {x,y} not in li:
                judge = False
        return judge


    group = []
    while total:
        te = set()
        for x in total:
            time.sleep(0.5)
            if (check(x,te)):
                te.add(x)
        for x in te:
            total.remove(x)
        group.append(te)
    return group


print(do(li,total))
