import math
print("giải phương trình bậc 2:")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm.")
elif delta == 0:
    x = -b/(2*a)
    print("Phương trình có nghiệm kép x1 = x2 = ", x)
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("Phương trình có hai nghiệm phân biệt là x1 = ", x1, " và x2 = ", x2)