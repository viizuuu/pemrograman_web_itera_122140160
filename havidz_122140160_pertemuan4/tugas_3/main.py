# main.py

# Cara 1: Impor seluruh modul
import math_operations

# Cara 2: Impor fungsi tertentu dari modul
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin

def garis():
    print("=" * 50)

def main():
    garis()
    print("Perhitungan Geometri")
    garis()
    sisi = 5
    panjang = 8
    lebar = 4
    jari_jari = 7

    print(f"Luas persegi (sisi={sisi}): {math_operations.luas_persegi(sisi)}")
    print(f"Keliling persegi (sisi={sisi}): {math_operations.keliling_persegi(sisi)}")
    print(f"Luas persegi panjang (p={panjang}, l={lebar}): {math_operations.luas_persegi_panjang(panjang, lebar)}")
    print(f"Keliling persegi panjang (p={panjang}, l={lebar}): {math_operations.keliling_persegi_panjang(panjang, lebar)}")
    print(f"Luas lingkaran (r={jari_jari}): {math_operations.luas_lingkaran(jari_jari):.2f}")
    print(f"Keliling lingkaran (r={jari_jari}): {math_operations.keliling_lingkaran(jari_jari):.2f}")

    garis()
    print("Konversi Suhu")
    garis()
    celsius = 25

    print(f"{celsius}°C = {celsius_ke_fahrenheit(celsius):.2f}°F")
    print(f"{celsius}°C = {celsius_ke_kelvin(celsius):.2f}K")

    garis()

if __name__ == "__main__":
    main()