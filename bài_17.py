n = int(input("Nhập số n: "))
if n >= 1:
    sum = 0
    for i in range(1, n+1):
        sum += i
    print("Tổng các số nguyên dương từ 1 đến", n, "là", sum)
else:
    print("n phải lớn hơn hoặc bằng 1.")