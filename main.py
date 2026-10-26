name = input("Telebenin adi: ")

m1 = float(input("1-ci imtahan bali: "))
m2 = float(input("2-ci imtahan bali: "))
m3 = float(input("3-cu imtahan bali: "))

average = (m1 + m2 + m3) / 3

print("\nTelebe:", name)
print("Orta bal:", round(average, 2))

if average >= 51:
    print("Netice: Kecdi")
else:
    print("Netice: Kesildi")