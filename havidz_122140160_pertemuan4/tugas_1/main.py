# Program Penghitung BMI (Body Mass Index)

# Membuat variabel berat badan (dalam kilogram) dan tinggi badan (dalam meter)
berat = float(input("Masukkan berat badan Anda (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan Anda (cm): "))

tinggi = tinggi_cm / 100  # mapping, konversi ke meter

# Menghitung BMI
bmi = berat / (tinggi * tinggi)

# Menentukan kategori BMI
if bmi < 18.5:
    kategori = "Berat badan kurang"
elif bmi < 25:
    kategori = "Berat badan normal"
elif bmi < 30:
    kategori = "Berat badan berlebih"
else:
    kategori = "Obesitas"

# Menampilkan hasil
print(f"\nBMI Anda adalah: {bmi:.2f}")
print(f"Kategori: {kategori}")
