n = int(input("Nhập n: "))
tong = 0
for i in range(1, n+1, 2):
    tong += i
print("Tổng các số lẻ từ 1 đến", n, "là", tong)