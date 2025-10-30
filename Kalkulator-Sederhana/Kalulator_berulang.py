def hitung():
    print("\nPilih Operasi:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Keluar (x)")

    pilihan = input("Masukan Pilihan (1/2/3/4/5 atau operator): ")


    #pilihan untuk Keluar
    if pilihan == '5' or pilihan.lower() == 'x' : 
        return False #mengembalikan false untuk menghentikan loop utama
    
    operator_map = {'1': '+', '2': '-', '3': '*', '4': '/', '+': '+', '-': '-', '*': '*', '/': '/'}
    operator = operator_map.get(pilihan, pilihan) #ambil operator, jika tidak ada gunakan input asli

    #validasi operator
    if operator not in ['+', '-', '*', '/']:
        print("Pilihan atau operator tidak valid.")
        return True #lanjutkan Loop

    try: 
        angka1 = float(input("Masukan angka pertama: "))
        angka2 = float(input("Masukan angka kedua: "))
    except ValueError:
        print("Input tidak valid. Harap masukan angka!")
        return True
    
    if operator == '+':
        hasil = angka1 + angka2
    elif operator == '-':
        hasil = angka1 - angka2
    elif operator == '*':
        hasil = angka1 * angka2
    elif operator == '/':
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            print("Eror! Tidak bisa di bagi nol!")
            return True 
    
    print(f"\nHasil dari {angka1} {operator} {angka2} adalah: **{hasil}**")
    return True #mengembalikan true untuk melanjutkan loop

    # ---Main Program---
berjalan = True
print("Selamat datang di kalkulator berulang!")
while berjalan:
    #fungsi hitung() akan mengembalikan False jika pengguna memilih keluar
    berjalan = hitung()

print("Terima Kasih! Kalkulator di matikan!.")