1. VARIABEL

        x = 50
        y = 100
        warna = "merah"
        print(f"Koordinat titik ({x}, {y}) dengan warna {warna}.")

   <img width="646" height="204" alt="image" src="https://github.com/user-attachments/assets/d969f95f-2fb5-4355-880e-017038c20e81" />

2. INPUT OUTPUT

        x = int(input("Masukkan nilai x: "))
        y = int(input("Masukkan niali y: "))
        warna = input("Masukkan warna titik: ")
        
        print(f"Titik berada di ({x}), {y}) dan berwarna {warna}.")

   <img width="654" height="278" alt="image" src="https://github.com/user-attachments/assets/a8eb5ab2-432e-4137-be1b-f6f73ae7a7f0" />

3. KONDISI & LOOP

        x = int(input("masukkan nilai x: "))
        
        if x > 0:
             print("titik di kanan layar.")
        elif x < 0:
            print("Titik di kiri layar.")
        else:
            print ("Titik di tengah.")
        
        print("Menampilkan 5 titik:")
        for i in range(1, 6):
            print(f"Titik ke-{i}")

   <img width="434" height="502" alt="image" src="https://github.com/user-attachments/assets/c81885be-bbc2-4af5-9a8a-dfd162477894" />

4. FUNGSI

        import math
        
        def hitung_jarak(x1, y1, x2, y2):
            jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            return jarak
        
        hasil = hitung_jarak(0, 0, 3, 4)
        print(f"Jarak antara dua titik: {hasil}")

   <img width="568" height="298" alt="image" src="https://github.com/user-attachments/assets/91988cbe-b707-4768-bce3-7b0e5474d3b0" />

5. LIST TUPLE & DICTIONARY

        # 1. Membuat dan Menampilkan List Pasangan Titik
        titik_list = [(0, 0), (50, 50), (100, 0)]
        print("--- Menampilkan Semua Titik dalam List ---")
        for x, y in titik_list:
            print(f"Titik: ({x}, {y})")
            
        # 2. Menyimpan dan Menampilkan Nilai Tuple
        pusat = (0, 0)
        print("\n--- Titik Pusat (Tuple) ---")
        print(f"Nilai titik pusat adalah: {pusat}")
        
        # 3. Membuat dan Menampilkan Data Dictionary
        objek_attr = {"x": 10, "y": 20, "warna": "biru"}
        print("\n--- Atribut Objek (Dictionary) ---")
        
        # Mengambil nilai dari dictionary
        x_val = objek_attr["x"]
        y_val = objek_attr["y"]
        warna_val = objek_attr["warna"]
        
        # Menampilkan dalam format yang diminta
        print(f"Titik ({x_val}, {y_val}) berwarna {warna_val}.")

   <img width="641" height="756" alt="image" src="https://github.com/user-attachments/assets/e81002bd-ccfc-448d-9c0d-c32691b93069" />
