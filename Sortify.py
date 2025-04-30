import os
import shutil
import requests
import sys

# ===== VERIFICAÇÃO DE LICENÇA =====
def verificar_licenca(alvaz):
    try:
        url = f"https://licencas-api.onrender.com/verificar_licenca?cliente={alvaz}"
        resposta = requests.get(url, timeout=5)
        status = resposta.json().get("status")

        if status != "ativo":
            print("Licença inativa. Encerrando...")
            sys.exit()
    except Exception as e:
        print(f"Erro ao verificar licença: {e}")
        sys.exit()

# Defina o ID do cliente
cliente_id = "alvaz"  # Alterar para cada cliente
verificar_licenca(cliente_id)

# ===== ORGANIZAÇÃO DE ARQUIVOS =====
pasta_origem = "C:/Users/hickl/Downloads"
pasta_destino = "C:/Users/hickl/Downloads/ORGANIZER"

# Tipos de arquivos
tipos = ['pdf', 'jpg', 'docx', 'xlsx', 'outros']
for tipo in tipos:
    os.makedirs(os.path.join(pasta_destino, tipo), exist_ok=True)

# Organiza os arquivos
for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)
    if os.path.isfile(caminho_arquivo):
        extensao = arquivo.split('.')[-1].lower()
        destino = os.path.join(pasta_destino, extensao if extensao in tipos else 'outros')
        shutil.move(caminho_arquivo, os.path.join(destino, arquivo))

print("Organização concluída!")
