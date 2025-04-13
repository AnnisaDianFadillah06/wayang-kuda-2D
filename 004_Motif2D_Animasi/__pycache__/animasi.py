import py5
import primitif.basic
import numpy as np
from primitif.transformasiv2 import reflect2D, reflect2D2, shear2D, translatePoints, rotate2D, scale2D, translate2D
import primitif.line

class WayangKuda:
    def __init__(self):
        self.ctrl_points = [
            [180, 215], [200, 230], [140, 280], [175, 310],
            [385, 295], [215, 295], [350, 425], [175, 310],
            [385, 295], [365, 205], [265, 275], [280, 265],
            [200, 130], [315, 195], [220, 260], [280, 265],
            [200, 130], [62, 128], [132, 235], [110, 285],
            [165, 250], [150, 255], [175, 340], [110, 285],
            [385, 295], [390, 340], [310, 330], [350, 400],
            [165, 250], [185, 230], [150, 210], [180, 215],
            [385, 295], [410, 290], [435, 345], [370, 370],
            [370, 370], [350, 380], [360, 390], [350, 400],
            [390, 295], [430, 350], [325, 345], [343, 385]
        ]

    def draw(self, tx, ty):
        # Terapkan translasi global ke semua bagian objek
        translated_ctrl_points = translatePoints(np.array(self.ctrl_points, dtype=np.float64), tx, ty)
        
        py5.stroke(0, 0, 255)  # Set warna untuk garis
        # Gambar elemen-elemen wayang kuda
        self._draw_body(tx, ty)
        self._draw_curves(translated_ctrl_points)  # Terapkan translasi yang sama
        self.draw_triangles(-tx, -ty)  # Terapkan translasi yang sama untuk rambut

    def _draw_body(self, tx, ty):
        radius = 7
        # Terapkan translasi pada lingkaran dan persegi panjang
        primitif.basic.lingkaran(152 + tx, 195 + ty, radius, [0, 0, 255, 255])
        primitif.basic.lingkaran(152 + tx, 195 + ty, 9, [0, 0, 255, 255])
        primitif.basic.lingkaran(125 + tx, 210 + ty, 4, [0, 0, 255, 255])
        
        primitif.basic.draw_rotated_rectangle(113 + tx, 187 + ty, 67, 8, 45, (255, 0, 0))
        primitif.basic.draw_rotated_rectangle(110 + tx, 220 + ty, 70, 10, 105, (0, 0, 255))
        primitif.basic.draw_rotated_rectangle(113 + tx, 260 + ty, 47, 7, 25, (0, 0, 255))
        primitif.basic.draw_rotated_rectangle(159 + tx, 300 + ty, 135, 5, 30, (0, 0, 255))
        
        mulut = primitif.basic.segitiga_sama_kaki(138 + tx, 270 + ty, 13, 30)
        xa, ya = mulut[0][0], mulut[0][1]
        rotation_matrix = rotate2D(27, xa, ya)
        rotated_mulut = [rotation_matrix.dot(np.array([point[0], point[1], 1]))[:2] for point in mulut]
        primitif.basic.draw_transformed_triangle(rotated_mulut)

    def _draw_curves(self, translated_ctrl_points):
        bezier_points = [
            (translated_ctrl_points[0], translated_ctrl_points[1], translated_ctrl_points[2], translated_ctrl_points[3]),
            (translated_ctrl_points[4], translated_ctrl_points[5], translated_ctrl_points[6], translated_ctrl_points[7]),
            (translated_ctrl_points[8], translated_ctrl_points[9], translated_ctrl_points[10], translated_ctrl_points[11]),
            (translated_ctrl_points[12], translated_ctrl_points[13], translated_ctrl_points[14], translated_ctrl_points[15]),
            (translated_ctrl_points[16], translated_ctrl_points[17], translated_ctrl_points[18], translated_ctrl_points[19]),
            (translated_ctrl_points[20], translated_ctrl_points[21], translated_ctrl_points[22], translated_ctrl_points[23]),
            (translated_ctrl_points[24], translated_ctrl_points[25], translated_ctrl_points[26], translated_ctrl_points[27]),
            (translated_ctrl_points[28], translated_ctrl_points[29], translated_ctrl_points[30], translated_ctrl_points[31]),
            (translated_ctrl_points[32], translated_ctrl_points[33], translated_ctrl_points[34], translated_ctrl_points[35]),
            (translated_ctrl_points[36], translated_ctrl_points[37], translated_ctrl_points[38], translated_ctrl_points[39]),
            (translated_ctrl_points[40], translated_ctrl_points[41], translated_ctrl_points[42], translated_ctrl_points[43]),
        ]
        for p in bezier_points:
            py5.bezier(*p[0], *p[1], *p[2], *p[3])

    def draw_triangles(self, tx, ty):
        xa, ya = 320, 230  # Translasi diterapkan di seluruh fungsi di akhir
        alas, tinggi = 30, 80
        triangle = primitif.basic.segitiga_sama_kaki(xa, ya, alas, tinggi)
        
        # Terapkan shear sebelum translasi
        shear_matrix = shear2D(0.3, 0)
        triangle_shear = np.dot(triangle, shear_matrix.T)
        
        # Translasi diterapkan terakhir setelah shear
        triangle_translated = translatePoints(triangle_shear, tx, ty)
        self.draw_transformed_triangles(triangle_translated, xa + tx, ya + ty)

    def draw_transformed_triangles(self, triangle_shear, xa, ya):
        total_steps = 15
        angle_step = 160 / total_steps
        
        for i in range(total_steps):
            rotation_matrix = rotate2D(i * angle_step, xa, ya)
            transformed_triangle = np.dot(triangle_shear, rotation_matrix.T)
            
            reflected_triangle = reflect2D2(transformed_triangle, axis='x')
            reflected_triangle_y = reflect2D2(reflected_triangle, axis='y')

            translated_reflected_triangle = translatePoints(reflected_triangle_y, 500, 431)
            primitif.basic.draw_transformed_triangle(translated_reflected_triangle)

class GununganWayang:
    def __init__(self):
        self.ctrl_points = {
            "curve1": [[365, 95], [15, 610], [255, 330], [220, 625]],
            "curve2": [[360, 275], [350, 265], [290, 230], [240, 300]],
            "curve3": [[360, 275], [350, 235], [290, 200], [240, 300]],
            "curve4": [[355, 440], [295, 365], [230, 420], [285, 450]],
            "curve5": [[355, 440], [295, 365], [95, 460], [285, 450]],
            "curve1a": [[245, 315], [225, 360], [295, 380], [260, 410]]
        }
        self.scale_factor_x = 0.5  # Horizontal scaling factor
        self.scale_factor_y = 0.5  # Vertical scaling factor
        self.ref_point = [300, 400]  # Reference point for scaling (can be adjusted)

    def draw_bezier(self, points, color):
        py5.stroke(*color)
        py5.bezier(points[0][0], points[0][1], 
                   points[1][0], points[1][1], 
                   points[2][0], points[2][1], 
                   points[3][0], points[3][1])
    
    def draw_reflected_bezier(self, points, axis='y', translate_x=665, color=(255, 0, 0)):
        reflected_points = [reflect2D(pt, axis=axis) for pt in points]
        translated_points = translatePoints(np.array(reflected_points), translate_x, 0)
        self.draw_bezier(translated_points, color)

    def apply_scaling(self, points):
        # Apply scaling to control points
        scaled_points = []
        for pt in points:
            scaled_pt = scale2D(self.scale_factor_x, self.scale_factor_y, self.ref_point[0], self.ref_point[1], np.array([[pt[0]], [pt[1]], [1]]))
            scaled_points.append([scaled_pt[0][0], scaled_pt[1][0]])
        return scaled_points

    def draw_roof_and_house(self, tx=100, ty=50):  # Adjust translation values as needed
        # Create the translation matrix
        translation_matrix = translate2D(tx, ty)

        # Draw the trapeziums for the roof
        py5.no_fill()
        py5.stroke(0)  # Set stroke color

        # Apply translation to the trapeziums for the roof (scaled down by half)
        roof_top_left = np.dot(translation_matrix, np.array([185, 240, 1]))
        roof_top_right = np.dot(translation_matrix, np.array([185, 240, 1]))
        roof_bottom_left = np.dot(translation_matrix, np.array([185, 250, 1]))
        roof_bottom_right = np.dot(translation_matrix, np.array([185, 250, 1]))

        primitif.basic.trapesium_siku(roof_top_left[0], roof_top_left[1], 20, 30, 10, reflect=False, tx=0)
        primitif.basic.trapesium_siku(roof_top_right[0], roof_top_right[1], 20, 30, 10, reflect=True, tx=570)
        primitif.basic.trapesium_siku(roof_bottom_left[0], roof_bottom_left[1], 45, 60, 15, reflect=False, tx=0)
        primitif.basic.trapesium_siku(roof_bottom_right[0], roof_bottom_right[1], 45, 60, 15, reflect=True, tx=570)

        # Draw the house base and door (scaled down by half)
        house_base = np.dot(translation_matrix, np.array([145, 265, 1]))
        primitif.basic.persegi_panjang(house_base[0], house_base[1], 80, 50)

        # Apply translation to door shapes
        door_top = np.dot(translation_matrix, np.array([152.5, 202.5, 1]))  # Apply translation to the door top
        door_bottom_ref = np.dot(translation_matrix, np.array([152.5, 250, 1]))  # Apply translation to the door reference point

        primitif.basic.trapesium_siku(door_top[0], door_top[1], 30, 45, 15, reflect=True, tx=570, rotate_angle=90, refx=door_top[0], refy=door_bottom_ref[1])  # Using door_bottom_ref[1] as refy
        door_bottom = np.dot(translation_matrix, np.array([-62.5, 265, 1]))  # Apply translation to door bottom
        primitif.basic.trapesium_siku(door_bottom[0], door_bottom[1], 30, 45, 15, reflect=False, tx=150, rotate_angle=-90, refx=door_top[0], refy=door_bottom_ref[1])  # Use door_bottom_ref[1] as refy


    def draw(self):
        py5.no_fill()
        py5.background(255)

        # Draw each curve and its reflection with scaling applied
        for key, points in self.ctrl_points.items():
            scaled_points = self.apply_scaling(points)
            if key == "curve1a":
                self.draw_bezier(scaled_points, (0, 0, 255))
                self.draw_reflected_bezier(scaled_points, color=(255, 0, 0))
            else:
                self.draw_bezier(scaled_points, (0, 0, 255))
                self.draw_reflected_bezier(scaled_points, color=(255, 0, 0))
        
        # Draw the roof and house
        self.draw_roof_and_house(tx=100, ty=50)  # Adjust these values as needed
        
        # Additional specific curves (colors and styles can be adjusted)
        scaled_curve2 = self.apply_scaling(self.ctrl_points["curve2"])
        self.draw_bezier(scaled_curve2, (0, 255, 0))
        self.draw_reflected_bezier(scaled_curve2, color=(255, 165, 0))
        
        scaled_curve3 = self.apply_scaling(self.ctrl_points["curve3"])
        self.draw_bezier(scaled_curve3, (0, 0, 255))
        self.draw_reflected_bezier(scaled_curve3, color=(128, 0, 128))
        
        scaled_curve4 = self.apply_scaling(self.ctrl_points["curve4"])
        self.draw_bezier(scaled_curve4, (255, 20, 147))
        self.draw_reflected_bezier(scaled_curve4, color=(255, 140, 0))
        
        scaled_curve5 = self.apply_scaling(self.ctrl_points["curve5"])
        self.draw_bezier(scaled_curve5, (0, 100, 0))
        self.draw_reflected_bezier(scaled_curve5, color=(100, 100, 100))

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

class BusurPanah:
    def __init__(self):
        # Koordinat awal, panjang alas, dan tinggi segitiga
        self.xa, self.ya = 300, 200  # Koordinat sudut lancip segitiga
        self.alas, self.tinggi = 30, 50  # Alas dan tinggi segitiga sama kaki

    def draw_busur_panah(self):
        # Buat segitiga sama kaki
        segitiga_points = primitif.basic.segitiga_sama_kaki(self.xa, self.ya, self.alas, self.tinggi)

        # Warna hitam untuk segitiga
        color = [0, 0, 0, 255]

        # Gambar segitiga
        primitif.basic.draw_transformed_triangle(segitiga_points, color)

        # Gambar persegi panjang berotasi
        primitif.basic.draw_rotated_rectangle(233, 316, 135, 5, 90, (0, 0, 255))

        # Gambar trapesium siku terpantul dan terotasi
        primitif.basic.trapesium_siku(305, 500, 35, 50, 12, reflect=True, tx=760, rotate_angle=-90, refx=305, refy=500)
        primitif.basic.trapesium_siku(-30, 510, 35, 50, 12, reflect=False, tx=185, rotate_angle=90, refx=305, refy=500)

def setup():
    py5.size(py5.display_width - 50, py5.display_height - 50)
    py5.rect_mode(py5.CENTER)
    py5.no_fill()

# Variabel untuk mengatur pergerakan
tx, ty = 0, 0  # Translasi awal
speed_x = 2  # Kecepatan translasi

def draw():
    py5.background(255)  # Set background to white
    
    gunungan_wayang = GununganWayang()
    gunungan_wayang.draw()
    
    awan = Awan()  # Membuat objek awan
    awan.draw_awan()  # Menggambar awan
    
    busur_panah = BusurPanah()  # Membuat objek busur panah
    busur_panah.draw_busur_panah()  # Menggambar busur dan panah
    global tx, ty, speed_x
    
    wayang_kuda = WayangKuda()  # Membuat objek WayangKuda
    
    # Gerakan maju mundur dengan sedikit naik turun
    ty = 10 * np.sin(py5.frame_count * 0.1)  # Gerakan naik turun diagonal
    
    # Terapkan translasi pada objek
    wayang_kuda.draw(float(tx), float(ty))  # Menggambar Wayang Kuda dengan translasi
    
    # Update posisi translasi
    tx += speed_x
    
    # Membalik arah gerakan jika mencapai tepi layar
    if tx > py5.width - 100 or tx < 0:
        speed_x = -speed_x


py5.run_sketch()

