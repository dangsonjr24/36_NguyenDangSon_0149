def nguyen_to(n):
    if n <= 1:
        return False
    flag=True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return flag
so=int(input("Nhập vào số thứ nhất:"))

if nguyen_to(so):
    print(so,"là số nguyên tố")
else:
    print(so,"không phải số nguyên tố") 
    