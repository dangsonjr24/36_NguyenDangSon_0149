def chan_le(n):
    if n % 2 == 0:
        return True
    else:
        return False
so=int(input("xin mời nhập số:"))
if chan_le(so):
    
        print(so,"là số chẵn ")
else:        
        print(so,"là số lẻ")