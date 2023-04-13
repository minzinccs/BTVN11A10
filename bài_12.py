a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a > 0 and b > 0 and c > 0:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Là 3 cạnh của tam giác vuông.")
    else:
        print("Không là 3 cạnh của tam giác vuông.")
else:
    print("Các cạnh phải lớn hơn 0.")

