# controle_gastos.py
import csv
from collections import defaultdict

def ler_gastos(arquivo_csv):
    categorias = defaultdict(float)
    total = 0.0

    try:
        with open(arquivo_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                categoria = row["categoria"]
                valor = float(row["valor"])
                categorias[categoria] += valor
                total += valor

        print("📊 Relatório de Gastos:")
        for cat, valor in categorias.items():
            print(f"  {cat}: R$ {valor:.2f}")
        print(f"\n💰 Total: R$ {total:.2f}")

    except Exception as e:
        print(f"❌ Erro ao ler o arquivo: {e}")

# Exemplo de uso:
# ler_gastos("gastos.csv")