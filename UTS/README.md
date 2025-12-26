Simulasi Tata Surya Realistis 2D dengan Python Turtle

a. Judul Proyek
   "Implementasi Transformasi Geometris dan Algoritma Grafika Primitif dalam Simulasi Tata Surya 2D"

b. Konsep Grafika yang Digunakan
    Proyek ini menerapkan konsep dasar Grafika Komputer 2D dengan pendekatan berikut:
    1. Sistem Koordinat Kartesius: Layar dimodelkan sebagai bidang X-Y di mana matahari berada di titik pusat (0,0).
    2. Rendering Sprite & Primitif: Penggabungan antara penggunaan sprite (gambar bitmap), dan rendering manual (menggambar pixel/garis).
    3. Penerapan konsep Parent-Child, di mana posisi Satelit bergantung pada posisi Bumi, dan posisi Bumi bergantung pada Matahari.
    4. Animasi Frame-by-Frame: Menggunakan teknik double buffering (tracer(0) dan update()) untuk menciptakan animasi yang halus tanpa kedipan.

c. Algoritma yang Dipakai
Sesuai syarat tugas "Minimal 4 Materi", proyek ini mengimplementasikan algoritma berikut:Transformasi Geometris 2D (Rotasi & Translasi):Digunakan untuk menghitung posisi orbit planet setiap detiknya.Rumus Rotasi: $x' = x \cos(\theta) - y \sin(\theta)$ dan $y' = x \sin(\theta) + y \cos(\theta)$.Digunakan juga untuk logika satelit yang mengorbit Bumi (Rotasi Lokal + Translasi ke posisi induk).Algoritma Gambar Garis (Line Drawing):Diterapkan secara manual pada fitur "Targeting UI" (garis penunjuk data di bawah planet Bumi).Program menarik garis dari koordinat poligon menuju teks label menggunakan koordinat yang dihitung.Algoritma Gambar Poligon:Diterapkan pada Kotak Radar (Target Box) yang membungkus planet Bumi.Algoritma menggambar segiempat tertutup dengan menghubungkan 4 titik sudut $(x \pm size, y \pm size)$ secara berurutan.Algoritma Lingkaran (Circle Drawing):Digunakan untuk memvisualisasikan Lintasan Orbit planet.Diterapkan untuk memastikan planet bergerak pada jalur kurva tertutup yang presisi mengelilingi pusat.
