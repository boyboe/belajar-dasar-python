angka1 = float(input("Masukan angka pertama: "))
operator = input("Masukan operator (+, -, *, /) :")
angka2 = float(input("Masukan angka kedua: "))

if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    if angka2 != 0 :
        hasil = angka1 / angka2
    else : 
        "hasil eror tidak bisa di bagi nol"

else: 
    "hasil operator tidak valid"

print("Hasil:", hasil)