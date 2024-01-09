def chinh_phuong(n):
    if  n <  0 :
     return False
     flag=False
    for i in range(1,n+1):
      if i*i==n:
       flag=True
       break
     return flag
so=int(input(" nhập vào 1 số"))
if chinh_phuong(so):
   print(so,"là số chính phương")
else:
   print(so,"không phải số chính phương") 


