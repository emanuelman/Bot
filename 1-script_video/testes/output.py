import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
profile = "/home/octal_chmod777/.config/google-chrome/Profile 3"
options.add_argument(f"user-data-dir={profile}")
driver = uc.Chrome(options=options, use_subprocess=True)

url = "https://poe.com/chat/249rpaxeeuh7ca0ca51"
driver.get(url)
time.sleep(5)

# Role a página para baixo para carregar todas as mensagens
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Obtenha o conteúdo HTML da página
html = driver.page_source

# Use o BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontre todas as divs com a classe 'Message_botMessageBubble__aYctV'
message_divs = soup.find_all('div', class_='Message_botMessageBubble__aYctV')

# Extrair o texto das tags <p> dentro das divs encontradas
texto_completo = ""
for div in message_divs:
    paragraphs = div.find_all('p')
    for p in paragraphs:
        texto_completo += p.text + "\n\n"

# Salvar o texto no arquivo resposta.txt
with open("resposta.txt", "w") as arquivo:
    arquivo.write(texto_completo)

# Encerre o navegador
driver.quit()

