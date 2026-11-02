name = input("Telebenin adi: ")

m1 = float(input("1-ci imtahan bali: "))
m2 = float(input("2-ci imtahan bali: "))

average = (m1 + m2) / 2

print("\nTelebe:", name)
print("Orta bal:", round(average, 2))

if average >= 51:
    print("Netice: Kecdi")
else:
    print("Netice: Kesildi")