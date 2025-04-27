# Program Pengelolaan Data Nilai Mahasiswa

# Data mahasiswa (list berisi dictionary)
mahasiswa = [
    {"nama": "Naruto", "nim": "122140271", "nilai_uts": 80, "nilai_uas": 85, "nilai_tugas": 78},
    {"nama": "Sasuke", "nim": "122140272", "nilai_uts": 75, "nilai_uas": 70, "nilai_tugas": 72},
    {"nama": "Sakura", "nim": "122140273", "nilai_uts": 65, "nilai_uas": 60, "nilai_tugas": 70},
    {"nama": "Hinata", "nim": "122140274", "nilai_uts": 55, "nilai_uas": 58, "nilai_tugas": 60},
    {"nama": "Shikamaru", "nim": "122140275", "nilai_uts": 40, "nilai_uas": 45, "nilai_tugas": 50}
]

# Menghitung nilai akhir dan grade
for mhs in mahasiswa:
    nilai_akhir = (0.3 * mhs["nilai_uts"]) + (0.4 * mhs["nilai_uas"]) + (0.3 * mhs["nilai_tugas"])
    mhs["nilai_akhir"] = nilai_akhir
    
    # Menentukan grade
    if nilai_akhir >= 80:
        mhs["grade"] = "A"
    elif nilai_akhir >= 70:
        mhs["grade"] = "B"
    elif nilai_akhir >= 60:
        mhs["grade"] = "C"
    elif nilai_akhir >= 50:
        mhs["grade"] = "D"
    else:
        mhs["grade"] = "E"

# Menampilkan data dalam format tabel
print("="*80)
print(f"{'Nama':<15}{'NIM':<10}{'UTS':<7}{'UAS':<7}{'Tugas':<7}{'Nilai Akhir':<15}{'Grade'}")
print("="*80)

for mhs in mahasiswa:
    print(f"{mhs['nama']:<15}{mhs['nim']:<10}{mhs['nilai_uts']:<7}{mhs['nilai_uas']:<7}{mhs['nilai_tugas']:<7}{mhs['nilai_akhir']:<15.2f}{mhs['grade']}")

print("="*80)

# Menentukan mahasiswa dengan nilai tertinggi dan terendah
nilai_tertinggi = max(mahasiswa, key=lambda x: x["nilai_akhir"])
nilai_terendah = min(mahasiswa, key=lambda x: x["nilai_akhir"])

print(f"Mahasiswa dengan nilai tertinggi: {nilai_tertinggi['nama']} ({nilai_tertinggi['nilai_akhir']:.2f})")
print(f"Mahasiswa dengan nilai terendah : {nilai_terendah['nama']} ({nilai_terendah['nilai_akhir']:.2f})")
