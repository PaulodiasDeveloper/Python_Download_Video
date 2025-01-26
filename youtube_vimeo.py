import streamlit as st
from yt_dlp import YoutubeDL
import os

# Criando duas colunas
col1, col2 = st.columns(2)

# Exibindo as imagens com a mesma largura e espaço no topo
with col1:
    st.markdown('<div style="margin-top: 20px;">', unsafe_allow_html=True)
    st.image("youtube.png", width=150)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div style="margin-top: 60px;">', unsafe_allow_html=True)
    st.image("vimeo.png", width=150)
    st.markdown('</div>', unsafe_allow_html=True)

# Define o título do aplicativo
st.title("Downloader de Vídeos")

# Adiciona uma breve descrição
st.markdown("Escolha a plataforma e insira o link para fazer o download do vídeo.")

# Seleção da plataforma
platform = st.selectbox("Escolha a plataforma Youtube ou Vimeo", ["YouTube", "Vimeo"])

# Entrada para o link do vídeo
url = st.text_input("Insira o link do vídeo")

# Botão de download
if st.button("Download"):
    if not url.strip():
        st.error("Por favor, insira um link válido.")
    else:
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
            st.info(f"Baixando do {platform}...")
            try:
                ydl.download([url])
                st.success("Download concluído!")
            except Exception as e:
                st.error(f"Erro ao baixar o vídeo: {e}")
