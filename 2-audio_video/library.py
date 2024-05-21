# Importacoes de bibliotecas para auxiliar na automação do navegador, manipulação de arquivos e parsing de HTML.
import time
import os
import shutil
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#////////////////////////////////////////////////////////////////////
#               FUNCOES DA SEGUNDA PARTE DO PROJETO
#////////////////////////////////////////////////////////////////////

# Importacao da biblioteca de inspects
from inspects import *
from script_video import titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao

# Função para configurar e retornar uma instância do driver do Chrome.
def setup_driver(profile):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"user-data-dir={profile}")
    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver

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
        chat_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))
        chat_input = driver.find_element(By.XPATH, xpath_textarea)
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

