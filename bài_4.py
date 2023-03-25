print('Nhập đ dài của 3 cạnh tam giác:')
a=float(input('nhập độ dài cạnh a:'))
b=float(input('nhập đọ dài cạnh b:'))
c=float(input('nhập độ dài cạnh c:'))
cv=a+b+c
p=cv/2
import math
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
#bị giới hạn yêu cầu vì sqrt cần hàm phụ để tính được trường hợp số âm
# thử 1 2 3 4 5 6 7 8 9 10 
print('Chu vi tam giác là:',cv)
print('Diện tích tam giác là:',dt)
