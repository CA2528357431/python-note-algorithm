# 寻找相邻若干个数字，使之和最大



def do(li):
    n = len(li)
    if n > 1:

        left,left_li = do(li[0:n // 2])
        rigrt,rigrt_li = do(li[n // 2:n])

        middle = findmiddle(li)[0]
        middle_li = findmiddle(li)[1]


        maxi = max(left, rigrt, middle)

        if middle == maxi:
            neoli = middle_li.copy()


        elif left == maxi:
            neoli = left_li.copy()

        else:
            neoli = rigrt_li.copy()
        return maxi, neoli
    elif n == 1:
        return li[0], li
    else:
        return 0, li

def findmiddle(li):
    le = len(li)

    leftnum = -100000
    rightnum = -100000
    for x in range(0,le//2):
        sum = 0
        for y in range(x,le//2):
            sum += li[y]
        if sum>leftnum:
            leftnum = sum
            left = x
    for x in range(le//2,le):
        sum = 0
        for y in range(le//2,x+1):
            sum += li[y]
        if sum>rightnum:
            rightnum = sum
            right = x
    return rightnum+leftnum,li[left:right+1]


li = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(do(li))