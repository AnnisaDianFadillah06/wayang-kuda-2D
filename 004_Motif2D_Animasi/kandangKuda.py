import py5
import primitif.basic
import primitif.line

class KandangKuda:
    def __init__(self, x, y, lebar, tinggi, pintu_lebar, pintu_tinggi):
        self.x = x
        self.y = y
        self.lebar = lebar
        self.tinggi = tinggi
        self.pintu_lebar = pintu_lebar
        self.pintu_tinggi = pintu_tinggi
        self.pintu_x1 = self.x + (self.lebar - self.pintu_lebar) // 2
        self.pintu_x2 = self.pintu_x1 + (self.pintu_lebar // 2)
        self.pintu_y = self.y + self.tinggi - self.pintu_tinggi
        self.offset = False  # Track if the doors are open
        
    def draw(self):        
        # Gambar kandang
        self.gambar_kandang()
        
        # Gambar pintu
        self.gambar_pintu()
        
        # Gambar tiang pintu
        self.gambar_tiang_pintu()

        # Gambar atap
        self.gambar_atap()

        # Gambar jendela
        self.gambar_jendela()

    def gambar_kandang(self):
        # Menggambar kandang sebagai persegi panjang menggunakan primitif.basic.persegi_panjang
        primitif.basic.persegi_panjang(self.x, self.y, self.lebar, self.tinggi)
    
    def gambar_atap(self):
        # Menggambar atap sebagai segitiga sama kaki
        atap_xa = self.x + 250 + (self.lebar - self.lebar)  # Center the apex on the x-axis of the rectangle
        atap_ya = self.y - (self.tinggi * 0.5)  # Move the roof above the rectangle
        alas = self.lebar
        tinggi = self.tinggi * 0.5
        segitiga = primitif.basic.segitiga_sama_kaki(atap_xa, atap_ya, alas, tinggi)
        primitif.basic.draw_transformed_triangle(segitiga)

    def gambar_jendela(self):
        # Menggambar jendela
        jendela_x = self.x + (self.lebar - self.pintu_lebar) // 1.3
        jendela_y = self.y - (self.tinggi * 0.6) + (self.pintu_tinggi * 0.3)  # Center the window on the roof
        jendela_size = self.pintu_lebar // 4
        
        # Gambar jendela
        primitif.basic.persegi(jendela_x, jendela_y, jendela_size)
        
        # Gambar kotak-kotak di dalam jendela
        for i in range(2):
            for j in range(2):
                kotak_x = jendela_x + 6 + (j * jendela_size // 2)
                kotak_y = jendela_y + 6 + (i * jendela_size // 2)
                primitif.basic.persegi(kotak_x, kotak_y, jendela_size // 4)

    def gambar_tiang_pintu(self):
        # Menggambar dua pintu berdempetan
        primitif.basic.persegi_panjang(self.pintu_x1, self.pintu_y, self.pintu_lebar, self.pintu_tinggi)

    def gambar_pintu(self):
        # Pintu kiri (bergerak ke kiri)
        pintu_x1_shifted = self.pintu_x1 - self.offset
        primitif.basic.persegi_panjang(pintu_x1_shifted, self.pintu_y, self.pintu_lebar // 2, self.pintu_tinggi)

        # Garis menyilang pada pintu kiri
        self.gambar_garis_menyilang(pintu_x1_shifted, self.pintu_x1 - self.offset)

        # Pintu kanan (bergerak ke kanan)
        pintu_x2_shifted = self.pintu_x2 + self.offset
        primitif.basic.persegi_panjang(pintu_x2_shifted, self.pintu_y, self.pintu_lebar // 2, self.pintu_tinggi)

        # Garis menyilang pada pintu kanan
        self.gambar_garis_menyilang(pintu_x2_shifted, self.pintu_x2 + self.offset)

    def gambar_garis_menyilang(self, pintu_x, original_x):
        # Garis menyilang dari kanan atas pintu kiri ke kiri bawah pintu kanan
        garis1 = primitif.line.line_bresenham(pintu_x + self.pintu_lebar // 2, self.pintu_y,
                                               original_x, self.pintu_y + self.pintu_tinggi)
        for x, y in garis1:
            py5.point(x, y)

        # Garis menyilang dari kanan bawah pintu kiri ke kiri atas pintu kanan
        garis2 = primitif.line.line_bresenham(pintu_x + self.pintu_lebar // 2, self.pintu_y + self.pintu_tinggi,
                                               original_x, self.pintu_y)
        for x, y in garis2:
            py5.point(x, y)

    def geser_pintu(self, amount):
        # Pergeseran pintu ke kiri dan kanan secara bersamaan
        self.offset += amount

    def reset_pintu(self):
        # Mengembalikan pintu ke posisi semula
        self.offset = 0