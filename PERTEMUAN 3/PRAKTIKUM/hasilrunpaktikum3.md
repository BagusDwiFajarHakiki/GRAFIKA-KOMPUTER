1. LOOP

       for y in range(0, 5):
         for x in range(0, 10):
             print("*", end="")
         print()

   <img width="328" height="272" alt="image" src="https://github.com/user-attachments/assets/d09ba499-6141-40a8-bf38-0494e27c3816" />

2. KOORDINAT

        import math
        
        x1 = float(input("Masukkan x1: "))
        y1 = float(input("Masukkan y1: "))
        x2 = float(input("Masukkan x2: "))
        y2 = float(input("Masukkan y2: "))
        
        jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        if x1 > 0 and y1 > 0:
            kuadran = "Kuadran I"
        elif x1 < 0 and y1 > 0:
            kuadran = "Kuadran II"
        elif x1 < 0 and y1 < 0:
            kuadran = "Kuadran III"
        elif x1 > 0 and y1 < 0:
            kuadran = "Kuadran IV"
        
        print("\n=== HASIL ===\n")
        
        print(f"Titik pertama: ({x1}, {y1})")
        print(f"Titik kedua  : ({x2}, {y2})")
        print(f"Jarak antar titik: {jarak:.2f}")
        print(f"Titik pertama berada di: {kuadran}")

   <img width="565" height="803" alt="image" src="https://github.com/user-attachments/assets/75b09411-7361-41b3-b102-20aa1e0f8b87" />

3. KOORDINAT DENGAN TANDA X

         for y in range(0, 5):
           for x in range(0, 10):
              if x == 2 and y == 3:
                  print("X", end=" ")
              else:
                  print("*", end=" ")
          print()

   <img width="371" height="331" alt="image" src="https://github.com/user-attachments/assets/498be00a-f684-43e5-8bf3-d4e4adcd6aa0" />

4. KOORDINAT DENGAN TANDA X YANG KEDUA

         for y in range(0, 10):
          for x in range(0, 10):
              if x == 4 and y == 6:
                  print("X", end=" ")
              else:
                  print(".", end=" ")
          print()

   <img width="382" height="422" alt="image" src="https://github.com/user-attachments/assets/d9ab96fe-58be-4ef3-81da-d568af42991d" />

5. GARIS & TITIK

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

   <img width="1048" height="776" alt="image" src="https://github.com/user-attachments/assets/16629a87-11e9-4cac-babc-1cdb0d507d53" />
   <img width="1003" height="654" alt="image" src="https://github.com/user-attachments/assets/b049a35e-633d-43eb-981a-59e86ac9daea" />
   <img width="1019" height="377" alt="image" src="https://github.com/user-attachments/assets/f6cc3005-a5b4-41ec-8066-48caabf6ba79" />
