N = input("Nhập dãy số cách nhau bởi dấu cách: ")
N = N.split()
N = [int(i) for i in N]
min_element = min(N)
print("Phần tử bé nhất trong dãy số là:", min_element)