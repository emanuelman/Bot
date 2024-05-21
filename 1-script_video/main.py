import os
import time
from library import *

# Diretório para salvar o arquivo script_video.py
diretorio_script_video = "~/Desktop/project_youtube_channel/saborarte_namesa/Bot/2-audio_video"

profile = "/home/octal_chmod777/.config/google-chrome/Profile 1"
url = "https://poe.com/ChatGPT"
driver = setup_driver(profile)

driver.get(url)
time.sleep(5)

prompts = [
    titulo_prompt,
    introducao_prompt,
    prompt_primeiro_paragrafo,
    prompt_segundo_paragrafo,
    prompt_terceiro_paragrafo,
    prompt_quarto_paragrafo,
    finalizacao_prompt,
]

respostas = {}

# Mapeamento de prompts para variáveis
prompt_variavel_map = {
    titulo_prompt: "titulo",
    introducao_prompt: "introducao",
    prompt_primeiro_paragrafo: "primeiro_paragrafo",
    prompt_segundo_paragrafo: "segundo_paragrafo",
    prompt_terceiro_paragrafo: "terceiro_paragrafo",
    prompt_quarto_paragrafo: "quarto_paragrafo",
    finalizacao_prompt: "finalizacao",
}

for prompt in prompts:
    send_question(driver, prompt)

    # Obter todas as divs de resposta
    message_divs = driver.find_elements(By.CLASS_NAME, class_response_div)

    # Selecionar apenas a última div de resposta
    response_div = message_divs[-1] if message_divs else None

    if response_div:
        # Obter o texto da resposta
        response_text = response_div.text.strip()

        # Determine a variável correspondente ao prompt
        variavel = prompt_variavel_map[prompt]

        # Armazenar a resposta no dicionário de respostas
        respostas[variavel] = f'"""{response_text}"""'
    else:
        print("Nenhuma resposta encontrada para o prompt:", prompt)

# Caminho completo para o arquivo script_video.py
caminho_script_video = os.path.join(diretorio_script_video, "script_video.py")

# Verificar se o diretório existe e criar, se necessário
if not os.path.exists(diretorio_script_video):
    os.makedirs(diretorio_script_video)

with open(caminho_script_video, "w") as arquivo:
    for chave, valor in respostas.items():
        arquivo.write(f"{chave} = {valor}\n")

print("O arquivo script_video.py foi criado com sucesso!")

time.sleep(1000)
driver.quit()

