# PoC - Hexahue Bergerak

Mengektsrak suatu teks secara otomatis dari hexahue yang diberikan sebagai GIF, yang dimana 1 frame = 1 karakter (2x3).

## TLDR
Input : `HCS.gif` animated GIF berisi 2x3 kotak dengan 6 warna

Proses :
1. Baca semua frame
2. Untuk tiap frame
   - konversi ke RGB
   - bagi gambar menjadi 2 kolom x 3 baris
   - bentuk tuple 6 warna
3. Cocokkan tuple warna frame terhadap dictionary Hexahue
4. Gabungkan semua karakter dari semua frame menjadi teks akhir

Proses diharapkan menggunakan solver otomatis, karena ada ~468 frame jadi kalo di decode manual kelamaan

---
flag :
`HCS{woah.hexahue.adalah.alfabet.berwarna.c0y}`