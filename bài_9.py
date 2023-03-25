# Nhập vào số KW điện tiêu thụ
so_kw = float(input("Nhập số KW điện tiêu thụ: "))

# Kiểm tra nếu số KW điện tiêu thụ bé hơn 0
if so_kw < 0:
    print("Số KW điện tiêu thụ không hợp lệ. Vui lòng nhập lại.")
else:
    # Tính số tiền phải trả
    if so_kw <= 50:
        tien_dien = so_kw * 1500
    elif so_kw <= 100:
        tien_dien = 50 * 1500 + (so_kw - 50) * 1700
    elif so_kw <= 150:
        tien_dien = 50 * 1500 + 50 * 1700 + (so_kw - 100) * 2000
    else:
        tien_dien = 50 * 1500 + 50 * 1700 + 50 * 2000 + (so_kw - 150) * 2500

    # In kết quả
    print("Số tiền phải trả là:", tien_dien, "nghìn đồng")
