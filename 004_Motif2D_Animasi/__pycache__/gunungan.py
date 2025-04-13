import py5
import numpy as np
from primitif.transformasiv2 import translate2D, scale2D, rotate2D, transformPoints2D, reflect2D

# Inisialisasi titik kontrol untuk Bézier pertama
ctrl_point1 = [365, 95]
ctrl_point2 = [15, 610]
ctrl_point3 = [255, 330]
ctrl_point4 = [220, 625]


def setup():
    py5.size(800, 800)
    py5.no_fill()

def draw():
    py5.background(255)  # Set background to white
    
    # Gambarkan kurva Bézier pertama
    py5.stroke(0, 0, 255)  # Warna biru untuk Bézier pertama
    py5.bezier(ctrl_point1[0], ctrl_point1[1], ctrl_point2[0], ctrl_point2[1], 
               ctrl_point3[0], ctrl_point3[1], ctrl_point4[0], ctrl_point4[1])
    
    # Refleksi keempat titik kontrol terhadap sumbu Y
    reflected_point1 = reflect2D(ctrl_point1, axis='y')
    reflected_point2 = reflect2D(ctrl_point2, axis='y')
    reflected_point3 = reflect2D(ctrl_point3, axis='y')
    reflected_point4 = reflect2D(ctrl_point4, axis='y')
    
    # Gambarkan kurva Bézier kedua yang merupakan refleksi
    py5.stroke(255, 0, 0)  # Warna merah untuk Bézier kedua (refleksi)
    py5.bezier(reflected_point1[0], reflected_point1[1], reflected_point2[0], reflected_point2[1], 
               reflected_point3[0], reflected_point3[1], reflected_point4[0], reflected_point4[1])

    # Gambarkan titik kontrol dari kedua kurva
    py5.stroke(0)
    py5.ellipse(ctrl_point1[0], ctrl_point1[1], 10, 10)
    py5.ellipse(ctrl_point2[0], ctrl_point2[1], 10, 10)
    py5.ellipse(ctrl_point3[0], ctrl_point3[1], 10, 10)
    py5.ellipse(ctrl_point4[0], ctrl_point4[1], 10, 10)
    
    py5.ellipse(reflected_point1[0], reflected_point1[1], 10, 10)
    py5.ellipse(reflected_point2[0], reflected_point2[1], 10, 10)
    py5.ellipse(reflected_point3[0], reflected_point3[1], 10, 10)
    py5.ellipse(reflected_point4[0], reflected_point4[1], 10, 10)

py5.run_sketch()
