import turtle
import math
import time
import os

# =================================================================
#   BAGIAN 1: KONFIGURASI
# =================================================================

# --- FILE GAMBAR ---
IMG_BACKGROUND = "space2.gif" 
IMG_MATAHARI   = "matahari.gif"
IMG_SATELIT    = "satelit.gif"

# Gambar Planet
IMG_PLANETS = {
    "Merkurius": "merkurius.gif",
    "Venus":     "venus.gif",
    "Bumi":      "bumi.gif",
    "Mars":      "mars.gif",
    "Jupiter":   "jupiter.gif",
    "Saturnus":  "saturnus.gif",
    "Uranus":    "uranus.gif",
    "Neptunus":  "neptunus.gif"
}

# --- SETUP LAYAR FULL SCREEN ---
screen = turtle.Screen()
screen.title("Sistem Tata Surya Realistis")
screen.bgcolor("black") 

# [LOGIKA FULL SCREEN]
screen.setup(width=1000, height=800)

# --- MEMUAT GAMBAR ---
print("Memuat aset gambar...")
try:
    if os.path.exists(IMG_BACKGROUND):
        screen.bgpic(IMG_BACKGROUND)
    
    screen.register_shape(IMG_MATAHARI)
    screen.register_shape(IMG_SATELIT)
    for nama in IMG_PLANETS:
        screen.register_shape(IMG_PLANETS[nama])
except Exception as e:
    print(f"[ERROR] Masalah gambar: {e}")

screen.tracer(0) # Matikan animasi otomatis

# =================================================================
# BAGIAN 2: LOGIKA MATEMATIKA
# =================================================================

def rotasi_titik(x, y, angle_deg):
    rad = math.radians(angle_deg)
    return (x * math.cos(rad) - y * math.sin(rad), 
            x * math.sin(rad) + y * math.cos(rad))

def draw_targeting_ui(t_pen, x, y, size=20):
    t_pen.color("cyan")
    t_pen.pensize(1)
    
    # 1. MATERI POLIGON: Menggambar Kotak (Segiempat) di sekitar planet
    # Mulai dari sudut kiri atas
    t_pen.penup()
    t_pen.goto(x - size, y + size) 
    t_pen.pendown()
    
    # Gambar 4 sisi (Logika Poligon Sederhana)
    t_pen.goto(x + size, y + size) # Kanan
    t_pen.goto(x + size, y - size) # Bawah
    t_pen.goto(x - size, y - size) # Kiri
    t_pen.goto(x - size, y + size) # Atas (Tutup Poligon)
    t_pen.penup()

    # 2. MATERI GARIS: Menggambar garis penghubung ke teks
    t_pen.goto(x, y - size) # Dari bawah kotak
    t_pen.pendown()
    t_pen.goto(x, y - size - 15) # Tarik garis ke bawah (Menuju teks)
    t_pen.penup()
# =================================================================
# BAGIAN 3: SETUP OBJEK
# =================================================================

# 1. Matahari
t_matahari = turtle.Turtle()
t_matahari.shape(IMG_MATAHARI)
t_matahari.goto(0, 0)

# 2. Satelit
t_satelit = turtle.Turtle()
t_satelit.shape(IMG_SATELIT)
t_satelit.penup()
# Variabel khusus untuk satelit
satelit_data = {
    "induk": "Bumi",  # Satelit akan menempel pada Bumi
    "jarak": 35,      # Jarak orbit dari Bumi
    "speed": 6.0,     # Kecepatan orbit satelit
    "angle": 0        # Sudut awal
}

# 3. Pen Info & Orbit
pen_info = turtle.Turtle()
pen_info.hideturtle(); pen_info.penup(); pen_info.color("white")
pen_orbit = turtle.Turtle()
pen_orbit.hideturtle(); pen_orbit.speed(0); pen_orbit.color("#333333")

# 4. Data Planet
data_planet_config = [
    {"nama": "Merkurius", "jarak": 60,  "speed": 4.1, "real": "57.9 Jt Km",  "moons": []},
    {"nama": "Venus",     "jarak": 95,  "speed": 1.6, "real": "108.2 Jt Km", "moons": []},
    {"nama": "Bumi",      "jarak": 145, "speed": 1.0, "real": "149.6 Jt Km", "moons": [{"dist": 20, "speed": 12, "col": "white"}]},
    {"nama": "Mars",      "jarak": 200, "speed": 0.8, "real": "227.9 Jt Km", "moons": [{"dist": 15, "speed": 9, "col": "gray"}]},
    {"nama": "Jupiter",   "jarak": 300, "speed": 0.4, "real": "778.6 Jt Km", "moons": [{"dist": 40, "speed": 5, "col": "yellow"}]}, 
    {"nama": "Saturnus",  "jarak": 390, "speed": 0.3, "real": "1.4 M Km",    "moons": [{"dist": 45, "speed": 4, "col": "orange"}]},
    {"nama": "Uranus",    "jarak": 460, "speed": 0.2, "real": "2.9 M Km",    "moons": [{"dist": 28, "speed": 6, "col": "cyan"}]},
    {"nama": "Neptunus",  "jarak": 520, "speed": 0.1, "real": "4.5 M Km",    "moons": [{"dist": 25, "speed": 5, "col": "white"}]}
]

# Gambar Garis Orbit (Statis)
print("Menggambar lintasan orbit...")
for p in data_planet_config:
    pen_orbit.penup()
    pen_orbit.goto(0, -p["jarak"])
    pen_orbit.pendown()
    pen_orbit.circle(p["jarak"])
pen_orbit.penup()

# Setup Objek Planet
planet_objects = []
for config in data_planet_config:
    t = turtle.Turtle()
    t.shape(IMG_PLANETS[config["nama"]])
    t.penup()
    
    moon_turtles = []
    for moon_cfg in config['moons']:
        mt = turtle.Turtle()
        mt.shape("circle"); mt.shapesize(0.15); mt.color(moon_cfg['col']); mt.penup()
        moon_turtles.append(mt)

    planet_objects.append({"turtle": t, "config": config, "moons_t": moon_turtles})

# =================================================================
# BAGIAN 4: LOOP UTAMA
# =================================================================

def main():
    sudut_global = 0
    # Koordinat Bumi untuk referensi Satelit
    bumi_x, bumi_y = 0, 0 
    
    try:
        while True:
            pen_info.clear()
            
            # --- 1. UPDATE PLANET ---
            for p_obj in planet_objects:
                t = p_obj["turtle"]
                cfg = p_obj["config"]
                
                # Gerakan Planet
                sudut_kini = sudut_global * cfg['speed']
                px, py = rotasi_titik(cfg['jarak'], 0, sudut_kini)
                t.goto(px, py)
                
                # Simpan posisi Bumi
                if cfg["nama"] == "Bumi":
                    bumi_x, bumi_y = px, py
                    
                    draw_targeting_ui(pen_info, px, py, 20)

                # Info Teks
                pen_info.goto(px, py - 55) 
                pen_info.write(f"{cfg['nama']}\n{cfg['real']}", align="center", font=("Consolas", 7, "normal"))

                # Gerakan Bulan
                for i, moon_cfg in enumerate(cfg['moons']):
                    mt = p_obj["moons_t"][i]
                    mx, my = rotasi_titik(moon_cfg['dist'], 0, sudut_global * moon_cfg['speed'])
                    mt.goto(px + mx, py + my)

            # --- 2. UPDATE SATELIT (REALISTIS) ---
            # Satelit mengorbit Bumi
            sat_dx, sat_dy = rotasi_titik(satelit_data["jarak"], 0, satelit_data["angle"])
            
            # Posisi Akhir = Posisi Bumi + Offset Orbit Satelit
            t_satelit.goto(bumi_x + sat_dx, bumi_y + sat_dy)
            
            # Agar terlihat menghadap ke Bumi
            t_satelit.setheading(satelit_data["angle"] + 90) 
            
            # Update sudut satelit
            satelit_data["angle"] += satelit_data["speed"]

            # --- 3. RENDER ---
            screen.update()
            sudut_global += 0.5
            time.sleep(0.02)

    except turtle.Terminator:
        print("Selesai.")

if __name__ == "__main__":
    main()