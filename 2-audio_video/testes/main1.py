import os
import shutil
import time
from inspects import xpath_textarea, button_generate, button_download_audio
from script_video import titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Especificando o diretório de download
download_directory = "/home/octal_chmod777/Desktop/project_youtube_channel/saborarte_namesa/Bot/4-video/audios"

options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu") # Adicionando a opção para desabilitar a GPU
profile = "/home/octal_chmod777/.config/google-chrome/Profile 3"
options.add_argument(f"user-data-dir={profile}")
# Especificando o diretório de download
options.add_experimental_option("prefs", {
  "download.default_directory": download_directory
})
driver = uc.Chrome(options=options, use_subprocess=True)
url = "https://elevenlabs.io/"
driver.get(url)
time.sleep(10)

# Rolar a página até o final
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def split_text(text):
    max_chars = 600
    parts = []

    # Lista de pontuações finais que indicam o fim de uma frase ou ideia
    end_punctuations = ['.', '!', '?']

    current_part = ""
    for word in text.split():
        # Adiciona a palavra atual à parte atual
        current_part += word + " "

        # Verifica se a parte atual excede o limite de caracteres ou se a última palavra é uma pontuação final
        if len(current_part) > max_chars or current_part.strip()[-1] in end_punctuations:
            # Adiciona a parte atual à lista de partes
            parts.append(current_part.strip())
            # Reinicia a parte atual
            current_part = ""

    # Adiciona a parte final, se existir
    if current_part:
        parts.append(current_part.strip())

    return parts

def send_text(script, counter):
    timeout = 60
    wait = WebDriverWait(driver, timeout)

    # Divide o texto em partes de até 600 caracteres, mantendo a coesão
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


texts = [
    titulo,
    introducao,
    primeiro_paragrafo,
    segundo_paragrafo,
    terceiro_paragrafo,
    quarto_paragrafo,
    finalizacao,
]

# Contador para nomear os arquivos de áudio
counter = 1

for text in texts:
    send_text(text, counter)
    counter += 1

print("feito!")

time.sleep(1000)
driver.quit()

