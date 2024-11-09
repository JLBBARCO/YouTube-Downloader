import yt_dlp
import os

def baixar_video(url, format):
    caminho_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(caminho_downloads, '%(title)s.%(ext)s'),
    }
    
    if format == 'mp3':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f'Download concluído! O vídeo foi salvo em: {caminho_downloads}')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
