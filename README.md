<p align="center">
  <img src="https://img.icons8.com/papercut/120/video-file.png" width="80" alt="Video Logo">
</p>

# Video Sosmed Downloader Offline

Aplikasi web sederhana buat download video atau audio dari YouTube dan TikTok secara instan lewat browser. Begitu link dimasukkan dan ditekan enter, aplikasi langsung memproses unduhan secara lokal dan otomatis mengunggah hasilnya ke GoFile untuk menghasilkan link unduhan yang siap didownload

Aplikasi ini dibangun menggunakan Gradio sebagai antarmuka web, serta library yt-dlp untuk menangani proses pengunduhan videonya

## Fitur Utama

- Proses otomatis dengan menekan enter tanpa tombol submit, tinggal tempel link dan tunggu hasilnya
- Mendukung dua platform besar sekaligus: YouTube dan TikTok
- Pilihan format hasil konversi fleksibel antara MP3 audio atau MP4 video lengkap dengan suara
- Hasil download bisa disimpan langsung ke komputer atau dibagikan lewat link cloud GoFile

## Cara Kerja Sistem

1. Pengguna memilih platform tujuan dan format hasil yang diinginkan pada halaman web
2. Link video YouTube atau TikTok dimasukkan ke dalam kolom input yang tersedia
3. Pengguna menekan tombol enter untuk memicu fungsi pengunduhan secara lokal melalui komputer
4. Setelah file video berhasil didownload, aplikasi meminta server GoFile untuk menyiapkan slot penyimpanan
5. File tersebut diunggah ke cloud dan sistem mengembalikan link unduhan secara instan

## Persyaratan Sistem

Pastikan Python sudah terinstal di komputer Anda Selain itu aplikasi ini membutuhkan beberapa library tambahan yang bisa dipasang lewat pip

```bash
pip install -r requirements.txt
```

Habistuh sudah tinggal
```bash
Python3 app.py
```

Selamat Mencoba!
