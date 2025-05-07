📂 Sortify – Organizador de Arquivos Automatizado
Sortify é um sistema de automação para organização de arquivos em pastas, desenvolvido em Python. Ideal para uso pessoal ou empresarial, ele classifica e move arquivos automaticamente com base em sua extensão ou categoria definida.

🎯 Objetivo
Facilitar a rotina de organização de arquivos em diretórios, seja no computador pessoal ou em ambientes corporativos.
O sistema pode ser adaptado para rodar automaticamente via agendador de tarefas (como o Agendador do Windows).

🛠️ Tecnologias Utilizadas
🐍 Python 3

📁 Módulo os e shutil (manipulação de arquivos)

⏲️ Suporte para automação via agendadores

🚀 Funcionalidades

🔍 Varre uma pasta-alvo em busca de arquivos

📦 Move arquivos automaticamente para pastas organizadas por:

Tipo/extensão (PDF, PNG, EXE, etc.)

Nome personalizado ou categoria

🔁 Pode ser executado de forma recorrente (manual ou automatizada)

📂 Estrutura do Projeto
Sortify/
│
├── sortify.py           → Script principal de organização
├── config.json (opcional) → Arquivo de configuração de pastas/categorias
├── /destinos            → Pastas de destino (podem ser criadas dinamicamente)
▶️ Como Usar

💡 Exemplo de Organização
Um arquivo documento.pdf na pasta "Downloads" será automaticamente movido para:

/Downloads/Organizados/PDFs/documento.pdf
Outros exemplos:

.exe → Pasta "Executáveis"

.png, .jpg → Pasta "Imagens"

.mp3, .wav → Pasta "Áudios"

🧠 Autor
Henrique Liuti
Estudante de Ciência da Computação – 2º ano
LinkedIn

📜 Licença
Este projeto é open-source para fins educacionais e comerciais simples.
Você pode adaptá-lo para uso pessoal ou como serviço para empresas.
