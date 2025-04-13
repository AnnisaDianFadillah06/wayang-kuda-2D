import py5
import numpy as np
from busurPanah import BusurPanah
from gununganWayang import GununganWayang
from awan import Awan
from kandangKuda import KandangKuda
from wayangKuda import WayangKuda

kandang = None

def setup():
    py5.size(py5.display_width - 50, py5.display_height - 50)
    py5.rect_mode(py5.CENTER)
    global kandang
    kandang = KandangKuda(10, 340, 500, 200, 220, 140)
    py5.no_fill()

# Variabel untuk mengatur pergerakan
tx1, tx2= 850, 440 # Translasi awal
speed_x1, speed_x2 = 9, 9  # Kecepatan translasi
busur_panah = BusurPanah()  # Membuat objek busur panah di luar fungsi draw
show_kuda1 = True
door_open = True
background_color = 255
def draw():
    global tx1, tx2, ty, speed_x1, speed_x2, door_open, background_color
    global gunungan_wayang
    py5.background(background_color) 
    
    gunungan_wayang = GununganWayang()
    gunungan_wayang.draw()
    awan = Awan()
        

    
    busur_panah.draw_busur_panah()  # Menggambar busur dan panah
    
    awan.draw_awan()

    kandang.draw()
    
    # Draw kuda 1 if show_kuda1 is True
    if show_kuda1:
        wayang_kuda1 = WayangKuda(scale_factor=0.4)  # Skala lebih kecil
        ty1 = 490  # Gerakan naik turun untuk kuda pertama
        wayang_kuda1.draw(float(tx2), float(ty1 + 440))  # Menggambar kuda pertama

    # Kuda kedua dengan ukuran lebih besar
    wayang_kuda2 = WayangKuda(scale_factor=1)  # Skala lebih besar
    ty2 = 350  # Gerakan naik turun untuk kuda kedua
    wayang_kuda2.draw(float(tx1), float(ty2-200))  # Menggambar kuda kedua dengan translasi x yang berbeda


py5.run_sketch()


