n = int(input("Nhap so phan tu cua day: "))
arr = []


for i in range(n):
    num = int(input(f"Nhap phan tu thu {i+1}: "))
    arr.append(num)

sum = sum(arr)
avg = sum / n

print("Tong cac phan tu cua day:", sum)
print("Trung binh cong cac phan tu cua day:", avg)