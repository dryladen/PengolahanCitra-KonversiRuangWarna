import cv2 as cv  # library untuk image prossecing
import numpy as np


def KonversiWarna(foto, warna, judul):
    banding = np.hstack((foto, warna))
    cv.imshow(judul, banding)
    cv.waitKey()


def menuKonversiRuangWarna():
    dim = (269, 392)
    resized = cv.resize(fotoBunga, dim)
    print("""
    1. RGB ke HLS
    2. RGB ke HSV
    3. RGB ke YCrCb
    4. RGB ke LUV
    5. RGB ke LAB
    """)
    menuKonversi = input("Masukan pilihan : ")
    if(menuKonversi == "1"):
        warna = cv.cvtColor(resized, cv.COLOR_RGB2HLS)
        KonversiWarna(resized, warna, "RGB ke HLS")
    elif(menuKonversi == "2"):
        warna = cv.cvtColor(resized, cv.COLOR_RGB2HSV)
        KonversiWarna(resized, warna, "RGB ke HSV")
    elif(menuKonversi == "3"):
        warna = cv.cvtColor(resized, cv.COLOR_RGB2YCrCb)
        KonversiWarna(resized, warna, "RGB ke YCrCb")
    elif(menuKonversi == "4"):
        warna = cv.cvtColor(resized, cv.COLOR_RGB2LUV)
        KonversiWarna(resized, warna, "RGB ke LUV")
    elif(menuKonversi == "5"):
        warna = cv.cvtColor(resized, cv.COLOR_RGB2LAB)
        KonversiWarna(resized, warna, "RGB ke LAB")
    else:
        print("Piihan tidak ada")


fotoBunga = cv.imread("Foto bunga.jpeg")
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
        pass
    elif(menuUtama == "2"):
        menuKonversiRuangWarna()
    elif(menuUtama == "3"):
        break
