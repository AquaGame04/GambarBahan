import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import { getFirestore, collection, getDocs } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";

// 👉 Ganti dengan config project Firebase kamu
const firebaseConfig = {
    apiKey: "AIzaSyA_s-QXqEZo6h40ZmOUFXJghn8Yw_B4RNw",
    authDomain: "resepmakananenak-fee3d.firebaseapp.com",
    projectId: "resepmakananenak-fee3d",
    storageBucket: "resepmakananenak-fee3d.firebasestorage.app",
    messagingSenderId: "701844805728",
    appId: "1:701844805728:web:ed5e32fe22c7608ef7cb05",
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// 🔽 Ambil subkoleksi dari dokumen "Telur"
const imageContainer = document.getElementById("image-container");

async function loadImages() {
  const querySnapshot = await getDocs(collection(db, "Bahan", "Telur", "image"));
  querySnapshot.forEach((doc) => {
    const data = doc.data();
    const img = document.createElement("img");
    img.src = data.image_url;
    img.alt = data.name || "Bahan gambar";
    img.style.width = "150px";
    img.style.margin = "10px";
    imageContainer.appendChild(img);
  });
}

loadImages();
