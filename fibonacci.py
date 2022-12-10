#0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fibanacci(n):
    a=0
    b=1
    if n <0:
        print("incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(n):
            c = a + b
            #print(c)
            a = b
            b = c
        return b
    
def fibo_r(n):
    if (n <= 0):
        return -1
    if n==1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_r(n-1)+fibo_r(n-2)

print(fibanacci(9))
print(fibo_r(9))

##0, 1, 1
##a


