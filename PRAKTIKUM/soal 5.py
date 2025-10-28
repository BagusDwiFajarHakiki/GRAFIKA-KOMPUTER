#x1, y1 = 0, 0
#x2, y2 = 5, 3
#
#print(f"Titik Awal : ({x1},{y1})")
#print(f"Titik Akhir: ({x2},{y2})\n")
#
#n = 5
#for i in range(n + 1):
#    x = x1 + (x2 - x1) * i / n
#    y = y1 + (y2 - y1) * i / n
#    print(f"Titik ke-{i}: ({x:.0f},{y:.0f})")

# 1. DEFINISI TITIK AWAL DAN AKHIR
x1, y1 = 0, 0
x2, y2 = 5, 3

print(f"Titik Awal : ({x1},{y1})")
print(f"Titik Akhir: ({x2},{y2})\n")

# 2. HITUNG DAN KUMPULKAN TITIK KOORDINAT (PIKSEL)
n = 5
koordinat_piksel = []

for i in range(n + 1):
    # Rumus Interpolasi Linier Parametrik
    x_float = x1 + (x2 - x1) * i / n
    y_float = y1 + (y2 - y1) * i / n
    
    # Ambil koordinat Integer (Piksel) dengan pembulatan
    x_int = round(x_float)
    y_int = round(y_float)
    
    # Tambahkan koordinat integer ke daftar
    koordinat_piksel.append((x_int, y_int))
    
    # Menampilkan daftar titik
    print(f"Titik ke-{i}: ({x_int},{y_int})") 

print("\n--------------------------")
print("VISUALISASI GRID KOORDINAT")
print("--------------------------")

# 3. TENTUKAN UKURAN GRID
# Lebar grid (sumbu X) harus mencakup dari 0 hingga x2
max_x = max(x1, x2)
# Tinggi grid (sumbu Y) harus mencakup dari 0 hingga y2
max_y = max(y1, y2)

# 4. BUAT GRID KOSONG (dengan karakter '.')
# Kita perlu membalik sumbu Y saat mencetak karena layar/output dimulai dari atas (Y terbesar)
grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

# 5. TANDAI TITIK GARIS (dengan karakter '*')
for x_coord, y_coord in koordinat_piksel:
    # Karena Y=0 adalah baris terbawah, kita harus membalik indeks baris.
    # Indeks baris = max_y - y_coord
    grid_row = max_y - y_coord
    grid_col = x_coord
    
    # Pastikan koordinat berada dalam batas grid
    if 0 <= grid_row <= max_y and 0 <= grid_col <= max_x:
        grid[grid_row][grid_col] = '*'

# 6. TAMPILKAN GRID
print("Y")
for r in range(max_y + 1):
    # Tampilkan Label Sumbu Y (membalik urutan)
    y_label = max_y - r
    print(f"{y_label} |", end="") 
    
    # Tampilkan baris grid
    print(" ".join(grid[r]))

# Tampilkan Sumbu X dan Label
print("   " + "-" * (2 * (max_x + 1) - 1))
print("   0 1 2 3 4 5 X")