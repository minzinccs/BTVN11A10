a = input("Nhập tên học sinh thứ nhất: ")
b = input("Nhập tên học sinh thứ hai: ")
if len(a) > len(b):
    print("Tên học sinh có độ dài lớn hơn là", a)
elif len(a) < len(b):
    print("Tên học sinh có độ dài lớn hơn là", b)
else:
    print("Hai tên học sinh có độ dài bằng nhau.")