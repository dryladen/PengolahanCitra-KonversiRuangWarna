import cv2 as cv  # library untuk image processing
import numpy as np
import os  # library untuk clear screen


def KonversiWarna(foto, warna, judul):
    banding = np.hstack((foto, warna))
    cv.imshow(judul, banding)  # untuk menampilkan foto ke layar
    cv.waitKey()  # menunggu inputan untuk menutup windows foto


def menuKonversiRuangWarna(foto):
    print("""
    1. RGB ke HLS
    2. RGB ke HSV
    3. RGB ke YUV
    4. RGB ke LUV
    5. RGB ke LAB
    """)
    menuKonversi = input("Masukan pilihan : ")
    if(menuKonversi == "1"):
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_BGR2HLS)
        KonversiWarna(foto, warna, "RGB ke HLS")
    elif(menuKonversi == "2"):
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_BGR2HSV)
        KonversiWarna(foto, warna, "RGB ke HSV")
    elif(menuKonversi == "3"):
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_BGR2YUV)
        KonversiWarna(foto, warna, "RGB ke YUV")
    elif(menuKonversi == "4"):
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_BGR2LUV)
        KonversiWarna(foto, warna, "RGB ke LUV")
    elif(menuKonversi == "5"):
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_BGR2LAB)
        KonversiWarna(foto, warna, "RGB ke LAB")
    else:
        print("Piihan tidak ada")
        input("Tekan apa saja untuk melanjutkan")


def menuBins():
    print("""
    1. 256 Bins
    2. 32 Bins
    3. 16 Bins
    4. 8 Bins
    5. 4 Bins
    """)
    menu1 = input("Masukan pilihan : ")
    if(menu1 == "1"):
        pass
    elif(menu1 == "2"):
        pass
    elif(menu1 == "3"):
        pass
    elif(menu1 == "4"):
        pass
    elif(menu1 == "5"):
        pass
    else:
        print("Pilihan tidak ada")
        input("Tekan apa saja untuk melanjutkan")


def menuHistogram():
    print("""
    1. Full histogram
    2. Histogram per channel
    """)
    menu1 = input("Masukan pilihan : ")
    if(menu1 == "1"):
        pass
    elif(menu1 == "2"):
        print("""
        1. Channel merah
        2. Channel Hijau
        3. Channel Biru
        """)
        menu2 = input("Masukan pilihan : ")
        if(menu2 == "1"):
            pass
        elif(menu2 == "2"):
            pass
        elif(menu2 == "3"):
            pass
        else:
            print("Pilihan tidak ada")
            input("Tekan apa saja untuk melanjutkan")
    else:
        print("Pilihan tidak ada")
        input("Tekan apa saja untuk melanjutkan")


def main():
    fotoBunga = cv.imread("Foto bunga.jpeg")
    dimension = (369, 492)  # ukuran foto yang baru
    # untuk mengatur dimension/ukuran foto
    foto = cv.resize(fotoBunga, dimension)
    while(True):
        print("="*64)
        print(">> Program Konversi Ruang Warna")
        print("="*64)
        print("""
        1. Lihat foto
        2. Konversi Ruang Warna
        3. Histogram
        4. Exit Program
        """)
        print("="*64)
        menuUtama = input("Masukan pilihan : ")
        if(menuUtama == "1"):
            cv.imshow("Foto Asli", foto)  # untuk menampilkan foto ke layar
            cv.waitKey()  # menunggu inputan untuk menutup windows foto
            os.system("cls")  # membersihkan tampilan menu
        elif(menuUtama == "2"):
            menuKonversiRuangWarna(foto)
            os.system("cls")
        elif(menuUtama == "4"):
            print("Program Exit")
            break
        else:
            print("Pilihan tidak ada")
            input("Tekan apa saja untuk melanjutkan")
            os.system("cls")


main()
