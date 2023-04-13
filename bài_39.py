n = int(input("Nhập số lượng phần tử của mảng: "))
a = []
for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    a.append(x)
# làm bằng tiếng việt vui vãi!
tong_chan = 0
dem_chan = 0
for x in a:
    if x % 2 == 0:
        tong_chan += x
        dem_chan += 1
print("Tổng các phần tử chẵn trong mảng là:", tong_chan)
print("Số lượng các phần tử chẵn trong mảng là:", dem_chan)