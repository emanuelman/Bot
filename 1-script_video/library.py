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
#               FUNCOES DA PRIMEIRA PARTE DO PROJETO
#////////////////////////////////////////////////////////////////////

# Importacao da biblioteca de inspects
from inspects import *
from temp_prompts import titulo_prompt, introducao_prompt, prompt_primeiro_paragrafo, prompt_segundo_paragrafo, prompt_terceiro_paragrafo, prompt_quarto_paragrafo, finalizacao_prompt, ideias_prompt

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
    response_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))

    chat_input_element = driver.find_element(By.XPATH, xpath_textarea)
    chat_input_element.send_keys(question)

    time.sleep(5)

    chat_input_element.send_keys(Keys.ENTER)

    time.sleep(30)

    response_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_response_div)))
    return response_div.text.strip()
