import requests
from bs4 import BeautifulSoup
import pyperclip

# Target GitHub URL
github_url = "https://github.com/AquaGame04/GambarBahan/tree/main/TelurAyam"

# Ambil isi halaman HTML
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(github_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Ekstensi gambar yang dicari
valid_extensions = [".jpg", ".jpeg"]

# Pakai set biar nggak dobel
image_links = set()

# Cari semua tag <a> yang mengandung link file
for a in soup.find_all("a", href=True):
    href = a['href']
    if "/blob/" in href and any(href.lower().endswith(ext) for ext in valid_extensions):
        # Convert ke raw link
        raw_link = href.replace("/blob", "")
        raw_url = f"https://raw.githubusercontent.com{raw_link}"
        image_links.add(raw_url.strip())

# Gabung jadi satu teks
result = "\n".join(sorted(image_links))  # Optional: sort biar rapi

# Copy ke clipboard
pyperclip.copy(result)

# Tampilkan hasil
if image_links:
    print("✅ Link gambar (RAW) berhasil di-copy ke clipboard:\n")
    print(result)
else:
    print("❌ Gagal nemuin gambar dengan ekstensi .jpg / .jpeg di repo ini.")
