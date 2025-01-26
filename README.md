# Downloader de Vídeos - YouTube e Vimeo

Este é um aplicativo simples criado com o Streamlit que permite o download de vídeos diretamente de plataformas como YouTube e Vimeo.

## Requisitos

Antes de rodar o aplicativo, certifique-se de ter os seguintes pacotes instalados:

- Python 3.x
- streamlit
- yt-dlp

Você pode instalar os pacotes necessários com o seguinte comando:


pip install streamlit yt-dlp
## Como Usar
1. Clone o repositório ou baixe os arquivos do projeto.
2. Coloque as imagens youtube.png e vimeo.png na pasta do projeto.
3. Execute o aplicativo Streamlit com o comando:

```bash
streamlit run app.py
```

O aplicativo abrirá em seu navegador padrão. Escolha a plataforma (YouTube ou Vimeo) e insira o link do vídeo que deseja baixar. Clique no botão Download para iniciar o processo de download. O vídeo será salvo na pasta download com o nome do título do vídeo.

## Funcionalidades
- Selecione a plataforma: YouTube ou Vimeo.
- Insira o link do vídeo.
- Baixe o vídeo diretamente para o seu computador.
- A pasta <mark style="background-color:rgb(114, 113, 113); color: white;">download</mark> será criada automaticamente se não existir.

## Como Funciona
O aplicativo utiliza a biblioteca <mark style="background-color:rgb(114, 113, 113); color: white;">yt-dlp</mark> para realizar o download do vídeo. O código define algumas opções de configuração, como:

- Baixar o melhor formato de vídeo disponível (vídeo e áudio juntos).
- Salvar o vídeo na pasta <mark style="background-color:rgb(114, 113, 113); color: white;">download</mark> com o título do vídeo.
- Baixar apenas o vídeo individual (sem playlists).

![Image](https://github.com/user-attachments/assets/099258f7-8f23-440b-a1cd-108a7effdcbb)

![Image](https://github.com/user-attachments/assets/f1f655c8-8d17-46b8-9eb9-916c62be653c)

## Contribuindo
Se você deseja contribuir com melhorias ou correções para o projeto, fique à vontade para fazer um fork e enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.# Python_Download
