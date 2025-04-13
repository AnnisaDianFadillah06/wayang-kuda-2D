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
show_kuda1 = False
door_open = False
background_color = 255
def draw():
    global tx1, tx2, ty, speed_x1, speed_x2, door_open, background_color
    global gunungan_wayang
    py5.background(background_color) 
    
    gunungan_wayang = GununganWayang()
    gunungan_wayang.draw()
        

    busur_panah.update_position()  # Update posisi busur panah
    busur_panah.draw_busur_panah()  # Menggambar busur dan panah
    
    
    # Update dan gambarkan awan atas
    for awan in awan_atas + awan_bawah:
        awan.update()
        awan.draw_awan()

    kandang.draw()
    # Draw kuda 1 if show_kuda1 is True
    if show_kuda1:
        wayang_kuda1 = WayangKuda(scale_factor=0.4)  # Skala lebih kecil
        ty1 = 10 * np.sin(py5.frame_count * 0.1) + 490  # Gerakan naik turun untuk kuda pertama
        wayang_kuda1.draw(float(tx2), float(ty1 + 440))  # Menggambar kuda pertama

    # Kuda kedua dengan ukuran lebih besar
    wayang_kuda2 = WayangKuda(scale_factor=1)  # Skala lebih besar
    ty2 = 10 * np.sin(py5.frame_count * 0.1) + 350  # Gerakan naik turun untuk kuda kedua
    wayang_kuda2.draw(float(tx1), float(ty2-200))  # Menggambar kuda kedua dengan translasi x yang berbeda

    # Update translasi untuk kuda pertama (dengan batas pergerakan penuh)
    tx1 += speed_x1
    if tx1 > 860 or tx1 < 630:
        speed_x1 = -speed_x1

    # Update translasi untuk kuda kedua (dengan batas pergerakan lebih kecil)
    tx2 += speed_x2
    if tx2 > py5.width // 2 - 200 or tx2 < 320:  # Batas pergerakan lebih kecil
        speed_x2 = -speed_x2

# Membuat daftar awan
awan_atas = [
    Awan(initial_position=[260, -40], direction=-1, is_top=True),
    Awan(initial_position=[460, -40], direction=1, is_top=True),
]

awan_bawah = [
    Awan(initial_position=[150, 80], direction=-1, is_top=False),
    Awan(initial_position=[350, 80], direction=1, is_top=False),
]
def key_pressed():
    global door_open, show_kuda1, background_color, speed_x1, speed_x2
    if py5.key == '1':
        if door_open:
            # If the door is open, reset the door and hide the horse
            kandang.reset_pintu()  # Mengembalikan pintu ke posisi semula
            door_open = False  # Set the state to closed
            show_kuda1 = False
        else:
            # If the door is closed, move the door and show the horse
            kandang.geser_pintu(110)  # Menggeser pintu
            door_open = True  # Set the state to open
            show_kuda1 = True
            
    elif py5.key == '3':
        # Meningkatkan kecepatan animasi
        speed_x1 *= 1.511
        speed_x2 *= 1.5
        
    elif py5.key == '4':
        # Mengurangi kecepatan animasi
        speed_x1 *= 0.5
        speed_x2 *= 0.5

    elif py5.key == '2':
        # Mengurangi kecepatan animasi
        if background_color == 255:
            background_color = 0  # Ubah ke hitam
        else:
            background_color = 255  # Ubah ke putih
py5.run_sketch()


