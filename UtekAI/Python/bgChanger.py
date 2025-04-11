import cv2
import numpy as np
import os

# Folder input dan output
input_folder = "..\\Dataset\\Bahan\\DagingSapi"
output_folder = "..\\Dataset\\Bahan\\TelurAyam\\noBG"

# Bikin folder output kalau belum ada
os.makedirs(output_folder, exist_ok=True)

# Loop semua file di folder
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(input_folder, filename)
        img = cv2.imread(path)

        # Konversi ke HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Deteksi warna putih
        lower_white = np.array([0, 0, 200])
        upper_white = np.array([180, 30, 255])
        mask = cv2.inRange(hsv, lower_white, upper_white)
        mask_inv = cv2.bitwise_not(mask)

        # Hapus background putih (jadi hitam)
        result = cv2.bitwise_and(img, img, mask=mask_inv)

        # Simpan hasil
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, result)

        print(f"✅ {filename} selesai!")

print("🔥 Semua gambar udah diproses!")
