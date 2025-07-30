# Script: faz backup de fotos da pasta Downloads
# backup_fotos.py
# Automação para o Bem
# Script simples para mover fotos da pasta Downloads para Backup/Fotos
# Feito por Fábio de Lima - 2025

import os
import shutil
from datetime import datetime

# Configurações
PASTA_DOWNLOADS = os.path.expanduser("~/Downloads")
PASTA_BACKUP = os.path.expanduser("~/Backup/Fotos")

# Extensões de imagem suportadas
EXTENSOES = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}

def criar_pasta_se_nao_existir(caminho):
    """Cria a pasta se ela não existir."""
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        print(f"Pasta criada: {caminho}")

def obter_arquivos_de_fotos(pasta_origem):
    """Retorna lista de arquivos de imagem na pasta."""
    arquivos = []
    for arquivo in os.listdir(pasta_origem):
        caminho = os.path.join(pasta_origem, arquivo)
        if os.path.isfile(caminho):
            _, ext = os.path.splitext(arquivo.lower())
            if ext in EXTENSOES:
                arquivos.append(arquivo)
    return arquivos

def copiar_fotos_para_backup():
    """Copia as fotos encontradas para a pasta de backup."""
    print("🔍 Procurando fotos na pasta Downloads...")

    arquivos_fotos = obter_arquivos_de_fotos(PASTA_DOWNLOADS)

    if not arquivos_fotos:
        print("✅ Nenhuma foto encontrada para fazer backup.")
        return

    criar_pasta_se_nao_existir(PASTA_BACKUP)

    fotos_copiadas = 0
    for arquivo in arquivos_fotos:
        origem = os.path.join(PASTA_DOWNLOADS, arquivo)
        destino = os.path.join(PASTA_BACKUP, arquivo)

        # Evita sobrescrita adicionando timestamp se necessário
        if os.path.exists(destino):
            nome, ext = os.path.splitext(arquivo)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            destino = os.path.join(PASTA_BACKUP, f"{nome}_{timestamp}{ext}")

        try:
            shutil.copy2(origem, destino)
            print(f"📎 Copiado: {arquivo}")
            fotos_copiadas += 1
        except Exception as e:
            print(f"❌ Erro ao copiar {arquivo}: {e}")

    print(f"\n✅ Backup concluído! {fotos_copiadas} foto(s) copiada(s) para {PASTA_BACKUP}")

if __name__ == "__main__":
    print(f"🚀 Iniciando backup de fotos - {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    copiar_fotos_para_backup()
    print("🎉 Processo finalizado.")