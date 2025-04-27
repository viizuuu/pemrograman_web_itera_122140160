# math_operations.py

# Variabel konstanta
PI = 3.14159

# Fungsi untuk menghitung luas dan keliling persegi
def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

# Fungsi untuk menghitung luas dan keliling persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

# Fungsi untuk menghitung luas dan keliling lingkaran
def luas_lingkaran(jari_jari):
    return PI * jari_jari * jari_jari

def keliling_lingkaran(jari_jari):
    return 2 * PI * jari_jari

# Fungsi untuk konversi suhu
def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_ke_kelvin(celsius):
    return celsius + 273.15
