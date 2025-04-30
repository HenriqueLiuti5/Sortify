import os
import shutil
import requests
import sys
from datetime import datetime

# ===== VERIFICAÇÃO DE LICENÇA =====
def verificar_licenca(salomon):
    try:
        url = f"https://licencas-api.onrender.com/verificar_licenca?cliente={salomon}"
        resposta = requests.get(url, timeout=5)
        status = resposta.json().get("status")

        if status != "ativo":
            print("Licença inativa. Encerrando...")
            sys.exit()
    except Exception as e:
        print(f"Erro ao verificar licença: {e}")
        sys.exit()

# Defina o ID do cliente
cliente_id = "salomon"  # Alterar para cada cliente
verificar_licenca(cliente_id)

# ===== ORGANIZAÇÃO DE ARQUIVOS =====
pasta_origem = "C:/Sortify/ORIGEM"
pasta_destino = "C:/Sortify/DESTINO"

# Organiza os arquivos por ano e mês
for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)
    if os.path.isfile(caminho_arquivo):
        # Obter a data de modificação do arquivo (mês e ano)
        data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho_arquivo))
        ano_mes = data_modificacao.strftime("%Y-%m")  # Formato: "2025-04"
        
        # Criação da pasta de destino com o ano e mês
        pasta_ano_mes = os.path.join(pasta_destino, ano_mes)
        os.makedirs(pasta_ano_mes, exist_ok=True)
        
        # Mover o arquivo para a pasta correspondente
        shutil.move(caminho_arquivo, os.path.join(pasta_ano_mes, arquivo))

print("Organização concluída!")
