target_tabungan = int(input("Target tabungan: "))

total_tabungan = 0
hari = 0

while total_tabungan < target_tabungan:
    hari += 1
    tabungan_harian = int(input(f"Tabungan hari ke-{hari}: "))
    total_tabungan += tabungan_harian
    print(f"Total tabungan setelah hari ke-{hari}: {total_tabungan}")

print(f"Target tabungan dalam {hari} hari")
print(f"Total tabungan akhir: {total_tabungan}")