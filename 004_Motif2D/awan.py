import py5
import numpy as np
import math

class Awan:
    def __init__(self):
        # Simpan salah satu set titik kontrol
        self.ctrl_point1 = [315, 110]  # Disimpan di variabel
        self.ctrl_point2 = [280, 75]
        self.ctrl_point3 = [275, 115]
        self.ctrl_point4 = [245, 75]

    def draw_awan(self):
        # Menggambar beberapa kurva Bézier yang membentuk awan
        py5.stroke(0, 0, 255)  # Warna biru untuk Bézier
        py5.no_fill()
        
        # Kurva Bézier pertama
        py5.bezier(self.ctrl_point1[0], self.ctrl_point1[1], self.ctrl_point2[0], self.ctrl_point2[1],
                   self.ctrl_point3[0], self.ctrl_point3[1], self.ctrl_point4[0], self.ctrl_point4[1])

        # Kurva Bézier lainnya langsung dimasukkan tanpa disimpan di variabel
        py5.bezier(165, 55, 200, 80, 225, 60, 245, 75)
        py5.bezier(165, 55, 100, 80, 165, 95, 185, 85)
        py5.bezier(245, 105, 210, 105, 205, 85, 185, 85)
        py5.bezier(245, 105, 295, 145, 250, 105, 235, 145)
        py5.bezier(130, 135, 165, 125, 180, 185, 235, 145)
        py5.bezier(130, 135, 145, 90, 160, 130, 185, 105)
        py5.bezier(185, 120, 175, 160, 240, 115, 185, 105)
        py5.bezier(130, 135, 165, 125, 180, 185, 235, 145)
        py5.bezier(315, 110, 295, 105, 285, 155, 245, 160)
        py5.bezier(130, 150, 170, 150, 165, 215, 245, 160)
        py5.bezier(130, 150, 100, 170, 110, 125, 60, 140)
        py5.bezier(140, 80, 80, 150, 85, 80, 60, 140)
