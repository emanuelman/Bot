import os
import shutil
import time
from temp_prompts import titulo_prompt, introducao_prompt, prompt_primeiro_paragrafo, prompt_segundo_paragrafo, prompt_terceiro_paragrafo, prompt_quarto_paragrafo, finalizacao_prompt, ideias_prompt
from inspects import xpath_textarea, class_response_div
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu") # Adicionando a opção para desabilitar a GPU
profile = "/home/octal_chmod777/.config/google-chrome/Profile 3"
options.add_argument(f"user-data-dir={profile}")
driver = uc.Chrome(options=options, use_subprocess=True)
url = "https://poe.com/ChatGPT"
driver.get(url)
time.sleep(5)

def send_question(question):
    timeout = 60
    wait = WebDriverWait(driver, timeout)
    response_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))

    chat_input_element = driver.find_element(By.XPATH, xpath_textarea)
    chat_input_element.send_keys(question)

    chat_input_element.send_keys(Keys.ENTER)

    time.sleep(30)

    response_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_response_div)))

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
    send_question(prompt)

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

with open("resposta.py", "w") as arquivo:
    for chave, valor in respostas.items():
        arquivo.write(f"{chave} = {valor}\n")

print("O arquivo resposta.py foi criado com sucesso!")

time.sleep(1000)
driver.quit()

