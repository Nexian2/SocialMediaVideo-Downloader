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

==========================================================================================

```markdown
<p align="center">
  <img src="https://img.icons8.com/papercut/120/video-file.png" width="80" alt="Video Logo">
</p>

# Video Social Media Downloader Offline

A simple web app to download video or audio from YouTube and TikTok instantly right from your browser. Once you paste the link and hit enter, it processes the download locally and automatically uploads the result to GoFile to generate a ready-to-share download link

This app is built using Gradio for the web interface, along with the yt-dlp library to handle the video downloading process under the hood

## Key Features

- Fully automated process by pressing enter with no submit button needed, just paste the link and wait for the result
- Supports two major platforms at once: YouTube and TikTok
- Flexible output format options between MP3 audio or MP4 video with full audio support
- Downloaded files can be saved directly to your computer or shared via GoFile cloud link

## How It Works

1. Select the target platform and desired output format on the web page
2. Paste your YouTube or TikTok video link into the available input field
3. Press enter to trigger the local downloading process through your computer
4. Once downloaded, the app requests the GoFile server to prepare a storage slot
5. The file is uploaded to the cloud and the system returns the download link instantly

## System Requirements

Make sure Python is already installed on your computer Other than that, this app requires a few extra libraries that can be installed via pip

```bash
pip install -r requirements.txt
```

And then, you must type

```bash
Python3 app.py
```

Good luck!