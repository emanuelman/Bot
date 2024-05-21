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
profile = "/home/octal_chmod777/.config/google-chrome/Profile 3"
options.add_argument(f"user-data-dir={profile}")
driver = uc.Chrome(options=options, use_subprocess=True)
url = "https://poe.com/ChatGPT"
driver.get(url)
time.sleep(5)
#driver.refresh()
#time.sleep(3)

def send_question(question):
    # Aguarde até que o elemento de resposta seja exibido
    timeout = 60  # Exemplo de valor para timeout (5 segundos)
    wait = WebDriverWait(driver, timeout)
    response_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))

    # Digitar a pergunta no chat
    chat_input_element = driver.find_element(By.XPATH, xpath_textarea)
    chat_input_element.send_keys(question)

    # Pressionar "Enter"
    chat_input_element.send_keys(Keys.ENTER)

    # Aguardar um curto período para a resposta do chat ser carregada
    time.sleep(30)

    # Aguarde até que a resposta do chat seja exibida
    response_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_response_div)))

# Enviar as perguntas do arquivo temp_prompts.py
prompts = [
    titulo_prompt,
    introducao_prompt,
    prompt_primeiro_paragrafo,
    prompt_segundo_paragrafo,
    prompt_terceiro_paragrafo,
    prompt_quarto_paragrafo,
    finalizacao_prompt,
]

for prompt in prompts:
    send_question(prompt)
    # Esperar um pouco antes de enviar a próxima pergunta
    time.sleep(7)

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

# Deletar o arquivo temp_prompts.py se ele existir
if os.path.exists("temp_prompts.py"):
    os.remove("temp_prompts.py")

time.sleep(1000)
driver.quit()

