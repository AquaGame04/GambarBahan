import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
import { getFirestore, collection, addDoc, doc } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-firestore.js";

// Konfigurasi Firebase
const firebaseConfig = {
  apiKey: "AIzaSyA_s-QXqEZo6h40ZmOUFXJghn8Yw_B4RNw",
  authDomain: "resepmakananenak-fee3d.firebaseapp.com",
  projectId: "resepmakananenak-fee3d",
  storageBucket: "resepmakananenak-fee3d.appspot.com",
  messagingSenderId: "701844805728",
  appId: "1:701844805728:web:ed5e32fe22c7608ef7cb05"
};

// Inisialisasi Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore();

document.getElementById('uploadBtn').addEventListener('click', async () => {
  const text = document.getElementById('linkInput').value;
  const links = text.split('\n').map(link => link.trim()).filter(link => link);

  // Ini struktur path yang benar
  const bahanRef = doc(db, "BahanMakanan", "BahanAja");
  const telurGroupRef = collection(bahanRef, "BawangMGroup");
  const telurDocRef = doc(telurGroupRef, "BawangMerah");
  const linkCollectionRef = collection(telurDocRef, "Link");

  for (const link of links) {
    await addDoc(linkCollectionRef, {
      url: link,
      timestamp: new Date(),
    });
  }

  alert('✅ Semua link udah di-upload ke Firestore!');
});
