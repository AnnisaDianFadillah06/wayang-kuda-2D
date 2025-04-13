import primitif.line
import py5
import numpy as np
from primitif.transformasiv2 import reflect2D2, translatePoints, rotate2D, shear2D, reflect2D

def round(x):
    return int(x+0.5)

def draw_margin(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(margin,margin,width-margin,margin))
    py5.points(primitif.line.line_dda(margin,height-margin,width-margin,height-margin))
    py5.points(primitif.line.line_bresenham(margin,margin,margin,height-margin))
    py5.points(primitif.line.line_bresenham(width-margin,margin,width-margin,height-margin))

def draw_grid(width, height, margin, c=[0,0,0,255]):
    # Sumbu Y
    xa = margin;
    ya = 2*margin;
    xb = width - xa
    yb = height - ya
    y_range = (height / margin)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    for count in range(1, int(y_range)):
        py5.points(primitif.line.line_dda(xa,ya,xb,ya))
        ya = ya + margin

    # Sumbu X
    xa = 2*margin
    ya = margin
    xb = width - xa
    yb = height - ya
    x_range = (width / margin)
    for count in range(1, int(x_range)):
        py5.points(primitif.line.line_dda(xa,ya,xa,yb))
        xa = xa + margin

def draw_kartesian(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(width/2,margin,width/2,height-margin))
    py5.points(primitif.line.line_bresenham(margin,height/2,width-margin,height/2))
    
def persegi(xa, ya, panjang, c=[0, 0, 255, 255]):
    py5.stroke(*c)
    points = []
    points.extend(primitif.line.line_bresenham(xa, ya, xa + panjang, ya))  # Sisi atas
    points.extend(primitif.line.line_bresenham(xa + panjang, ya, xa + panjang, ya + panjang))  # Sisi kanan
    points.extend(primitif.line.line_bresenham(xa + panjang, ya + panjang, xa, ya + panjang))  # Sisi bawah
    points.extend(primitif.line.line_bresenham(xa, ya + panjang, xa, ya))  # Sisi kiri
    for x, y in points:
        py5.point(x, y)
        
def persegi_panjang(xa, ya, panjang, lebar, c=[0, 0, 255, 255]):
    py5.stroke(*c)
    points = []
    points.extend(primitif.line.line_bresenham(xa, ya, xa + panjang, ya))  # Sisi atas
    points.extend(primitif.line.line_bresenham(xa + panjang, ya, xa + panjang, ya + lebar))  # Sisi kanan
    points.extend(primitif.line.line_bresenham(xa + panjang, ya + lebar, xa, ya + lebar))  # Sisi bawah
    points.extend(primitif.line.line_bresenham(xa, ya + lebar, xa, ya))  # Sisi kiri
    for x, y in points:
        py5.point(x, y)

# Fungsi untuk menghitung dan merotasi persegi panjang
def draw_rotated_rectangle(x, y, width, height, angle, color):
    # Hitung sudut-sudut dari persegi panjang
    points = np.array([[x, y], [x + width, y], [x + width, y + height], [x, y + height]]).T

    # Rotasi setiap titik
    rotated_points = []
    for point in points.T:
        rotated_point = rotate2D(angle, x + width / 2, y + height / 2).dot(np.array([point[0], point[1], 1]))  # Rotasi terhadap pusat persegi panjang
        rotated_points.append(rotated_point[:2])  # Ambil x dan y dari hasil rotasi

    # Gambar persegi panjang yang sudah dirotasi dengan algoritma Bresenham
    py5.stroke(*color)  # Warna untuk persegi panjang yang sudah dirotasi
    all_points = []
    for i in range(len(rotated_points)):
        next_index = (i + 1) % len(rotated_points)  # Menghubungkan titik terakhir ke pertama
        # Gambar garis dengan Bresenham antara dua titik
        all_points.extend(primitif.line.line_bresenham(int(rotated_points[i][0]), int(rotated_points[i][1]),
                                                       int(rotated_points[next_index][0]), int(rotated_points[next_index][1])))

    # Gambar titik-titik hasil Bresenham
    for x, y in all_points:
        py5.point(x, y)

def segitiga_siku(xa, ya, alas, tinggi, c=[255,0,0,255]):
    py5.stroke(*c)
    points = []
    points.extend(primitif.line.line_bresenham(xa, ya, xa + alas, ya))  # Alas
    points.extend(primitif.line.line_bresenham(xa + alas, ya, xa, ya + tinggi))  # Sisi miring
    points.extend(primitif.line.line_bresenham(xa, ya + tinggi, xa, ya))  # Sisi tegak
    for x, y in points:
        py5.point(x, y)
# Fungsi untuk membuat segitiga sama kaki
def segitiga_sama_kaki(xa, ya, alas, tinggi):
    points = [
        [xa, ya, 1],  # Titik pertama (sudut lancip)
        [xa + alas / 2, ya + tinggi, 1],  # Titik kedua (alas kanan)
        [xa - alas / 2, ya + tinggi, 1],  # Titik ketiga (alas kiri)
    ]
    return np.array(points)

# Fungsi untuk menggambar segitiga menggunakan garis Bresenham (hanya x dan y)
def draw_transformed_triangle(points, color=[255,0,0,255]):
    py5.stroke(*color)
    all_points = []
    for i in range(3):
        x1, y1 = points[i][:2]  # Ambil hanya x dan y
        x2, y2 = points[(i + 1) % 3][:2]  # Ambil hanya x dan y dari titik berikutnya
        # Gambar garis dengan Bresenham antara dua titik
        all_points.extend(primitif.line.line_bresenham(int(x1), int(y1), int(x2), int(y2)))    # Gambar titik-titik hasil Bresenham
    for x, y in all_points:
        py5.point(x, y)
        
def trapesium_siku(xa, ya, aa, ab, tinggi, c=[255,0,0,255], reflect=False, tx=0, ty=0, rotate_angle=0, refx=0, refy=0):
    py5.stroke(*c)
    points = []

    # Koordinat awal trapesium sebelum refleksi dan transformasi
    points.extend(primitif.line.line_bresenham(xa, ya, xa + aa, ya))  # Sisi atas
    points.extend(primitif.line.line_bresenham(xa + aa, ya, xa + ab, ya + tinggi))  # Garis miring kanan
    points.extend(primitif.line.line_bresenham(xa + ab, ya + tinggi, xa, ya + tinggi))  # Sisi bawah
    points.extend(primitif.line.line_bresenham(xa, ya + tinggi, xa, ya))  # Sisi kiri
    
    # Konversi points ke numpy array untuk transformasi
    points = np.array(points)

    # Jika parameter refleksi True, refleksikan terhadap sumbu Y
    if reflect:
        points = np.array([reflect2D(np.array([x, y]), axis='y') for x, y in points])

    # Terapkan translasi jika tx atau ty tidak nol
    if tx != 0 or ty != 0:
        points = translatePoints(points, tx, ty)

    # Terapkan rotasi jika rotate_angle tidak nol
    if rotate_angle != 0:
        points = np.array([rotate2D(rotate_angle, refx, refy).dot([x, y, 1])[:2] for x, y in points])

    # Gambar titik-titik trapesium
    for x, y in points:
        py5.point(x, y)

def persegi_titik_titik(xa, ya, panjang, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa,ya,xa+panjang,ya)))
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa,ya+panjang,xa+panjang,ya+panjang)))
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa,ya,xa,ya+panjang)))
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa+panjang,ya, xa+panjang,ya+panjang)))

def persegi_garis_kosong_garis(xa, ya, panjang, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa,ya,xa+panjang,ya)))
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa,ya+panjang,xa+panjang,ya+panjang)))
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa,ya,xa,ya+panjang)))
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa+panjang,ya, xa+panjang,ya+panjang)))
    
def persegi_garis_titik_titik(xa, ya, panjang, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa,ya,xa+panjang,ya)))
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa,ya+panjang,xa+panjang,ya+panjang)))
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa,ya,xa,ya+panjang)))
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa+panjang,ya, xa+panjang,ya+panjang)))
    

def persegi_panjang_titik_titik(xa, ya, panjang, lebar, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa,ya,xa+panjang,ya)))
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa,ya+lebar,xa+panjang,ya+lebar)))
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa,ya,xa,ya+lebar)))
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa+panjang,ya,xa+panjang,ya+lebar)))

def persegi_panjang_garis_kosong_garis(xa, ya, panjang, lebar, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa,ya,xa+panjang,ya)))
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa,ya+lebar,xa+panjang,ya+lebar)))
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa,ya,xa,ya+lebar)))
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa+panjang,ya,xa+panjang,ya+lebar)))

def persegi_panjang_garis_titik_titik(xa, ya, panjang, lebar, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa,ya,xa+panjang,ya)))
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa,ya+lebar,xa+panjang,ya+lebar)))
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa,ya,xa,ya+lebar)))
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa+panjang,ya,xa+panjang,ya+lebar)))


def segitiga_siku_siku_titik_titik(xa, ya, alas, tinggi, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa, ya, xa + alas, ya)))
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa + alas, ya, xa, ya + tinggi)))
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa, ya + tinggi, xa, ya)))

def segitiga_siku_siku_garis_kosong_garis(xa, ya, alas, tinggi, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa, ya, xa + alas, ya)))
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa + alas, ya, xa, ya + tinggi)))
    py5.points(convert_to_garis_kosong_garis(primitif.line.line_dda(xa, ya + tinggi, xa, ya)))

def segitiga_siku_siku_garis_titik_titik(xa, ya, alas, tinggi, c=[255,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa, ya, xa + alas, ya)))
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa + alas, ya, xa, ya + tinggi)))
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa, ya + tinggi, xa, ya)))


def trapesium_siku_titik_titik(xa, ya, aa, ab, tinggi, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa, ya, xa + aa, ya)))  # Sisi atas
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa + aa, ya, xa + ab, ya + tinggi)))  # Garis miring kanan
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa + ab, ya + tinggi, xa, ya + tinggi)))  # Sisi bawah
    py5.points(convert_to_titik_titik(primitif.line.line_dda(xa, ya + tinggi, xa, ya)))  # Sisi kiri

def trapesium_siku_garis_kosong_garis(xa, ya, aa, ab, tinggi, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.line(xa, ya, xa + aa, ya)  # Sisi atas
    py5.line(xa + aa, ya, xa + ab, ya + tinggi)  # Garis miring kanan
    py5.line(xa + ab, ya + tinggi, xa, ya + tinggi)  # Sisi bawah
    py5.line(xa, ya + tinggi, xa, ya)  # Sisi kiri

def trapesium_siku_garis_titik_titik(xa, ya, aa, ab, tinggi, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.line(xa, ya, xa + aa, ya)  # Sisi atas
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa + aa, ya, xa + ab, ya + tinggi)))  # Garis miring kanan
    py5.line(xa + ab, ya + tinggi, xa, ya + tinggi)  # Sisi bawah
    py5.points(convert_to_garis_titik_titik(primitif.line.line_dda(xa, ya + tinggi, xa, ya)))  # Sisi kiri


def kali(xa, ya, panjang, c=[255,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_bresenham(xa,ya,xa+panjang,ya+panjang))
    py5.points(primitif.line.line_bresenham(xa,ya+panjang,xa+panjang,ya))

def convert_to_titik_titik(array_of_point):
    #menjadikan array jika genap diisi 0, agar bisa dijadikan titik-titik
    for i in range(len(array_of_point)):
        if i%10 == 0:
            array_of_point[i] = [0,0]
    return np.array(array_of_point)
def convert_to_garis_kosong_garis(array_of_point):
    for i in range(len(array_of_point)):
        if i%5 != 0:
            array_of_point[i] = [0,0]
    return np.array(array_of_point)
def convert_to_garis_titik_titik(array_of_point):
    for i in range(len(array_of_point)):
        if i%2 == 0 | i%7 == 0:
            array_of_point[i] = [0,0]
    return np.array(array_of_point)

def circlePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
        [xc + y, yc + x],
        [xc - y, yc + x],
        [xc + y, yc - x],
        [xc - y, yc - x],
        ]
    return np.array(res)

def lingkaran(xc, yc, radius, c=[255,0,0,255]):
    x = 0
    y = radius
    p = 1 - radius
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(circlePlotPoints(xc, yc, x, y))
    
    while(x < y):
        x+=1
        if (p < 0):
            p+= 2*x + 1
        else:
            y-=1
            p+= 2*(x-y) + 1
        py5.points(circlePlotPoints(xc, yc, x, y))
        
        
def ellipsePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y]
    ]
    return np.array(res)

def ellips(xc, yc, rx, ry, c=[255,0,0,255]):
    x = 0
    y = ry
    rx_sq = rx * rx
    ry_sq = ry * ry
    two_rx_sq = 2 * rx_sq
    two_ry_sq = 2 * ry_sq

    # Decision parameter region 1
    p1 = ry_sq - (rx_sq * ry) + (0.25 * rx_sq)
    dx = two_ry_sq * x
    dy = two_rx_sq * y

    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(ellipsePlotPoints(xc, yc, x, y))  # Plot titik pertama

    # Region 1
    while dx < dy:
        x += 1
        dx += two_ry_sq
        if p1 < 0:
            p1 += ry_sq + dx
        else:
            y -= 1
            dy -= two_rx_sq
            p1 += ry_sq + dx - dy

        py5.points(ellipsePlotPoints(xc, yc, x, y))

    # Decision parameter region 2
    p2 = (ry_sq * (x + 0.5) ** 2) + (rx_sq * (y - 1) ** 2) - (rx_sq * ry_sq)

    # Region 2
    while y > 0:
        y -= 1
        dy -= two_rx_sq
        if p2 > 0:
            p2 += rx_sq - dy
        else:
            x += 1
            dx += two_ry_sq
            p2 += rx_sq - dy + dx

        py5.points(ellipsePlotPoints(xc, yc, x, y))