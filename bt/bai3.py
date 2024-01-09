def doi_xung(n):
    flag=True
    if str(n)!=str(n)[::-1]:
        flag=False
    return flag
so=int(input("nhập vào một số:"))
if doi_xung(so):
    print(so,"đây là số đối xứng")
else:
    print(so,"đây không phải số đối xứng")
    