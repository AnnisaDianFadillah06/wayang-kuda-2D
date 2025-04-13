import py5
import primitif.basic

class BusurPanah:
    def __init__(self):
        # Koordinat awal, panjang alas, dan tinggi segitiga
        self.xa, self.ya = 100, 5  # Koordinat sudut lancip segitiga
        self.alas, self.tinggi = 30, 50  # Alas dan tinggi segitiga sama kaki
        self.speed = 3  # Kecepatan gerakan
        self.direction = 1  # 1 untuk bergerak ke bawah, -1 untuk ke atas

    def draw_busur_panah(self):
        # Buat segitiga sama kaki
        segitiga_points = primitif.basic.segitiga_sama_kaki(self.xa, self.ya + 200, self.alas, self.tinggi)

        # Warna hitam untuk segitiga
        color = [255,0,0,255]

        # Gambar segitiga
        primitif.basic.draw_transformed_triangle(segitiga_points, color)

        # Gambar persegi panjang berotasi
        primitif.basic.draw_rotated_rectangle(33, 316 + self.ya, 135, 5, 90, (0, 0, 255))

        # Gambar trapesium siku terpantul dan terotasi
        primitif.basic.trapesium_siku(105, 500 + self.ya, 35, 50, 12, reflect=True, tx=360, rotate_angle=-90, refx=105, refy=500 + self.ya)
        primitif.basic.trapesium_siku(-230, 510 + self.ya, 35, 50, 12, reflect=False, tx=185, rotate_angle=90, refx=105, refy=500 + self.ya)

    def update_position(self):
        # Update posisi vertikal
        self.ya += self.speed * self.direction
        
        # Ubah arah jika mencapai batas atas atau bawah
        if self.ya > -10:  # Ubah nilai ini untuk batas bawah
            self.direction = -1  # Bergerak ke atas
        elif self.ya < 40:  # Ubah nilai ini untuk batas atas
            self.direction = 1  # Bergerak ke bawah