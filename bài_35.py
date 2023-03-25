N = input("Nhập nhiệt độ của các ngày cách nhau bởi dấu cách: ")
N = N.split()
N = [int(i) for i in N]

# Tính nhiệt độ trung bình
average_temperature = sum(N) / len(N)
print("Nhiệt độ trung bình của các ngày là:", average_temperature)

# Tính số ngày có nhiệt độ cao hơn nhiệt độ trung bình
count = 0
for temperature in N:
    if temperature > average_temperature:
        count += 1
print("Số ngày có nhiệt độ cao hơn nhiệt độ trung bình là:", count)