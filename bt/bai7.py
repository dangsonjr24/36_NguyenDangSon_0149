def hoan_hao(n):
    
    if n<=1:
        return False
    tong_uoc=0
    for i in range(1,n):
       if n%i==0:
        tong_uoc+=i
        if tong_uoc==n:
           return False
        else:
           return True
so=int(input("Nhập vào một số:"))
if hoan_hao(so):
   print(so,("đây là số hoàn hảo"))
else:
   print(so,("đây không phải số hoàn hảo"))