import os

# Ganti ke path folder tempat gambarnya
folder_path = 'D:\\software\\UtekAI\\Dataset\\Bahan\\BawangMerah'  # <-- ubah ini ke folder kamu
prefix_baru = 'Bawang_Merah_'  # nama awal baru untuk file
ekstensi = ['.jpg', '.jpeg', '.png']  # file yang mau diganti namanya

def rename_images(path, prefix):
    files = os.listdir(path)
    gambar = [f for f in files if os.path.splitext(f)[1].lower() in ekstensi]

    for i, file in enumerate(gambar, start=1):
        ekst = os.path.splitext(file)[1]
        nama_baru = f"{prefix}{i}{ekst}"
        os.rename(os.path.join(path, file), os.path.join(path, nama_baru))
        print(f"{file} -> {nama_baru}")

    print("✅ Semua gambar berhasil di-rename!")

# Panggil fungsi
rename_images(folder_path, prefix_baru)
