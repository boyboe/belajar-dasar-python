import pandas as pd
import matplotlib.pyplot as plt


FILE_NAME = 'penjualan.csv'

def analisis_data_penjualan():
    print("--- Memulai Analisis Data Penjualan ---")
    
    try: 
        df =pd.read_csv(FILE_NAME)
        print(f"Data berhasil dimuat. Total baris: {len(df)}")
    except FileNotFoundError:
        print(f"ERROR: File {FILE_NAME} tidak ditemukan. Pastikan anda sudah mebuatnya.")
        return
    
    print("\n[Tantangan 1 : Mengubah Tipe Data ]")

    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    print("Tipe data adalah Konversi: ")
    print(df.dtypes)

    print("/n[Tantangan 2 : Membuat Kolom Kategori Penjualan]")

    df['Kategori_Penjualan'] = (
        df['jumlah_Penjualan'].apply(lambda x: 'Tinggi' if x > 150000 else 'Rendah')
    )
    print("\nDataframe setelah penambahan kolom Kategori_Penjualan: ")
    print(df[['jumlah_penjualan','kategori_penjualan']].head(8))

    print("\nTantangan 3 : Agregasi Data")

    penjualan_per_produk = df.grouphby('Produk')['jumlah_penjualan'].sum().sort_values(ascending = False)
    print("\nTotal Penjualan per Produk")
    print(penjualan_per_produk)


    rata_rata_per_kota = df.grouphby('Kota')['jumlah_penjualan'].mean().round(2)
    print("\nRata -rata Penjualan per Kota")
    print(rata_rata_per_kota)

    print("\nTantangan 4 : Visualisasi Data")

    plt.figure(figsize=(8,5))
    penjualan_per_produk.plot(kind='bar', color=['skyblue','salmon','lightgreen'])
    plt.title('Total Penjualan Berdasarkan Produk')
    plt.xlabel('Produk')
    plt.ylabel('Total Penjualan (Rp)')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--')
    plt.show()

    print("\n--- Analisis Selesai ---")

if __name__ == "__main__":
    analisis_data_penjualan()