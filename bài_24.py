n = int(input("Nhập vào n: "))
sum = 0
for i in range(1, n, 2):
    sum += i
print("Tổng các số lẻ từ 1 đến", n, "là", sum)