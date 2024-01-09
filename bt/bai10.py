import math
a=int(input("nhập số thứ nhất:"))
b=int(input("Nhập số thứ hai:"))
if a<0 or b<0:
    print("số thứ nhất")
elif a>b:
    print("số thứ hai")
else:
    for n in range(a,b+1):
      for i in range(2,int(math.sqrt(n))+1):
          if n%i==0:
              break
          else:
              print(n,end="")
             
         