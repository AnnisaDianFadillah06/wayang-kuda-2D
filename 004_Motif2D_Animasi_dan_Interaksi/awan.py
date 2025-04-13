import py5
import numpy as np
import math

class Awan:
    def __init__(self, initial_position, direction, is_top):
        self.position = initial_position  # Posisi awal awan
        self.direction = direction  # Arah gerakan zig-zag
        self.is_top = is_top  # Menandakan apakah awan berada di atas atau bawah
        self.scale_factor = 1.0  # Faktor skala untuk awan
        self.scale_direction = 1  # Arah skala (1 untuk membesar, -1 untuk mengecil)

        # Titik kontrol awan
        self.ctrl_point1 = [315, 110]
        self.ctrl_point2 = [280, 75]
        self.ctrl_point3 = [275, 115]
        self.ctrl_point4 = [245, 75]

    def draw_awan(self):
        py5.stroke(0, 0, 255)  # Warna biru untuk Bézier
        
        # Menggambar awan menggunakan titik kontrol dengan skala
        scale_matrix = np.array([[self.scale_factor, 0], [0, self.scale_factor]])
        
        # Titik kontrol untuk menggambar awan
        control_points = np.array([
            [315, 110], [280, 75], [275, 115], [245, 75],
            [165, 55], [200, 80], [225, 60], [245, 75],
            [165, 55], [100, 80], [165, 95], [185, 85],
            [245, 105], [210, 105], [205, 85], [185, 85],
            [245, 105], [295, 145], [250, 105], [235, 145],
            [130, 135], [165, 125], [180, 185], [235, 145],
            [130, 135], [145, 90], [160, 130], [185, 105],
            [185, 120], [175, 160], [240, 115], [185, 105],
            [130, 135], [165, 125], [180, 185], [235, 145],
            [315, 110], [295, 105], [285, 155], [245, 160],
            [130, 150], [170, 150], [165, 215], [245, 160],
            [130, 150], [100, 170], [110, 125], [60, 140],
            [140, 80], [80, 150], [85, 80], [60, 140]
        ])

        # Terapkan skala ke titik kontrol
        scaled_points = np.dot(control_points, scale_matrix.T)

        # Menggambar awan menggunakan titik kontrol yang telah diskalakan
        for i in range(0, len(scaled_points), 4):
            py5.bezier(scaled_points[i][0] + self.position[0], scaled_points[i][1] + self.position[1],
                       scaled_points[i + 1][0] + self.position[0], scaled_points[i + 1][1] + self.position[1],
                       scaled_points[i + 2][0] + self.position[0], scaled_points[i + 2][1] + self.position[1],
                       scaled_points[i + 3][0] + self.position[0], scaled_points[i + 3][1] + self.position[1])

    def update(self):
        # Memperbarui posisi awan
        self.position[0] += 2 * self.direction  # Menggeser awan secara horizontal
        vertical_movement = math.sin(py5.frame_count / 10) * 0.5

        # Jika awan berada di atas, gerak ke atas, sebaliknya ke bawah
        if self.is_top:
            self.position[1] += vertical_movement
        else:
            self.position[1] -= vertical_movement

        # Ubah arah jika mencapai batas
        if self.position[0] > py5.width//2 + 350 or self.position[0] < -50:
            self.direction *= -1  # Ubah arah

        # Mengubah skala
        if self.scale_factor >= 0.7:  # Maksimum ukuran
            self.scale_direction = -1
        elif self.scale_factor <= 0.5:  # Minimum ukuran
            self.scale_direction = 1

        self.scale_factor += 0.01 * self.scale_direction  # Update faktor skala