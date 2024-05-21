import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = uc.ChromeOptions()
profile = "/home/octal_chmod777/.config/google-chrome/Profile 3"
options.add_argument(f"user-data-dir={profile}")
driver = uc.Chrome(options=options, use_subprocess=True)
driver.get("https://poe.com/ChatGPT")
time.sleep(5)
#driver.refresh()
#time.sleep(3)

def send_question(question):
    # Aguarde até que o elemento de resposta seja exibido
    timeout = 10  # Exemplo de valor para timeout (5 segundos)
    wait = WebDriverWait(driver, timeout)
    response_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/footer/div/div/div/textarea')))

    # Digitar a pergunta no chat
    chat_input_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/footer/div/div/div/textarea')
    chat_input_element.send_keys(question)

    # Pressionar "Enter"
    chat_input_element.send_keys(Keys.ENTER)

# Enviar a primeira pergunta
send_question("Me dê um código em C que imprima 'Hello, World!'")

# Esperar um pouco antes de enviar a próxima pergunta
time.sleep(5)

# Enviar a segunda pergunta
send_question("Como posso fazer um loop em Python?")

time.sleep(1000)

