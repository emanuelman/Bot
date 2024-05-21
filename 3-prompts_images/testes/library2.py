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

    try:
        # Espera até que o elemento esteja presente na página
        response_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))
        chat_input_element = driver.find_element(By.XPATH, xpath_textarea)

        # Limpar o campo de entrada antes de enviar a pergunta
        chat_input_element.clear()

        # Enviar a pergunta completa para o chat
        chat_input_element.send_keys(question)

        # Aguardar um momento
        time.sleep(5)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None
    
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
    time.sleep(2)

    response_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_response_div)))
    return response_div.text.strip()

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
    url = driver.current_url
    # Chama a funcao generate_image_prompts_with_existing_chat
    generate_image_prompts_with_existing_chat(driver, url_ideas, url_prompt, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao)

def generate_image_prompts_with_existing_chat(driver, url_ideas, url_prompt, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao):

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

    sugestao = ""  

    prompts = [titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao]
    prompts_validos = ["titulo", "introducao", "primeiro_paragrafo", "segundo_paragrafo", "terceiro_paragrafo", "quarto_paragrafo", "finalizacao"]

    for prompt, prompt_valido in zip(prompts, prompts_validos):
        if prompt_valido in locals() and prompt == locals()[prompt_valido]:
            partes_prompt = divide_texto(prompt)
            for parte in partes_prompt:
                texto = "Me dê apenas uma sugestão de imagem para eu colocar nesta parte do meu vídeo no meu canal no YouTube de culinária: " + parte
                pergunta = texto
                driver.get(url_ideas)
                time.sleep(5)
                send_question(driver, pergunta)
            # Após enviar todas as partes do prompt, chama get_response para finalizar o envio
            sugestao += get_response(driver) + "\n"
        else:
            print(f"Erro: O prompt '{prompt_valido}' não foi passado corretamente.")
        # Armazenar as respostas em um arquivo prompt_images.py
        store_responses_in_file(driver, url_prompt, sugestao, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao)

# Função para gerar as respostas e armazenar elas um arquivo prompt_images.py
def store_responses_in_file(driver, url_prompt, sugestao, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao):
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

