import py5
import primitif.basic
import numpy as np
from primitif.transformasiv2 import reflect2D2, shear2D, translatePoints, rotate2D, scale2D

class WayangKuda:
    def __init__(self, scale_factor=1.0):
        # Menambahkan scale_factor untuk mengatur ukuran
        self.scale_factor = scale_factor
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
        # Terapkan translasi dan skala ke semua bagian objek
        translated_ctrl_points = translatePoints(np.array(self.ctrl_points, dtype=np.float64), tx, ty)
        scaled_ctrl_points = translated_ctrl_points * self.scale_factor
        
        py5.stroke(0, 0, 255, 255)  # Set warna untuk garis
        self._draw_body(tx, ty)
        self._draw_curves(scaled_ctrl_points)  # Terapkan translasi dan skala
        self.draw_triangles(-tx, -ty, self.scale_factor)  # Terapkan translasi yang sama untuk rambut

    def _draw_body(self, tx, ty):
        radius = 7 * self.scale_factor
        primitif.basic.lingkaran((152 + tx) * self.scale_factor, (195 + ty) * self.scale_factor, radius, [0, 0, 255, 255])
        primitif.basic.lingkaran((152 + tx) * self.scale_factor, (195 + ty) * self.scale_factor, 9 * self.scale_factor, [0, 0, 255, 255])
        primitif.basic.lingkaran((125 + tx) * self.scale_factor, (210 + ty) * self.scale_factor, 4 * self.scale_factor, [0, 0, 255, 255])
        
        primitif.basic.draw_rotated_rectangle((113 + tx) * self.scale_factor, (187 + ty) * self.scale_factor, 67 * self.scale_factor, 8 * self.scale_factor, 45, (255, 0, 0))
        primitif.basic.draw_rotated_rectangle((110 + tx) * self.scale_factor, (220 + ty) * self.scale_factor, 70 * self.scale_factor, 10 * self.scale_factor, 105, (0, 0, 255))
        primitif.basic.draw_rotated_rectangle((113 + tx) * self.scale_factor, (260 + ty) * self.scale_factor, 47 * self.scale_factor, 7 * self.scale_factor, 25, (0, 0, 255))
        primitif.basic.draw_rotated_rectangle((159 + tx) * self.scale_factor, (300 + ty) * self.scale_factor, 135 * self.scale_factor, 5 * self.scale_factor, 30, (0, 0, 255))
        
        mulut = primitif.basic.segitiga_sama_kaki((138 + tx) * self.scale_factor, (270 + ty) * self.scale_factor, 13 * self.scale_factor, 30 * self.scale_factor)
        xa, ya = mulut[0][0], mulut[0][1]
        rotation_matrix = rotate2D(27, xa, ya)
        rotated_mulut = [rotation_matrix.dot(np.array([point[0], point[1], 1]))[:2] for point in mulut]
        primitif.basic.draw_transformed_triangle(rotated_mulut)

    def _draw_curves(self, translated_ctrl_points):
        py5.stroke(0, 0, 255, 255)  # Set warna untuk garis
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

    def draw_triangles(self, tx, ty, scale_factor=1):
        xa, ya = 320 * scale_factor, 230 * scale_factor  # Pusat translasi rambut terpengaruh skala
        alas = 30 * scale_factor  # Sesuaikan alas dengan skala
        tinggi = 80 * scale_factor  # Sesuaikan tinggi dengan skala
        triangle = primitif.basic.segitiga_sama_kaki(xa, ya, alas, tinggi)

        # Terapkan shear sebelum translasi
        shear_matrix = shear2D(0.3, 0)  # Sesuaikan shear jika diperlukan
        triangle_shear = np.dot(triangle, shear_matrix.T) 

        # Translasi diterapkan setelah shear dengan skala
        triangle_translated = translatePoints(triangle_shear, tx * scale_factor, ty * scale_factor) 
        
        # Gambar segitiga yang merepresentasikan rambut
        self.draw_transformed_triangles(triangle_translated, xa + tx * scale_factor, ya + ty * scale_factor, scale_factor)


    def draw_transformed_triangles(self, triangle_shear, xa, ya, scale_factor=1):
        total_steps = 15
        # Sudut rotasi disesuaikan dengan scale factor
        angle_step = (160 / total_steps)  # Tanpa skala
        
        for i in range(total_steps):
            # Terapkan rotasi yang disesuaikan dengan skala
            rotation_matrix = rotate2D(i * angle_step, xa, ya) 
            transformed_triangle = np.dot(triangle_shear, rotation_matrix.T)
            
            # Refleksi segitiga untuk membuat pola rambut yang lebih kompleks
            reflected_triangle = reflect2D2(transformed_triangle, axis='x')
            reflected_triangle_y = reflect2D2(reflected_triangle, axis='y')

            # Translasi dan gambar segitiga yang sudah diubah
            translated_reflected_triangle = translatePoints(reflected_triangle_y, 500 * scale_factor, 431 * scale_factor)  # Tanpa skala
            primitif.basic.draw_transformed_triangle(translated_reflected_triangle)  # Menggambar tanpa skala