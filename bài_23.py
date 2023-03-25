n = int(input("Nhập vào n: "))
sum = 0
for i in range(1, n, 2):
    sum += i
print("Tổng các phần tử lẻ nhỏ hơn", n, "là", sum)