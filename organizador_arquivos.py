# organizador_arquivos.py
import os
import shutil

PASTA_ORIGEM = os.path.expanduser("~/Downloads")
PASTA_DESTINO = os.path.expanduser("~/Organizado")

tipos = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Vídeos": [".mp4", ".avi", ".mov", ".mkv"],
    "Áudios": [".mp3", ".wav", ".aac"],
    "Compactados": [".zip", ".rar", ".7z"]
}

os.makedirs(PASTA_DESTINO, exist_ok=True)

for nome_pasta in tipos.keys():
    os.makedirs(os.path.join(PASTA_DESTINO, nome_pasta), exist_ok=True)

for arquivo in os.listdir(PASTA_ORIGEM):
    caminho = os.path.join(PASTA_ORIGEM, arquivo)
    if os.path.isfile(caminho):
        _, ext = os.path.splitext(arquivo.lower())
        for pasta, extensoes in tipos.items():
            if ext in extensoes:
                destino = os.path.join(PASTA_DESTINO, pasta, arquivo)
                try:
                    shutil.move(caminho, destino)
                    print(f"✅ Movido: {arquivo} → {pasta}")
                except Exception as e:
                    print(f"❌ Erro ao mover {arquivo}: {e}")
                break