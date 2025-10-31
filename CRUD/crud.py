import pandas as pd
import os

FILE_NAME = 'kontak.csv'
COLUMNS = ['Nama', 'Telepon', 'Email']

def muat_data():
    """Memuat data dari CSV atau membuat DataFrame kosong jika file tidak ada."""
    if os.path.exists(FILE_NAME):
        try:
            df = pd.read_csv(FILE_NAME)
            print(f"Data Kontak ({len(df)} entri) berhasil dimuat.")
            return df
        except Exception as e:
            # Menggunakan pd.DataFrame, bukan pd.Dataframe (perbaikan kecil)
            print(f"Error saat memuat file CSV: {e}")
            return pd.DataFrame(columns=COLUMNS) 
    else:
        print("File Kontak.csv tidak ditemukan. Membuat daftar kontak baru.")
        return pd.DataFrame(columns=COLUMNS)
    
def simpan_data(df):
    """Menyimpan DataFrame ke file CSV."""
    df.to_csv(FILE_NAME, index=False)
    print("\n✅ Data Kontak berhasil disimpan ke kontak.csv")

# =========================================================================
# LOGIKA INTI (CRUD: CREATE, READ, UPDATE, DELETE)
# =========================================================================

def tambah_kontak(df):
    print("\n--- Tambah Kontak Baru ---")
    nama = input("Nama: ")
    telepon = input("Nomor Telepon: ")
    email = input("Email: ")

    kontak_baru = {'Nama': nama, 'Telepon': telepon, 'Email': email}

    df_baru = pd.DataFrame([kontak_baru])
    df = pd.concat([df, df_baru], ignore_index=True)

    print(f"\n[Kontak '{nama}' berhasil ditambahkan!]")
    return df

def lihat_kontak(df):
    if df.empty:
        print("\nDaftar kontak kosong.")
        return
    
    print("\n--- Daftar Semua Kontak ---")
    print(df.to_string(index=True)) # Index=True menampilkan nomor baris

def hapus_kontak(df):
    """Menghapus kontak berdasarkan nomor indeks."""
    if df.empty:
        print("\nDaftar kontak kosong, tidak ada yang bisa dihapus.")
        return df

    lihat_kontak(df) 
    
    try:
        indeks_untuk_dihapus = int(input("\nMasukkan NOMOR INDEKS kontak yang ingin dihapus: "))
        
        if indeks_untuk_dihapus in df.index:
            nama_kontak = df.loc[indeks_untuk_dihapus, 'Nama']
            
            # Menghapus baris berdasarkan indeks
            df = df.drop(index=indeks_untuk_dihapus, axis=0) 
            
            # Mengatur ulang indeks agar penomoran rapi
            df = df.reset_index(drop=True)
            
            print(f"\n🗑️ Kontak '{nama_kontak}' (Indeks: {indeks_untuk_dihapus}) berhasil dihapus.")
        else:
            print(f"Error: Indeks {indeks_untuk_dihapus} tidak ditemukan di daftar.")
            
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk Nomor Indeks.")
    
    return df

# =========================================================================
# MENU UTAMA
# =========================================================================

def menu_utama(df):
    while True:
        print("\n==============================")
        print("SISTEM PENGELOLA KONTAK (Pandas)")
        print("==============================")
        print("1. Lihat Semua Kontak")
        print("2. Tambah Kontak Baru")
        print("3. Hapus Kontak") # Sudah diimplementasi
        print("4. Simpan & Keluar")
        
        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == '1':
            lihat_kontak(df)
        elif pilihan == '2':
            df = tambah_kontak(df)
        elif pilihan == '3':
            df = hapus_kontak(df) # Panggil fungsi hapus
        elif pilihan == '4':
            simpan_data(df)
            print("Program diakhiri.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# =========================================================================
# PANGGILAN PROGRAM UTAMA
# =========================================================================
data_kontak = muat_data() # Pastikan ini di level teratas
if __name__ == "__main__":
    menu_utama(data_kontak)