# Importacoes de bibliotecas para auxiliar na automação do navegador, manipulação de arquivos e parsing de HTML.
import time
import os
import shutil
import json
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Importacao da biblioteca de inspects
from inspects import *
from training import *
from script_video import *

# Função para configurar e retornar uma instância do driver do Chrome.
def setup_driver(profile):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"user-data-dir={profile}")
    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver

def send_question(driver, question):
    timeout = 60
    wait = WebDriverWait(driver, timeout)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(4)

    # Espera até que o elemento esteja presente na página
    response_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))
    chat_input_element = driver.find_element(By.XPATH, xpath_textarea)

    # Limpar o campo de entrada antes de enviar a pergunta
    #chat_input_element.clear()

    # Enviar a pergunta completa para o chat
    chat_input_element.send_keys(question)

    # Aguardar um momento
    time.sleep(5)

def div_number():
    url_ideas_initial_number = 3
    url_prompts_initial_number = 9
    url_ideas_xpath_last_response_div = f'//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[2]/div[{url_ideas_initial_number}]/div[2]/div[2]/div[2]/div/div[1]/div'
    url_prompts_xpath_last_response_div = f'//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[2]/div[{url_prompts_initial_number}]/div[2]/div[2]/div[2]/div/div[1]/div'

    return url_ideas_xpath_last_response_div, url_prompts_xpath_last_response_div

def get_response(driver):
    timeout = 60
    wait = WebDriverWait(driver, timeout)

    response_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))
    chat_input_element = driver.find_element(By.XPATH, xpath_textarea)

    # Enviar a pergunta pressionando a tecla Enter
    time.sleep(5)  # Espera um pouco antes de enviar a pergunta para evitar conflitos
    chat_input_element.send_keys(Keys.ENTER)

    time.sleep(22)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(4)

    # Encontrar o número máximo de divs de resposta
    response_divs = driver.find_elements(By.CLASS_NAME, class_response_div)
    max_number = 2
    max_number += len(response_divs)

    # Construir o XPath da última div de resposta com base no número máximo encontrado
    xpath_last_response_div = f'//*[@id="__next"]/div/div[1]/div/main/div/div/div/div[2]/div[{max_number}]/div[2]/div[2]/div[2]/div/div[1]/div'

    print(xpath_last_response_div)
    
    # Encontrar a última div de resposta
    last_response_div = wait.until(EC.presence_of_element_located((By.XPATH, xpath_last_response_div)))
        
    # Obter o texto da última div de resposta
    response_text = last_response_div.text.strip()

    # Reinicializar max_number para None
    max_number = None

    return response_text

def create_chat_and_train_with_json_files(driver, url_ideas, url_prompt, json_padrao_luminosidade, json_paletas_cores_culinaria_doce, json_posicionamento_camera_culinaria_doce, json_prompts_negativos_culinaria_doce, json_prompts_positivos_culinaria_doce):
    # Abrir URL para treinar a AI
    driver.get(url_prompt)
    time.sleep(5)

    # Texto inicial
    initial_text = "Chat, eu vou te fornecer 5 arquivos.json dos quais contém detalhes sobre a geração de imagens por inteligência artificial através de prompts de texto baseado no modelo stable difusion. Vou te treinar através destes arquivos um de cada vez e após você fazer a análise de cada um dos arquivos que eu te fornecer, peço que caso tenha entendido, retorne: 'análise completa'. Caso não entenda algo me retorne: 'análise falhou'. Afirmativo?"

    # Enviar comandos para criar um novo chat
    chat_creation_commands = [
        initial_text,
        json.dumps(json_padrao_luminosidade),
        json.dumps(json_paletas_cores_culinaria_doce),
        json.dumps(json_posicionamento_camera_culinaria_doce),
        json.dumps(json_prompts_negativos_culinaria_doce),
        json.dumps(json_prompts_positivos_culinaria_doce)
    ]

    for command in chat_creation_commands:
        send_question(driver, command)
        get_response(driver)
        time.sleep(5)

    # Atualizar a variável url com o valor atual do site
    url_prompt = driver.current_url
    # Chama a funcao generate_image_prompts_with_existing_chat
    generate_image_prompts_with_existing_chat(driver, url_ideas, url_prompt, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao)

def generate_image_prompts_with_existing_chat(driver, url_ideas, url_prompt, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao):

    driver.get(url_ideas)
    time.sleep(5)

    sugestao = ""

    prompts = [titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao]
    prompts_validos = ["titulo", "introducao", "primeiro_paragrafo", "segundo_paragrafo", "terceiro_paragrafo", "quarto_paragrafo", "finalizacao"]

    def divide_texto(texto):
        tamanho_maximo_parte = 100  # Alterado para usar 100 caracteres como base
        partes = []
        parte_atual = ""
        
        for palavra in texto.split():
            parte_atual += palavra + " "
            if len(parte_atual) >= tamanho_maximo_parte:
                partes.append(parte_atual.strip())
                parte_atual = ""
        
        if parte_atual:
            partes.append(parte_atual.strip())
        
        return partes

    def dividir_prompt_em_partes(prompts):
        prompts_divididos = {}  # Dicionário para armazenar as partes divididas de cada prompt

        for idx, prompt in enumerate(prompts):
            partes_prompt = divide_texto(prompt)  # Dividir o prompt em partes de 100 caracteres
            numero_partes = len(partes_prompt)  # Calcular o número de partes
            # Armazenar as partes divididas em variáveis prompt_A, prompt_B, prompt_C, etc.
            for i, parte in enumerate(partes_prompt):
                chave = f"prompt_{chr(ord('A') + i)}"  # Gerar o nome da variável
                prompts_divididos[chave] = str(parte)  # Armazenar a parte no dicionário

        return prompts_divididos

    for prompt, prompt_valido in zip(prompts, prompts_validos):
        if prompt_valido in locals() and prompt == locals()[prompt_valido]:
            dicionario_prompts = dividir_prompt_em_partes([prompt])
            texto = ("Me dê apenas uma sugestão de imagem para eu colocar nesta parte do meu vídeo no meu canal no YouTube de culinária: ")
            send_question(driver, texto)
            for parte_prompt in dicionario_prompts.values():  # Iterar sobre os valores do dicionário
                pergunta = parte_prompt
                send_question(driver, pergunta)
            # Após enviar todas as partes do prompt, chama get_response para finalizar o envio
            sugestao += get_response(driver) + "\n"
            # Armazenar as respostas em um arquivo prompt_images.py
            store_responses_in_file(driver, url_ideas, url_prompt, sugestao, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao)
        else:
            print(f"Erro: O prompt '{prompt_valido}' não foi passado corretamente.")

# Função para gerar as respostas e armazenar elas um arquivo prompt_images.py
def store_responses_in_file(driver, url_ideas, url_prompt, sugestao, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao):
    # Abrir a url_ideas
    driver.get(url_prompt)
    time.sleep(5)
    
    # Obter os prompts de texto do script_video.py
    prompts = [titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao]

    prompt_idx = 0  # Variável para acompanhar o índice atual da prompt

    # Enviar prompts de texto para gerar os prompts das imagens
    for idx, prompt in enumerate(prompts):
        command = ("Com base nos prompts de texto de padrao_luminosidade_culinaria_doce, paletas_cores_culinaria_doce, posicionamento_camera_culinaria_doce, prompts_positivos_culinaria_doce e prompts_negativos_culinaria_doce, gere um prompt de texto para isso: " + sugestao)
        send_question(driver, command)
        response = get_response(driver)
        # Resetar sugestao para evitar concatenar resultados anteriores
        sugestao = ""
        # Armazenar a resposta em um arquivo prompt_images.py
        with open(f"prompt_images_{idx}.py", "w") as prompt_file:
            prompt_file.write(f"# Arquivo com o prompt de imagem gerado pela AI\n\n")
            prompt_file.write(f"{prompt} = {repr(response)}\n")
        break  # Quebrar o loop após a primeira iteração
        
    prompt_idx += 1  # Incrementar o índice da prompt

    driver.get(url_ideas)
    time.sleep(5)

