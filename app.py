import yt_dlp

# Link do vídeo ou live do YouTube
link = "https://www.youtube.com/live/54tlAFyp3HM?si=jfD87kK6qSK_ZNio"

# Opções de configuração para o downloader
ydl_opts = {
    'format': 'best',         # Baixa o melhor formato único disponível (áudio e vídeo juntos)
    'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo com o título do vídeo
    'noplaylist': True,       # Baixa apenas o vídeo individual, não uma playlist
    'quiet': False            # Mostra mensagens detalhadas no console
}

# Executa o download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])