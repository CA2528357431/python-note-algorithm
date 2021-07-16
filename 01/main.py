# 排序


# 简单选择排序
def meth1(li):
    for x in range(0, len(li)):
        min = x
        for y in range(x, len(li)):
            if li[min] > li[y]:
                min = y
        tempt = li[x]
        li[x] = li[min]
        li[min] = tempt

    return li


# 冒泡排序
def meth2(li):
    for x in range(0, len(li) - 1):
        for y in range(0, len(li) - 1 - x):
            if li[y + 1] < li[y]:
                tempt = li[y]
                li[y] = li[y + 1]
                li[y + 1] = tempt
    return li


# 搅拌排序
def meth3(li):
    for x in range(0, len(li) // 2 + 1):
        for y in range(x, len(li) - 1 - x):
            if li[y + 1] < li[y]:
                tempt = li[y]
                li[y] = li[y + 1]
                li[y + 1] = tempt
        for y in range(len(li) - 1 - x - 1, x, -1):
            if li[y - 1] > li[y]:
                tempt = li[y]
                li[y] = li[y - 1]
                li[y - 1] = tempt
    return li


# 合并排序
def meth4(li):
    def merge(a, b):
        re = []
        while True:
            if a and b:

                if a[0] < b[0]:
                    re.append(a[0])
                    a.pop(0)
                else:
                    re.append(b[0])
                    b.pop(0)
            elif a:
                re.append(a[0])
                a.pop(0)
            elif b:
                re.append(b[0])
                b.pop(0)
            else:
                break
        return re

    if (len(li) < 2):
        return li
    middle = len(li) // 2
    left = li[0:middle]
    right = li[middle:]
    res = merge(meth4(left), meth4(right))
    return res


# 快速排序
def meth5(data):
    if len(data) >= 2:
        mid = data[len(data) // 2]
        left = []
        right = []
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return meth5(left) + [mid] + meth5(right)
    else:
        return data

# 插入排序
def meth6(data):
    for x in range(0,len(data)):
        temp = data[x]
        parser = x-1
        while parser>=0 and temp<data[parser]:
            data[parser+1] = data[parser]
            parser-=1
        data[parser+1] = temp
    return data








if __name__ == '__main__':
    li = [9, 3, 7, 7, 8, 1, 5, 3, 1, -3, -2]
    print(meth1(li.copy()))
    print(meth2(li.copy()))
    print(meth3(li.copy()))
    print(meth4(li.copy()))
    print(meth5(li.copy()))
    print(meth6(li.copy()))