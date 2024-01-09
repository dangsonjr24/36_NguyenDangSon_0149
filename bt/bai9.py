def so_fibonacci(n):
    f0= 0
    f1=1
    fn=1
    if n <0:
        return False
    for i in range(0,n):
        f0=f1
        f1=fn
        fn=f0+f1
        return True
so=int(input("Nhập vào một số:"))
if so_fibonacci(so):
    print(so,"đây là dãy fibonacci")
else:
    print(so,"đây không phải dãy fb")

