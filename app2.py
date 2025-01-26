import streamlit as st
from yt_dlp import YoutubeDL
import os

st.image("youtube.png", width=150)

# Define o título do aplicativo
st.title("YouTube Downloader")

# Adiciona uma breve descrição
st.markdown("Insira o link para fazer o download do vídeo.")

# Entrada para o link do vídeo
url = st.text_input("Insira o link do vídeo")

# Botão de download
if st.button("Download"):
    # Garante que o diretório "download" exista
    if not os.path.exists("download"):
        os.makedirs("download")
    
    # Opções de configuração para o downloader
    ydl_opts = {
        'format': 'best',  # Baixa o melhor formato único disponível (áudio e vídeo juntos)
        'outtmpl': os.path.join("download", '%(title)s.%(ext)s'),  # Local e nome do arquivo
        'noplaylist': True,  # Baixa apenas o vídeo individual
        'quiet': False       # Mostra mensagens detalhadas no console
    }
    
    # Executa o download
    with YoutubeDL(ydl_opts) as ydl:
        st.info("Baixando...")
        try:
            ydl.download([url])
            st.success("Download concluído!")
        except Exception as e:
            st.error(f"Erro ao baixar o vídeo: {e}")
