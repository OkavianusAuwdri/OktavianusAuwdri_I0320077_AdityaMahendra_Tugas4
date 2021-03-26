a = 4
b = 11
c = a | b
print("a). Nilai c yaitu = ", c, " ", "binary = ", format(c, '08b'))
c = a >> b
print("b). Nilai c yaitu = ", c, " ", "binary = ", format(c, '08b'))
c = a ^ b
print("c). Nilai c yaitu = ", c, " ", "binary = ", format(c, '08b'))
c = ~a
print("d). Nilai c yaitu = ", c, " ", "binary = ", format(c, '08b'))
c = b & a
print("e). Nilai c yaitu = ", c, " ", "binary = ", format(c, '08b'))