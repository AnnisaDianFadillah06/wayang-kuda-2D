import py5
import primitif.basic
import numpy as np
from primitif.transformasiv2 import reflect2D, translatePoints, scale2D, translate2D

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
        self.ref_point = [900, 400]  # Reference point for scaling (can be adjusted)

    def draw_bezier(self, points, color):
        py5.stroke(*color)
        py5.bezier(points[0][0], points[0][1], 
                   points[1][0], points[1][1], 
                   points[2][0], points[2][1], 
                   points[3][0], points[3][1])
    
    def draw_reflected_bezier(self, points, axis='y', translate_x=1265, color=(0, 0, 255, 255)):
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
        primitif.basic.trapesium_siku(roof_top_right[0], roof_top_right[1], 20, 30, 10, reflect=True, tx=1270)
        primitif.basic.trapesium_siku(roof_bottom_left[0], roof_bottom_left[1], 45, 60, 15, reflect=False, tx=0)
        primitif.basic.trapesium_siku(roof_bottom_right[0], roof_bottom_right[1], 45, 60, 15, reflect=True, tx=1270)

        # Draw the house base and door (scaled down by half)
        house_base = np.dot(translation_matrix, np.array([145, 265, 1]))
        primitif.basic.persegi_panjang(house_base[0], house_base[1], 80, 50)

        # Apply translation to door shapes
        door_top = np.dot(translation_matrix, np.array([152.5, 202.5, 1]))  # Apply translation to the door top
        door_bottom_ref = np.dot(translation_matrix, np.array([152.5, 250, 1]))  # Apply translation to the door reference point

        primitif.basic.trapesium_siku(door_top[0], door_top[1], 30, 45, 15, reflect=True, tx=1270, rotate_angle=90, refx=door_top[0], refy=door_bottom_ref[1])  # Using door_bottom_ref[1] as refy
        door_bottom = np.dot(translation_matrix, np.array([-62.5, 265, 1]))  # Apply translation to door bottom
        primitif.basic.trapesium_siku(door_bottom[0], door_bottom[1], 30, 45, 15, reflect=False, tx=150, rotate_angle=-90, refx=door_top[0], refy=door_bottom_ref[1])  # Use door_bottom_ref[1] as refy

    def draw_bottom_lace(self):
        # Menggambar ellips di bagian bawah objek untuk efek renda
        py5.stroke(0)

        # Tentukan koordinat awal dan jumlah ellips
        start_x = 580  # Koordinat X awal (sesuaikan dengan objek Anda)
        end_x = 700    # Koordinat X akhir (sesuaikan dengan objek Anda)
        y_position = 515  # Koordinat Y posisi ellips (sesuaikan dengan objek Anda)
        ellipse_width = 30  # Lebar ellips
        ellipse_height = 6  # Tinggi ellips
        spacing = 15  # Jarak antara ellips

        for x in range(start_x, end_x, spacing):
            primitif.basic.ellips(x, y_position, ellipse_width, ellipse_height, c=[255,0,0,255])

    def draw_handle(self, xa, ya, panjang, lebar):
        # Draw the handle for the Gunungan
        primitif.basic.persegi_panjang(xa, ya, panjang, lebar, c=[0, 0, 255, 255])
        
        # Add decorative flower ornaments inside the handle
        # Looping flowers vertically to fill the handle area
        flower_spacing = 20  # Adjust spacing between flowers
        for i in range(ya + 20, ya + lebar - 20, flower_spacing):
            self.draw_flower(xa + panjang // 2, i, scale=0.5)

    def draw_flower(self, xc, yc, scale=1.0):
        # Draw a flower with 4 petals and a central circle
        py5.stroke(0)
        for angle in range(0, 360, 90):  # 4 petals, 90 degrees apart
            px = xc + np.cos(np.radians(angle)) * 10 * scale
            py = yc + np.sin(np.radians(angle)) * 10 * scale
            primitif.basic.ellips(px, py, 10 * scale, 4 * scale)  # Larger petals for better shape
        
        # Draw the central circle of the flower
        primitif.basic.lingkaran(xc, yc, 3 * scale, c=[255,0,0,255])

    def draw(self):
        py5.no_fill()

        # Draw each curve and its reflection with scaling applied
        for key, points in self.ctrl_points.items():
            scaled_points = self.apply_scaling(points)
            if key == "curve1a":
                self.draw_bezier(scaled_points, (0, 0, 255, 255))
                self.draw_reflected_bezier(scaled_points, color=(255, 0, 0))
            else:
                self.draw_bezier(scaled_points, (0, 0, 255, 255))
                self.draw_reflected_bezier(scaled_points, color=(255, 0, 0))
        
        # Draw the roof and house
        self.draw_roof_and_house(tx=450, ty=190)

        # Draw the bottom lace
        self.draw_bottom_lace()

        # Draw the handle below the gunungan
        self.draw_handle(623, 520, 20, 200)  # Adjust the position and size as needed

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