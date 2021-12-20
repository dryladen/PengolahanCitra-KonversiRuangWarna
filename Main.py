import cv2 as cv  # library untuk image processing
import numpy as np
import os  # library untuk clear screen
from matplotlib import pyplot as plt  # untuk menampilkan histogram


def bandingGambar(foto1, foto2, judul):
    banding = np.hstack((foto1, foto2))
    cv.imshow(judul, banding)  # untuk menampilkan foto ke layar
    cv.waitKey()  # menunggu inputan untuk menutup windows foto


def fotoResize(gambar, gray=False):
    if gray == True:
        fotoAsli = cv.imread(
            gambar + ".jpg" if gambar == "Foto rubik" else gambar + ".jpeg", 0
        )
    else:
        fotoAsli = cv.imread(
            gambar + ".jpg" if gambar == "Foto rubik" else gambar + ".jpeg"
        )
    foto = cv.resize(fotoAsli, (600, 400) if gambar == "Foto rubik" else (369, 492))
    return foto


def menuKonversiRuangWarna(gambar):
    foto = fotoResize(gambar)
    print("=" * 64)
    print(
        """
    |  1. RGB ke HLS  |
    |  2. RGB ke HSV  |
    |  3. RGB ke YUV  |
    |  4. RGB ke LUV  |
    |  5. RGB ke LAB  |
    """
    )
    print("=" * 64)
    menuKonversi = input("Masukan pilihan : ")
    if menuKonversi == "1":
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_BGR2HLS)
        bandingGambar(foto, warna, "RGB ke HLS")
    elif menuKonversi == "2":
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_BGR2HSV)
        bandingGambar(foto, warna, "RGB ke HSV")
    elif menuKonversi == "3":
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_BGR2YUV)
        bandingGambar(foto, warna, "RGB ke YUV")
    elif menuKonversi == "4":
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_BGR2LUV)
        bandingGambar(foto, warna, "RGB ke LUV")
    elif menuKonversi == "5":
        # untuk konversi ruang warna
        warna = cv.cvtColor(foto, cv.COLOR_BGR2LAB)
        bandingGambar(foto, warna, "RGB ke LAB")
    else:
        print("Piihan tidak ada")
        input("Tekan apa saja untuk melanjutkan")


def menuPilihFoto(foto1, foto2, foto3):
    foto = foto1
    print("=" * 64)
    print(
        """
    |  1. Foto pemandangan (terang)  |
    |  2. Foto bunga (sedang)        |
    |  3. Foto rubik (gelap)         |
    """
    )
    print("=" * 64)
    menuPilihFoto = input("Masukan pilihan : ")
    if menuPilihFoto == "1":
        foto = foto1
    elif menuPilihFoto == "2":
        foto = foto2
    elif menuPilihFoto == "3":
        foto = foto3
    else:
        print("Pilihan tidak ada")
        input("Tekan apa saja untuk melanjutkan")
        return foto
    cv.imshow(foto, fotoResize(foto))
    cv.waitKey(0)
    return foto


def menuBins():
    bins = 256
    print("=" * 64)
    print(
        """
    |  1. 256 Bins  |
    |  2. 32 Bins   |
    |  3. 16 Bins   |
    |  4. 8 Bins    |
    |  5. 4 Bins    |
    """
    )
    print("=" * 64)
    menu1 = input("Masukan pilihan : ")
    if menu1 == "1":
        bins = 256
    elif menu1 == "2":
        bins = 32
    elif menu1 == "3":
        bins = 16
    elif menu1 == "4":
        bins = 8
    elif menu1 == "5":
        bins = 4
    else:
        print("Pilihan tidak ada")
        input("Tekan apa saja untuk melanjutkan")
    return bins


def menuPerChannel(gambar):
    foto = fotoResize(gambar)
    b, g, r = cv.split(foto)  # memisahkan warna per channel
    # untuk mengosongkan nilai warna channel lain
    zeros = np.zeros(foto.shape[:2], dtype="uint8")
    red_img = cv.merge([r, zeros, zeros])
    green_img = cv.merge([zeros, g, zeros])
    blue_img = cv.merge([zeros, zeros, b])
    print("=" * 64)
    print(
        """
    |  1. Red Channel    |
    |  2. Green Channel  |
    |  3. Blue Channel   |
    """
    )
    print("=" * 64)
    menu = input("Masukan pilihan : ")
    if menu == "1":
        x = r
        x_img = red_img
    elif menu == "2":
        x = g
        x_img = green_img
    elif menu == "3":
        x = b
        x_img = blue_img
    else:
        print("Pilihan tidak ada")
        input("Tekan apa saja untuk melanjutkan")
        return
    bins = menuBins()  # menentukan bins histogram
    plt.subplot(121)  # membagi plot
    plt.imshow(x_img)
    plt.subplot(122)
    plt.hist(x.ravel(), bins, [0, 256])  # membuat histogram
    plt.ylabel("[ Jumlah Intensitas ]")
    plt.xlabel("[ Nilai Intensitas ]")
    plt.show()


def menuHistogram(gambar):
    print("=" * 64)
    print(
        """
    |  1. Histogram Berwarna   |
    |  2. Histogram GrayScale  |
    """
    )
    print("=" * 64)
    menu1 = input("Masukan pilihan : ")
    if menu1 == "1":
        print("=" * 64)
        print(
            """
        |  1. Full Channel  |
        |  2. Per Channel   |
        """
        )
        print("=" * 64)
        menu2 = input("Masukan pilihan : ")
        if menu2 == "1":
            fotorgb = cv.cvtColor(fotoResize(gambar), cv.COLOR_BGR2RGB)
            color = ("b", "g", "r")
            plt.subplot(121)
            plt.imshow(fotorgb)
            plt.subplot(122)
            for i, col in enumerate(color):
                histr = cv.calcHist([fotoResize(gambar)], [i], None, [256], [0, 256])
                plt.plot(histr, color=col)
                plt.xlim([0, 256])
            plt.ylabel("[ Jumlah Intensitas ]")
            plt.xlabel("[ Nilai Intensitas ]")
            plt.show()
        elif menu2 == "2":
            menuPerChannel(gambar)
        else:
            print("Pilihan tidak ada")
            input("Tekan apa saja untuk melanjutkan")
    elif menu1 == "2":
        foto = fotoResize(gambar, True)
        bins = menuBins()  # untuk menentukan bins histogram
        plt.subplot(121)  # untuk membagi plot
        plt.imshow(foto, "gray")  # menampilkan foto
        plt.subplot(122)
        plt.hist(foto.ravel(), bins, [0, 256])  # membuat histogram
        plt.ylabel("[ Jumlah Intensitas ]")
        plt.xlabel("[ Nilai Intensitas ]")
        plt.show()
    else:
        print("Pilihan tidak ada")
        input("Tekan apa saja untuk melanjutkan")


def sharpening(foto):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    image_sharp = cv.filter2D(src=foto, ddepth=-1, kernel=kernel)
    bandingGambar(foto, image_sharp, "Sharpening")


def imageSretching(foto):
    imageSretch = cv.addWeighted(foto, 1, np.zeros(foto.shape, foto.dtype), 1, 0)
    bandingGambar(foto, imageSretch, "Stretching")


def imageBrightness(foto):
    hsv = cv.cvtColor(foto, cv.COLOR_BGR2HSV)
    nilai = int(input("Masukan nilai brightness [ > 20 ] : "))
    # dengan proses split hsv
    h, s, v = cv.split(hsv)
    v += nilai
    hsv = cv.merge((h, s, v))
    brightness_img = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    bandingGambar(foto, brightness_img, "Brightness")


def imageBlur(foto):
    imgBlur = cv.GaussianBlur(foto, (7, 7), 0)
    bandingGambar(foto, imgBlur, "Blur")


def imageEnchancement(foto):
    os.system("cls")
    gambar = fotoResize(foto)
    while True:
        print("=" * 64)
        print(
            """
        |  1. Image Sharpening   |
        |  2. Image Blur         |
        |  3. Image Brightness   |
        |  4. Kembali ke menu    |
        """
        )
        print("=" * 64)
        menu1 = input("Masukan pilihan : ")
        if menu1 == "1":
            sharpening(gambar)
        elif menu1 == "2":
            imageBlur(gambar)
        elif menu1 == "3":
            imageBrightness(gambar)
        elif menu1 == "4":
            break
        else:
            print("Pilihan tidak ada")
            input("Tekan apa saja untuk melanjutkan")
            os.system("cls")


def main():
    fotoPemandangan = "Foto pemandangan"
    fotoBunga = "Foto bunga"
    fotoRubik = "Foto rubik"
    foto = fotoPemandangan
    while True:
        print("=" * 64)
        print(">> Program Pengolahan Citra")
        print("=" * 64)
        print(
            """
        |  1. Pilih foto            |
        |  2. Konversi Ruang Warna  |
        |  3. Histogram             |
        |  4. Image Enchancement    |
        |  5. Exit Program          |
        """
        )
        print("=" * 64)
        menuUtama = input("Masukan pilihan : ")
        if menuUtama == "1":
            foto = menuPilihFoto(fotoPemandangan, fotoBunga, fotoRubik)
            os.system("cls")
        elif menuUtama == "2":
            menuKonversiRuangWarna(foto)
            os.system("cls")
        elif menuUtama == "3":
            menuHistogram(foto)
            os.system("cls")
        elif menuUtama == "4":
            imageEnchancement(foto)
        elif menuUtama == "5":
            print("Exit")
            break
        else:
            print("Pilihan tidak ada")
            input("Tekan apa saja untuk melanjutkan")
            os.system("cls")


main()
