N = int(input("Nhập số phần tử của mảng: "))
ar = []
for i in range(N):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    ar.append(x)
# nó chỉ là hiện ra một cái gì đây thôi đừng để ý!
sum_even = 0
for i in ar:
    if i % 2 == 0:
        sum_even += i
print("Tổng các phần tử chẵn trong mảng là:", sum_even)