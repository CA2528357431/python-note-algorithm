#回溯法

#八皇后问题

def main(n):
    res=[]
    queen=[None]*n
    linep=[None]*n
    linem=[None]*n

    def add(num):
        print(queen)

        if num==n:

            queenre=queen
            res.append(queenre)

        else:
            for x in range(0,n):
                if (x not in queen) and (x+num not in linep) and (x-num not in linem):

                    queen[num]=x
                    linep[num]=x+num
                    linem[num]=x-num

                    add(num+1)

                    queen[num] = None
                    linep[num] = None
                    linem[num] = None


    add(0)
    print(res)
    return res
main(4)
