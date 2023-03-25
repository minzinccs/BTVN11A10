N = input("Nhập dãy số cách nhau bởi dấu cách: ")
N = N.split()
N = [int(i) for i in N]
max_element = max(N)
print("Phần tử lớn nhất trong dãy số là:", max_element)