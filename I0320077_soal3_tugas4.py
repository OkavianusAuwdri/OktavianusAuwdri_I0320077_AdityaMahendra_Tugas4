max_lb = 50
max_kg = max_lb * 0.453592
print("Berat maskimal yang diperbolehkan = ", max_kg, " kg")
barang_a = 110
print("Berat barang A = ", barang_a, " kg")
if barang_a > max_kg:
    print("Berat barang A melebihi batas maksimal")
else:
    print("Berat barang A tidak melebihi batas maksimal")
barang_b = 49
print("Berat Barang B = ", barang_b, " kg")
if barang_b > max_kg:
    print("Berat barang B melebihi batas maksimal")
else:
    print("Berat barang B tidak melebihi batas maksimal")