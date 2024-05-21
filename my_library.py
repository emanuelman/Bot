# Importacoes de bibliotecas para auxiliar na automação do navegador, manipulação de arquivos e parsing de HTML.
import time
import os
import sys
import shutil
import json
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#////////////////////////////////////////////////////////////////////
#               FUNCOES DA PRIMEIRA PARTE DO PROJETO
#////////////////////////////////////////////////////////////////////

# Importacao da biblioteca de inspects
from script_video_inspects import *

# Função para configurar e retornar uma instância do driver do Chrome.
def setup_driver(profile):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"user-data-dir={profile}")
    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver


# Função para enviar uma pergunta para o chat usando o driver do Chrome.
def send_question(driver, question):
    timeout = 60
    wait = WebDriverWait(driver, timeout)
    response_element = wait.until(EC.presence_of_element_located((By.XPATH, first_xpath_textarea)))

    chat_input_element = driver.find_element(By.XPATH, first_xpath_textarea)
    chat_input_element.send_keys(question)

    chat_input_element.send_keys(Keys.ENTER)

    time.sleep(30)

    response_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, first_class_response_div)))
    return response_div.text.strip()


#////////////////////////////////////////////////////////////////////
#               FUNCOES DA SEGUNDA PARTE DO PROJETO
#////////////////////////////////////////////////////////////////////

# Importacao da biblioteca de inspects
from audio_video_inspects import *

def split_text(text):
    max_chars = 600
    parts = []
    
    while len(text) > max_chars:
        # Encontra a posição da última pontuação final dentro do limite de caracteres
        last_punctuation = max_chars
        for i in range(max_chars, 0, -1):
            if text[i] in ['.', '!', '?']:
                last_punctuation = i
                break
        
        # Adiciona a parte do texto até a última pontuação final à lista de partes
        parts.append(text[:last_punctuation + 1].strip())
        # Remove a parte do texto que já foi adicionada
        text = text[last_punctuation + 1:].strip()
    
    # Adiciona a parte final do texto à lista de partes
    if text:
        parts.append(text.strip())
    
    return parts

def send_text(driver, download_directory, script, counter):
    timeout = 60
    wait = WebDriverWait(driver, timeout)

    # Divide o texto em partes de até 600 caracteres
    script_parts = split_text(script)

    for part in script_parts:
        # Encontra a caixa de texto e escreve o script
        chat_element = wait.until(EC.presence_of_element_located((By.XPATH, second_xpath_textarea)))
        chat_input = driver.find_element(By.XPATH, second_xpath_textarea)
        chat_input.send_keys(part)

        time.sleep(5)

        # Clica no botão para gerar o áudio
        try:
            generate_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, button_generate)))
            generate_button_element.click()
        except TimeoutException as e:
            print(e)

        time.sleep(15)
        
        # Rolar a página até o final
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        chat_input.clear()

        # Localiza o botão de download e clica nele
        try:
            download_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Download Audio')]")))
            download_button_element.click()
        except TimeoutException as e:
            print(e)
        
        time.sleep(10)

        # Inicializa o contador
        file_counter = 1

        # Renomeia o arquivo baixado para um nome único
        for fname in os.listdir(download_directory):
            if fname.endswith('.mp3'):
                audio_file_path = os.path.join(download_directory, f"{counter}.mp3")
                os.rename(os.path.join(download_directory, fname), audio_file_path)
                file_counter += 1  # Incrementa o contador para o próximo arquivo

        chat_input.clear()
        time.sleep(2)
    
    # Rolar a página até o final
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#////////////////////////////////////////////////////////////////////
#               FUNCOES DA TERCEIRA PARTE DO PROJETO
#////////////////////////////////////////////////////////////////////
    
# Importacao da biblioteca de inspects
from prompts_images_inspects import *
from training import *
from script_video import *

def generate_image_prompts_with_existing_chat(driver, url_ideas):
    # Definir a variável como global
    global sugestao

    # Inicializar a variável
    sugestao = ""

    pergunta = ("Me dê apenas de uma sugestão de imagem para eu colocar nesta parte do meu video no meu canal no youtube de culinária: " + prompt)

    # Abrir URL para gerar as sugestoes de imagens para colocar em um momento do video
    driver.get(url_ideas)
    time.sleep(5)

    # Obter os prompts de texto do script_video.py
    prompts = [
        titulo,
        introducao,
        primeiro_paragrafo,
        segundo_paragrafo,
        terceiro_paragrafo,
        quarto_paragrafo,
        finalizacao,
    ]

    # Enviar prompts de texto para gerar imagens
    for prompt in prompts:
        sugestao += send_question(driver, pergunta) + "\n"


def create_chat_and_train_with_json_files(driver, url):

    # Definir a variável como global
    global sugestao

    # Inicializar a variável
    sugestao = ""

    driver.get(url)
    time.sleep(5)

    # Enviar comandos para criar um novo chat
    chat_creation_commands = [
        """Chat, eu vou te fornecer 5 arquivos.json dos quais contém detalhes sobre a geração de
        imagens por inteligência artificial através de prompts de texto baseado no modelo stable difusion.
        Vou te treinar através destes arquivos um de cada vez e após você fazer a análise 
        de cada um dos arquivos que eu te fornecer, peço que caso tenha entendido, retorne: 
        “análise completa”. Caso não entenda algo me retorne: “análise falhou”. Afirmativo?
        """,
        json_padrao_luminosidade,
        json_paletas_cores_culinaria_doce,
        json_posicionamento_camera_culinaria_doce,
        json_prompts_negativos_culinaria_doce,
        json_prompts_positivos_culinaria_doce
    ]

    for command in chat_creation_commands:
        send_question(driver, command)

    store_responses_in_file(driver, url)

# Função para gerar as respostas e armazenar elas um arquivo prompt_images.py
def store_responses_in_file(driver, url):

    # Definir a variável como global
    global sugestao

    # Inicializar a variável
    sugestao = ""

    # Abrir URL para gerar os prompts de texto das imagens
    driver.get(url)
    time.sleep(5)

    # Obter os prompts de texto do script_video.py
    prompts = [
        titulo,
        introducao,
        primeiro_paragrafo,
        segundo_paragrafo,
        terceiro_paragrafo,
        quarto_paragrafo,
        finalizacao,
    ]

    command = f"Gere uma tabela em inglês sobre uma imagem de {sugestao} dividida nos prompts de texto de padrao_luminosidade_culinaria_doce, paletas_cores_culinaria_doce, posicionamento_camera_culinaria_doce, prompts_positivos_culinaria_doce e prompts_negativos_culinaria_doce"

    # Enviar prompts de texto para gerar imagens
    for prompt in prompts:
        sugestao += send_question(driver, command) + "\n"



#////////////////////////////////////////////////////////////////////
#               FUNCOES DA QUARTA PARTE DO PROJETO
#////////////////////////////////////////////////////////////////////
    
