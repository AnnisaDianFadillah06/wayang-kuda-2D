import numpy as np
import math

def translate2D(tx, ty, tm):
    m = np.identity(3)
    m[0][2] = tx
    m[1][2]=ty
    return np.dot(m, tm)

def translatePoints(points, tx, ty):
    # Menggeser semua titik dengan (tx, ty)
    translated_points = points.copy()
    translated_points[:, 0] += tx  # Menambahkan tx ke x
    translated_points[:, 1] += ty  # Menambahkan ty ke y
    return translated_points

def scale2D(sx, sy, refx, refy, tm):
    m = np.identity(3)
    m[0][0] = sx
    m[0][2] = (1-sx)*refx
    m[1][1] = sy 
    m[1][2] = (1-sy)*refy
    return np.dot(m, tm)

def rotate2D(a, refx, refy):
    m = np.identity(3)
    tm = np.identity(3)
    a = math.radians(a)
    m[0][0] = round(math.cos(a))
    m[0][1] = round(- math.sin(a))
    m[0][2] = refx * (1 - round(math.cos(a))) + refy * round(math.sin(a))
    m[1][0] = round(math.sin(a))
    m[1][1] = round(math.cos(a))
    m[1][2] = refy * (1 -round(math.cos(a))) - refx * round(math.sin(a))
    return np.dot(m, tm)

def transformPoints2D(pts, tm):
    i, _  = pts.shape
    
    for k in range(i):
        tmp = tm[0][0] * pts[k,0] + tm[0][1] * pts[k,1] + tm[0][2]
        pts[k,1] = tm[1][0] * pts[k,0] + tm[1][1] * pts[k,1] + tm[1][2]
        pts[k,0] = tmp

    return pts

# Fungsi untuk refleksi terhadap sumbu yang dipilih
def reflect2D(points, axis='x'):
    # Matriks identitas 3x3
    m = np.identity(3)
    
    if axis == 'x':
        m[1][1] = -1  # Mencerminkan terhadap sumbu X
    elif axis == 'y':
        m[0][0] = -1  # Mencerminkan terhadap sumbu Y
    elif axis == 'y=x':
        m[0][0] = 0  # Mencerminkan terhadap garis y=x
        m[1][1] = 0
        m[0][1] = 1
        m[1][0] = 1
    
    # Tambahkan koordinat homogen [1] untuk setiap titik
    homogeneous_points = np.array([[points[0], points[1], 1]])
    
    # Refleksi terhadap matriks
    reflected_points = np.dot(homogeneous_points, m)
    
    
    # Kembalikan hanya koordinat x dan y
    return reflected_points[0][:2]


def reflect2D2(points, axis='x'):
    # Matriks identitas 3x3
    m = np.identity(3)
    
    if axis == 'x':
        m[1][1] = -1  # Mencerminkan terhadap sumbu X
    elif axis == 'y':
        m[0][0] = -1  # Mencerminkan terhadap sumbu Y
    elif axis == 'y=x':
        m[0][0] = 0  # Mencerminkan terhadap garis y=x
        m[1][1] = 0
        m[0][1] = 1
        m[1][0] = 1
    
    # Tambahkan koordinat homogen [1] untuk setiap titik
    homogeneous_points = np.hstack((points[:, :2], np.ones((points.shape[0], 1))))  # Mengubah menjadi [x, y, 1]
    
    # Refleksi terhadap matriks
    reflected_points = np.dot(homogeneous_points, m)
    
    # Kembalikan hanya koordinat x dan y
    return reflected_points[:, :2]  # Mengembalikan array 2D [x, y]


def rotate2D(a, refx, refy):
    a = math.radians(a)
    m = np.identity(3)
    m[0][0] = math.cos(a)
    m[0][1] = -math.sin(a)
    m[0][2] = refx * (1 - math.cos(a)) + refy * math.sin(a)
    m[1][0] = math.sin(a)
    m[1][1] = math.cos(a)
    m[1][2] = refy * (1 - math.cos(a)) - refx * math.sin(a)
    return m

def translate2D(tx, ty):
    m = np.identity(3)
    m[0][2] = tx
    m[1][2] = ty
    return m

def shear2D(shx, shy):
    m = np.identity(3)
    m[0][1] = shx  # Shear faktor di sumbu X
    m[1][0] = shy  # Shear faktor di sumbu Y
    return m

def scalePoints(points, scale_factor):
    # Buat matriks skala 2D
    scale_matrix = np.array([
        [scale_factor, 0],
        [0, scale_factor]
    ])
    
    # Kalikan semua titik dengan matriks skala
    scaled_points = np.dot(points, scale_matrix.T)
    
    return scaled_points
