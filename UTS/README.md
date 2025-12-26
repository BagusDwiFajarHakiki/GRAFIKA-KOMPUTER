Simulasi Tata Surya Realistis 2D dengan Python Turtle

a. Judul Proyek
   Implementasi Transformasi Geometris dan Algoritma Grafika Primitif dalam Simulasi Tata Surya 2D

b. Konsep Grafika yang Digunakan
    Proyek ini menerapkan konsep dasar Grafika Komputer 2D dengan pendekatan berikut:
    1. Sistem Koordinat Kartesius: Layar dimodelkan sebagai bidang X-Y di mana matahari berada di titik pusat (0,0).
    2. Rendering Sprite & Primitif: Penggabungan antara penggunaan sprite (gambar bitmap), dan rendering manual (menggambar pixel/garis).
    3. Penerapan konsep Parent-Child, di mana posisi Satelit bergantung pada posisi Bumi, dan posisi Bumi bergantung pada Matahari.
    4. Animasi Frame-by-Frame: Menggunakan teknik double buffering (tracer(0) dan update()) untuk menciptakan animasi yang halus tanpa kedipan.

c. Algoritma yang Dipakai
   1. Transformasi Geometris 2D (Rotasi & Translasi) yang digunakan untuk menghitung posisi orbit planet setiap detiknya.
   2. Algoritma Gambar Garis (Line Drawing) yang diterapkan secara manual pada fitur "Targeting UI" (garis penunjuk data di bawah planet Bumi).
   3. Algoritma Gambar Poligon yang diterapkan pada Kotak Radar (Target Box) yang membungkus planet Bumi.
   4. Algoritma Lingkaran (Circle Drawing) yang digunakan untuk memvisualisasikan Lintasan Orbit planet.

d. Cara Menjalankan Program
   1. Install library turtle, math, time, os pada thonny
   2. Donwload seluruh file dan simpan pada tempat yang sama
   3. Jalankan program dan lihat hasilnya
