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
    3. RGB ke YCrCb
    4. RGB ke LUV
    5. RGB ke LAB
    """)
    menuKonversi = input("Masukan pilihan : ")
    if(menuKonversi == "1"):
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_RGB2HLS)
        KonversiWarna(foto, warna, "RGB ke HLS")
    elif(menuKonversi == "2"):
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_RGB2HSV)
        KonversiWarna(foto, warna, "RGB ke HSV")
    elif(menuKonversi == "3"):
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_RGB2YCrCb)
        KonversiWarna(foto, warna, "RGB ke YCrCb")
    elif(menuKonversi == "4"):
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_RGB2LUV)
        KonversiWarna(foto, warna, "RGB ke LUV")
    elif(menuKonversi == "5"):
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_RGB2LAB)
        KonversiWarna(foto, warna, "RGB ke LAB")
    else:
        print("Piihan tidak ada")
        input("Tekan apa saja untuk melanjutkan")


def main():
    fotoBunga = cv.imread("Foto bunga.jpeg")
    dimension = (369, 492)  # ukuran foto yang baru
    foto = cv.resize(fotoBunga, dimension)  # untuk mengatur ukuran foto
    while(True):
        print("="*64)
        print(">> Program Konversi Ruang Warna")
        print("="*64)
        print("""
        1. Lihat foto
        2. Konversi Ruang Warna
        3. Exit Program
        """)
        print("="*64)
        menuUtama = input("Masukan pilihan : ")
        if(menuUtama == "1"):
            cv.imshow("Foto Asli", foto)  # untuk menampilkan foto ke layar
            cv.waitKey()  # menunggu inputan untuk menutup windows foto
            os.system("cls")
        elif(menuUtama == "2"):
            menuKonversiRuangWarna(foto)
            os.system("cls")
        elif(menuUtama == "3"):
            print("Program Exit")
            break
        else:
            print("Pilihan tidak ada")
            input("Tekan apa saja untuk melanjutkan")
            os.system("cls")


main()
