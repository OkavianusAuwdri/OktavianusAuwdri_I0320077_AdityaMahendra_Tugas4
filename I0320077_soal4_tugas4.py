usia = int(input("Berapa usia kamu = "))
ujian = input("Apakah Anda sudah lulus ujian kualifikasi (Y / T) = ")

if usia >= 21 and ujian == 'Y':
    print("Anda dapat mendaftar di kursus.")
elif usia < 21 or ujian == 'T':
    print("Anda tidak dapat mendaftar di kursus.")