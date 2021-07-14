# gcd

def do(a,b):
    try:
        while a%b!=0:
            a,b=b,a%b
        return b
    except ZeroDivisionError:
        print("no 0")


print(do(121,44))