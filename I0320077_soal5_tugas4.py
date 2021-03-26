s = "String bad can come!"
# Panjangnya harus 20
print("panjang dari s = %d" % len(s), "\n")

# Huruf pertama 'a' harusnya di index no 8
print("Kemunculan pertama a = %d" % s.index("a"), "\n")

# Jumlah huruf a harusnya 2
print("a muncul sebanayak %d kali" % s.count("a"), "\n")

# Memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'" % s[:5])  # Start to 5
print("Lima karakter berikutnya adalah '%s'" % s[5:10])  # 5 to 10
print("Karakter ketiga belas adalah '%s'" % s[12])  # Just number 12
print("Karakter dengan indeks ganjil adalah '%s'" % s[1::2])  # (0-based indexing)
print("Lima karakter terakhir adalah '%s'" % s[-5:])  # 5th-from-last to end

# Konversikan ke upercase
print("String dalam huruf besar: %s" % s.upper())

# Konversikan ke lowercase
print("String dalam huruf kecil: %s" % s.lower())

# Cek bagaimana string itu dimulai
if s.startswith("Str"):
    print("String dimulai dengan 'Str' . Good!")

# Cek bagaimana string itu diakhiri
if s.endswith("ome!"):
    print("String diahiri dengan 'ome!' . Good!")

# Pisahkan String menjadi tiga string yang terpisah
# Masing-masing hanya berisis satu kata
print("Pisahkan kata-kata dari string tersebut: %s" % s.split(" "))
