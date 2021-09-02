while(True):
    print("="*64)
    print(">> Program Konversi Ruang Warna")
    print("="*64)
    print("""
    1. Pilih Foto
    2. Konversi Ruang Warna
    3. Exit Program
    """)
    print("="*64)
    menuUtama = input("Masukan pilihan : ")
    if(menuUtama == "1"):
        print("""
        1. Foto Bunga
        2. Foto Rubik
        """)
        menuFoto = input("Masukan pilihan : ")
    elif(menuUtama == "2"):
        print("""
        1. RGB ke HLS
        2. RGB ke HSV
        3. RGB ke GRAY
        4. RGB ke LUV
        5. RGB ke LAB
        """)
        menuKonversi = input("Masukan pilihan : ")
    elif(menuUtama == "3"):
        break
