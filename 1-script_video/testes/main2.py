import os
import shutil
from temp_prompts import titulo_prompt, introducao_prompt, prompt_primeiro_paragrafo, prompt_segundo_paragrafo, prompt_terceiro_paragrafo, prompt_quarto_paragrafo, finalizacao_prompt, ideias_prompt
from inspects import xpath_textarea, class_response_div
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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

# Definir um conjunto para armazenar as respostas únicas
respostas_armazenadas = set()

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

    # Capturar o texto da resposta do chat
    resposta_do_chat = response_div.text

    # Verificar se a resposta já foi armazenada para evitar duplicatas
    if resposta_do_chat not in respostas_armazenadas:
        # Adicionar a resposta ao conjunto de respostas armazenadas
        respostas_armazenadas.add(resposta_do_chat)

        # Escrever a resposta em um arquivo de texto
        with open("resposta_do_chat.txt", "a") as file:
            file.write(resposta_do_chat + "\n\n")


# Enviar a pergunta titulo_prompt
send_question(titulo_prompt)
# Esperar um pouco antes de enviar a próxima pergunta
time.sleep(7)

# Enviar a pergunta introducao_prompt
send_question(introducao_prompt)
# Esperar um pouco antes de enviar a próxima pergunta
time.sleep(7)

# Enviar a pergunta prompt_primeiro_paragrafo
send_question(prompt_primeiro_paragrafo)
# Esperar um pouco antes de enviar a próxima pergunta
time.sleep(7)

# Enviar a pergunta prompt_segundo_paragrafo
send_question(prompt_segundo_paragrafo)
# Esperar um pouco antes de enviar a próxima pergunta
time.sleep(7)

# Enviar a pergunta prompt_terceiro_paragrafo
send_question(prompt_terceiro_paragrafo)
# Esperar um pouco antes de enviar a próxima pergunta
time.sleep(7)

# Enviar a pergunta prompt_quarto_paragrafo
send_question(prompt_quarto_paragrafo)
# Esperar um pouco antes de enviar a próxima pergunta
time.sleep(7)

# Enviar a pergunta finalizacao_prompt
send_question(finalizacao_prompt)
# Esperar um pouco antes de enviar a próxima pergunta
time.sleep(7)

#send_question(ideias_prompt)
# Esperar um pouco antes de enviar a próxima pergunta
#time.sleep(5)

# Deletar o arquivo temp_prompts.py se ele existir
if os.path.exists("temp_prompts.py"):
    os.remove("temp_prompts.py")

time.sleep(1000)
driver.quit()

