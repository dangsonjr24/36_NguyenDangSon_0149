def so_hoan_hao(n):
    tong = 0
    if n < 1:
        return False
    for i in range(1, n):
        if n % i == 0:
            tong += i
    flag = False
    if tong == n:
        flag = True
    return flag
so=int(input("Nhập vào một số:"))
if so_hoan_hao(so):
   print(so,("đây là số hoàn hảo"))
else:
   print(so,("đây không phải số hoàn hảo"))