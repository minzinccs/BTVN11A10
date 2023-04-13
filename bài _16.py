a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

if a > b:
    if a > c:
        print("Giá trị lớn nhất là:", a)
    else:
        print("Giá trị lớn nhất là:", c)
else:
    if b > c:
        print("Giá trị lớn nhất là:", b)
    else:
        print("Giá trị lớn nhất là:", c)
