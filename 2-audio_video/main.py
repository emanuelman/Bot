import os
import time
from library import *

# Especificando o diretório de download
download_directory = "/home/octal_chmod777/Desktop/project_youtube_channel/saborarte_namesa/Bot/4-video/audios"

profile = "/home/octal_chmod777/.config/google-chrome/Profile 3"
url = "https://elevenlabs.io/"
driver = setup_driver(profile)

driver.get(url)
time.sleep(10)

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
    send_text(driver, download_directory, text, counter)
    counter += 1

print("feito!")

time.sleep(1000)
driver.quit()

