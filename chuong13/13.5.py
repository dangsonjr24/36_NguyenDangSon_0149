f=open("bai_tho.txt","r+")
a=f.read(12)
print('Nội dung là: \n',a)
b=f.tell()
print('Vị trí hiện tại:',b)
f.seek(0)
c=f.read(12)
print('Các ký tự đọc được sau khi trả về vị trí đầu tiên là: \n',c)