# Nhập độ dài
b=float(input('nhập b là độ dài cạnh b:'))
a=float(input('Nhập a là độ dài cạnh a:'))

#Thêm điều kiện cơ bản đẻ chạy chương trình:
if a<0 or b<0 or a==0 or b==0:
    print('xin mời chạy và nhập đúng dữ liệu')
else:
    c=(a+b)*2
    s=a*b
    print('Chu vi:',c)
    print('Diện tích:',s)
