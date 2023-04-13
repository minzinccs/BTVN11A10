N = int(input("Nhập số phần tử của mảng: "))
ar = []
for i in range(N):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    ar.append(x)
    # tương tụ bài 36
sum_odd = 0
for i in ar:
    if i % 2 != 0:
        sum_odd += i
        # chú ý là lẻ thì !=0 còn chẵn thì ==0
print("Tổng các phần tử lẻ trong mảng là:", sum_odd)