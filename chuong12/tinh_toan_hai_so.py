#Module tính toán hai số
import math
def tong(x,y):
    return x+y
def hieu(x,y):
    return x-y
from tinh_toan_hai_so import tong,hieu
x,y=3,5
print("Tong",x,"+",y,"=",tong(x,y))
print("Hieu",x,"-",y,"=",hieu(x,y))
