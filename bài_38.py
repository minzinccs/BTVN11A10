# nâng cao bài 37 ;-;???????????????? WTF this S**T!
N = int(input("Nhập số phần tử của mảng: "))
ar = []
sum_odd = 0
count_odd = 0
for i in range(N):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    ar.append(x)
    if x % 2 == 1:
        sum_odd += x
        count_odd += 1
print(f"Tổng các phần tử lẻ trong mảng là {sum_odd}")
print(f"Số lượng các phần tử lẻ trong mảng là {count_odd}")
