# Exercise 4.1
print("Exercise 4.1")
x = 35
y = 7
print('x + y = ', x + y)
print('x - y = ', x - y)
print('x * y = ', x * y)
print('x / y = ', x / y)
print('x // y = ', x // y)
print('x ** y = ', x ** y, "\n")

# Exercise 4.2
print("Exercise 4.2")
x = 9
y = 15
print('x > y = ', x > y)
print('x < y = ', x < y)
print('x == y = ', x == y)
print('x != y = ', x != y)
print('x >= y = ', x >= y)
print('x <= y = ', x <= y, "\n")

# Exercise 4.3
print("Exercise 4.3")
v = (45 > 50) and (30 <= 9)
print(v)
w = ("Oktavianus" == "Oktavianus") or (28 <= 4)
print(w)
p = not (11 == 12)
print(p, "\n")

# Exercise 4.4
print("Exercise 4.4")
# Strings
str1 = "Teknik"
str2 = "Industri"
result = str1 + " " + str2
print(result, "\n")

# Exercise 4.5
print("Exercise 4.5")
str1 = "WK"
result = str1 * 6
print(result, "\n")

# Exercise 4.6
print("Exercise 4.6")
kata1 = "vian"
kata2 = "Oktavianus"
if kata1 in kata2:
    print(kata1, "is present in the string", kata2, "\n")
else:
    print("Not Found")

# Exercise 4.7
print("Exercise 4.7")
kata3 = "mu"
kata4 = "Oktavianus"
if kata3 in kata4:
    print(kata3, "is present in the string", kata4)
else:
    print("Not Found", "\n")

# Exercise 4.8
print("Exercise 4.8")
str3 = "Oktavianus Auwdri"
cha = str3[4]
print(cha, "\n")

# Exercise 4.9
print("Exercise 4.9")
str4 = "Oktavianus Auwdri"
substr = str4[4:8]
print(substr, "\n")

# Exercise 4.10
print("Exercise 4.10")
str5 = "Oktavianus Auwdri"
new_str5 = str5[0::3]
print(new_str5, "\n")

# Exercise 4.11
print("Exercise 4,11")
str6 = "Auwdri Oktavianus"
hasil = str6[::-1]
print(hasil, "\n")

# Exercise 4.12
print("Exercise 4.12")
a = 45
b = 15
c = a & b
print("Baris 1 - Nilai dari c adalah ", c)
c = a | b
print("Baris 2 - Nilai dari c adalah ", c)
c = a ^ b
print("Baris 3 - Nilai dari c adalah ", c)
c = ~a
print("Baris 4 - Nilai dari c adalah ", c)
c = a << 2
print("Baris 5 - Nilai dari c adalah ", c)
c = a >> 2
print("Baris 6 - Nilai dari c adalah ", c, "\n")
