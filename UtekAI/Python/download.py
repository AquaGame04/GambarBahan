import os
import requests
from duckduckgo_search import DDGS
from PIL import Image
from io import BytesIO

# Lokasi root proyek kamu
project_root = "D:\\software\\UtekAI\\Dataset\\Bahan"
images_dir = os.path.join(project_root, "UtekAI", "Dataset", "Bahan")
os.makedirs(images_dir, exist_ok=True)

# Daftar bahan yang mau dicari
ingredients = [
    "bayam", "kangkung", "sawi hijau", "kubis", "wortel", "kentang", "tomat",
    "mentimun", "terong", "buncis", "kacang panjang", "brokoli", "labu siam",
    "jagung manis", "oyong", "daun singkong", "pare", "petai", "jengkol",
    "cabai merah", "paprika", "tauge", "lobak", "selada"
]

# Jumlah gambar per bahan
num_images = 50

def download_images_for_ingredient(ingredient):
    safe_name = ingredient.replace(" ", "_").lower()
    save_dir = os.path.join(images_dir, safe_name)
    os.makedirs(save_dir, exist_ok=True)
    count = 0

    with DDGS() as ddgs:
        for r in ddgs.images(f"{ingredient} bahan makanan", max_results=num_images):
            try:
                response = requests.get(r["image"], timeout=10)
                if response.status_code == 200:
                    image = Image.open(BytesIO(response.content)).convert("RGB")
                    image = image.resize((224, 224))
                    image.save(os.path.join(save_dir, f"{safe_name}_{count}.jpg"))
                    count += 1
                if count >= num_images:
                    break
            except Exception as e:
                continue

    print(f"[✅] {count} gambar berhasil diunduh untuk: {ingredient}")

# Jalankan untuk semua bahan
for ingredient in ingredients:
    print(f"[⬇] Downloading: {ingredient}")
    download_images_for_ingredient(ingredient)