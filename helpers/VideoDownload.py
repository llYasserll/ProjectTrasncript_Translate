import yt_dlp

def downloadVideo(url):
    ydl_opts = {
        "format": "bestvideo[height<=1080]+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": "video_1080p.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def downloadAudio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(title)s.%(ext)s',  # Guarda el archivo con el nombre del video
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def downloadVideoWithoutAudio(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4][vcodec!=none][acodec=none]',
        'outtmpl': '%(title)s.%(ext)s',  # Guarda con el nombre del video
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])