#查找

#顺序查找
def meth1(a,b):
    for x,y in enumerate(a):
        if y==b:
            return x
    else:
        return -1

#折半查找
def meth2(a,b):
    start=0
    end=len(a) - 1
    while start<=end:
        mid = (start+end)// 2
        if b > a[mid]:
            start = mid + 1
        elif b < a[mid]:
            end = mid - 1
        else:
            return mid
    return -1
#只应用于带序list


if __name__ == '__main__':
    li=['23','well',34,-1,78,'c']
    tar=-1
    print(meth1(li,tar))

    li = [-7,-3,0,6,19,100]
    tar = 0
    print(meth2(li, tar))