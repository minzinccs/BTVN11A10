# Nhập vào chiều cao và 2 đáy của hình thang
d1 = float(input("Nhập độ dài đáy lớn: "))
d2 = float(input("Nhập độ dài đáy nhỏ: "))
h = float(input("Nhập chiều cao: "))

# Tính diện tích hình thang
s = (d1 + d2) * h / 2

# In kết quả
print("Diện tích hình thang là:", s)