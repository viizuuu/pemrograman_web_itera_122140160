const API_KEY = "5485a3609f61ad007140f6ff164c57b8";

// ====== Class Catatan Harian ======
class CatatanHarian {
  constructor(inputId, daftarId) {
    this.input = document.getElementById(inputId);
    this.daftar = document.getElementById(daftarId);
    this.catatan = JSON.parse(localStorage.getItem("catatan")) || [];
    this.render();
  }

  tambah = () => {
    const isi = this.input.value.trim();
    if (!isi) return;

    this.catatan.push(isi);
    localStorage.setItem("catatan", JSON.stringify(this.catatan));
    this.input.value = "";
    this.render();
  };

  render = () => {
    this.daftar.innerHTML = "";
    this.catatan.forEach((isi, i) => {
      const p = document.createElement("p");
      p.textContent = `${i + 1}. ${isi}`;
      this.daftar.appendChild(p);
    });
  };
}

// ====== Fungsi Tampilkan Cuaca ======
const tampilkanCuaca = async () => {
  const input = document.getElementById("kotaInput");
  const output = document.getElementById("cuaca");
  const kota = input.value.trim();

  if (!kota) {
    output.innerHTML = "<p>Silakan masukkan nama kota terlebih dahulu.</p>";
    return;
  }

  try {
    const res = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(
        kota
      )}&appid=${API_KEY}&units=metric&lang=id`
    );
    if (!res.ok) throw new Error("Kota tidak ditemukan.");

    const data = await res.json();
    const suhu = data.main.temp;
    const kondisi = data.weather[0].description;

    output.innerHTML = `<p>Cuaca di <strong>${kota}</strong>: ${kondisi}, suhu ${suhu}°C</p>`;
  } catch (err) {
    output.innerHTML = `<p>Terjadi kesalahan: ${err.message}</p>`;
  }
};

// ====== Inisialisasi Event ======
document.addEventListener("DOMContentLoaded", () => {
  const catatanApp = new CatatanHarian("noteInput", "daftarCatatan");

  document
    .getElementById("btnSimpan")
    .addEventListener("click", () => catatanApp.tambah());

  document
    .getElementById("btnCuaca")
    .addEventListener("click", tampilkanCuaca);
});
