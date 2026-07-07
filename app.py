import os
import json
import urllib.request
from pathlib import Path
import gradio as gr
import yt_dlp

def upload_to_cloud(file_path):
    file_path = Path(file_path)
    try:
        server_req = urllib.request.Request("https://api.gofile.io/servers", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(server_req) as response:
            server_data = json.loads(response.read().decode('utf-8'))
            if server_data["status"] == "ok":
                server_name = server_data["data"]["servers"][0]["name"]
            else:
                raise Exception("Gagal mendapatkan server GoFile")

        upload_url = f"https://{server_name}.gofile.io/contents/uploadfile"
        boundary = "----WebKitFormBoundaryGofileUpload"
        
        with open(file_path, "rb") as f:
            file_data = f.read()
            
        parts = [
            b'--' + boundary.encode('utf-8'),
            b'Content-Disposition: form-data; name="file"; filename="' + file_path.name.encode('utf-8') + b'"',
            b'Content-Type: application/octet-stream',
            b'',
            file_data,
            b'--' + boundary.encode('utf-8') + b'--',
            b''
        ]
        
        body = b'\r\n'.join(parts)
        req = urllib.request.Request(upload_url, data=body)
        req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')
        req.add_header('User-Agent', 'Mozilla/5.0')
        
        with urllib.request.urlopen(req) as response:
            upload_data = json.loads(response.read().decode('utf-8'))
            if upload_data["status"] == "ok":
                return upload_data["data"]["downloadPage"]
            else:
                raise Exception(upload_data.get("status", "Gagal upload"))
    except Exception as e:
        raise Exception(f"Gagal upload ke GoFile: {str(e)}")

def download_video(platform, url, mode):
    if not url.strip():
        return "Silakan masukkan link videonya terlebih dahulu", None

    output_dir = Path("downloads")
    output_dir.mkdir(exist_ok=True)

    ydl_opts = {
        'outtmpl': str(output_dir / '%(title)s.%(ext)s'),
        'quiet': True,
    }

    if platform == "TikTok":
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'extractor_args': {'tiktok': {'web_api': ['true']}}
        })
    else:
        if mode == "MP3 (Audio saja)":
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:
            ydl_opts.update({
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            if platform != "TikTok" and mode == "MP3 (Audio saja)":
                file_path = Path(filename).with_suffix(".mp3")
            else:
                file_path = Path(filename)

        if not file_path.exists():
            return "File hasil download tidak ditemukan", None

        try:
            cloud_url = upload_to_cloud(file_path)
            status_msg = f"Oke video berhasil didownload\n\n Link Cloud (GoFile):\n{cloud_url}"
        except Exception as e:
            status_msg = f"Download lokal sukses tapi gagal upload ke cloud: {str(e)}"

        return status_msg, str(file_path)

    except Exception as e:
        return f"Gagal memproses video atau link tidak valid: {str(e)}", None

def update_mode_options(platform):
    if platform == "TikTok":
        return gr.update(choices=["MP4 (Video + Audio)"], value="MP4 (Video + Audio)")
    return gr.update(choices=["MP3 (Audio saja)", "MP4 (Video + Audio)"], value="MP4 (Video + Audio)")

video_theme = gr.themes.Default(
    primary_hue="red",
    secondary_hue="red",
    neutral_hue="slate",
).set(
    body_background_fill="#0f0f0f",
    body_text_color="#ffffff",
    block_background_fill="#212121",
    block_label_text_color="#aaaaaa",
    input_background_fill="#121212",
    button_primary_background_fill="#ff0000",
    button_primary_background_fill_hover="#cc0000",
    button_primary_text_color="#ffffff"
)

with gr.Blocks(title="Social Media Downloader", theme=video_theme) as demo:
    gr.Markdown("# Social Media Downloader Instan")
    gr.Markdown("Sistem download aman berjalan lewat komputer kamu dan langsung upload cloud otomatis")
    
    platform_input = gr.Radio(
        choices=["YouTube", "TikTok"],
        value="YouTube",
        label="Pilih Platform"
    )
    
    mode_input = gr.Radio(
        choices=["MP3 (Audio saja)", "MP4 (Video + Audio)"], 
        value="MP4 (Video + Audio)", 
        label="Pilih Format Hasil"
    )
    
    url_input = gr.Textbox(
        label="Masukkan Link Video", 
        placeholder="Tempel link di sini lalu tekan Enter untuk langsung mendownload"
    )
    
    status_output = gr.Textbox(label="Status & Link Cloud", interactive=False)
    file_output = gr.Video(label="Hasil Download")
    
    platform_input.change(
        fn=update_mode_options,
        inputs=[platform_input],
        outputs=[mode_input]
    )
    
    url_input.submit(
        fn=download_video, 
        inputs=[platform_input, url_input, mode_input], 
        outputs=[status_output, file_output]
    )

if __name__ == "__main__":
    demo.launch()