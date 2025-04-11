import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
import {
  getFirestore,
  collection,
  getDocs,
} from "https://www.gstatic.com/firebasejs/10.10.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyA_s-QXqEZo6h40ZmOUFXJghn8Yw_B4RNw",
  authDomain: "resepmakananenak-fee3d.firebaseapp.com",
  projectId: "resepmakananenak-fee3d",
  storageBucket: "resepmakananenak-fee3d.appspot.com",
  messagingSenderId: "701844805728",
  appId: "1:701844805728:web:ed5e32fe22c7608ef7cb05"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const imageContainer = document.getElementById("imageContainer");
const bahanSelect = document.getElementById("bahanSelect");
const reloadBtn = document.getElementById("reloadBtn");

async function loadImages(namaGroup, namaBahan) {
  imageContainer.innerHTML = "⏳ Loading...";

  const linkRef = collection(db, "BahanMakanan", "BahanAja", namaGroup, namaBahan, "Link");

  try {
    const snapshot = await getDocs(linkRef);
    imageContainer.innerHTML = "";

    if (snapshot.empty) {
      imageContainer.innerHTML = "😢 Ga ada gambar di koleksi ini.";
      return;
    }

    snapshot.forEach((doc) => {
      const data = doc.data();
      const img = document.createElement("img");
      img.src = data.url;
      img.alt = "gambar bahan";
      img.style.width = "200px";
      img.style.margin = "10px";
      imageContainer.appendChild(img);
    });

  } catch (err) {
    console.error(err);
    imageContainer.innerHTML = "❌ Error ambil gambar.";
  }
}

// 🎯 Event: klik tombol reload
reloadBtn.addEventListener("click", () => {
  const selectedValue = bahanSelect.value; // Format: Group|Bahan
  const [group, bahan] = selectedValue.split("|");
  loadImages(group, bahan);
});

// Auto load default pas pertama kali
loadImages("TelurGroup", "Telur");
