n = int(input("Nhập số n: "))
if n >= 2:
    sum = 0
    for i in range(2, n+1, 2):
        sum += i
    print("Tổng các số chẵn từ 1 đến", n, "là", sum)
else:
    print("n phải lớn hơn hoặc bằng 2.")