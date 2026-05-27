# sistemcerdaskesehatanfinal
# HealthTech CF - Sistem Pakar Diagnosa Penyakit Tropis di indonesia menggunakan dataset

Sistem pakar berbasis web ini dirancang untuk membantu melakukan diagnosa awal terhadap 10 jenis penyakit tropis yang umum ditemukan di Indonesia. Sistem ini mengimplementasikan metode Certainty Factor (CF) untuk mengatasi ketidakpastian pada gejala yang dirasakan oleh pasien, sehingga menghasilkan tingkat keyakinan dalam bentuk persentase.

---

## Fitur Utama dan cara pakai

Sistem ini terdiri dari 6 modul utama yang dapat diakses melalui menu navigasi:

1. **Dashboard**
   Halaman utama yang menyajikan ringkasan statistik sistem (jumlah penyakit target, algoritma yang digunakan, dan jumlah gejala terdaftar) serta visualisasi banner yang modern.
2. **Mulai Diagnosa**
   Modul inti tempat pengguna dapat memilih gejala-gejala yang dialami dan menentukan tingkat keparahan/keyakinan dari setiap gejala tersebut untuk dihitung menggunakan rumus Certainty Factor.
3. **Basis Pengetahuan (Kamus Medis)**
   Eksplorasi daftar lengkap penyakit tropis target beserta gejala-gejala terkait yang bersumber dari data pakar.
4. **Analisis Dataset**
   Menu visualisasi yang menampilkan transparansi data latih yang digunakan oleh sistem untuk melakukan perhitungan.
5. **Riwayat Pasien**
   Mencatat dan menampilkan riwayat hasil diagnosa secara permanen di database lokal. Dilengkapi fitur untuk mengosongkan riwayat.
6. Tentang Sistem
   Berisi tentang semua yang ada dalam website mulai dari dataset yang digunakan pengembang dan lain-lain.
7. Login
   Website ini dirancang dengan menu login dimana kalian harus login untuk menggunakan fitur" yang ada username : admin , password : admin123
---

## Teknologi yang Digunakan

* **Python 3.14+** (Bahasa pemrograman utama)
* **Streamlit** (Framework untuk antarmuka web yang interaktif)
* **Pandas** (Eksplorasi, pembersihan, dan manipulasi dataset langsung dari file kompresi .zip)
* **SQLite3** (Database lokal untuk pengelolaan data riwayat pasien)

---

## Cara Penggunaan Website

Berikut adalah panduan langkah demi langkah untuk menggunakan sistem pakar ini:

### Langkah 1: Proses Otentikasi (Login)
* Buka menu **Login** di halaman navigasi.
* Masukkan kredensial (Username & Password) **(username : admin , password : admin123 ) ** yang telah didaftarkan pada sistem untuk membuka akses penuh ke modul diagnosa.

### Langkah 2: Memilih Gejala
* Masuk ke modul **Mulai Diagnosa**.
* Pada kolom **Pilih Gejala**, ketik atau pilih satu atau beberapa gejala yang sedang dirasakan (Sistem mendukung lebih dari 50 jenis gejala medis).

### Langkah 3: Menentukan Tingkat Keyakinan (Certainty Value)
* Setelah gejala dipilih, akan muncul pilihan dropdown tingkat keyakinan untuk masing-masing gejala.
* Pilih kondisi yang paling sesuai dengan yang Anda rasakan:
  * Tidak (Nilai CF: 0.0)
  * Tidak Yakin (Nilai CF: 0.2)
  * Sedikit Yakin (Nilai CF: 0.4)
  * Cukup Yakin (Nilai CF: 0.6)
  * Yakin (Nilai CF: 0.8)
  * Sangat Yakin (Nilai CF: 1.0)

### Langkah 4: Analisis dan Hasil Diagnosa
* Klik tombol **Analisis Penyakit**.
* Sistem akan memproses bobot gejala menggunakan kalkulasi Certainty Factor gabungan.
* Hasil akan memunculkan **Kemungkinan Terbesar** jenis penyakit yang diderita beserta nilai persentase tingkat keyakinannya.
* Di bagian bawah, sistem juga menampilkan tabel alternatif penyakit lain yang relevan berdasarkan gejala yang dimasukkan.

### Langkah 5: Memeriksa Catatan Medis
* Masuk ke menu **Riwayat Diagnosa**.
* Anda dapat melihat tabel permanen dari database yang mencatat: Waktu Diagnosa, Penyakit Terdiagnosa, Tingkat Keyakinan, dan Daftar Gejala yang Diinput.
* Gunakan tombol **Hapus Riwayat (Database)** jika ingin membersihkan seluruh catatan data di dalam database SQLite.
