import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = uc.ChromeOptions()
profile = "/home/octal_chmod777/.config/google-chrome/Profile 3"
options.add_argument(f"user-data-dir={profile}")
driver = uc.Chrome(options=options,use_subprocess=True)
driver.get("https://poe.com/ChatGPT")
time.sleep(5)

# Aguarde até que o elemento "x" do pop-up seja clicável
#time.sleep(3)
#element = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "xpath_do_elemento_x")))

# Clique no elemento "x"
#element.click()

# Aguardar até que o elemento de resposta seja exibido
timeout = 5  # Exemplo de valor para timeout (5 segundos)
wait = WebDriverWait(driver, timeout)
response_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/footer/div/div/div/textarea')))

# Digitar a pergunta em C no chat
chat_input_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/footer/div/div/div/textarea')
chat_input_element.send_keys("Me dê um código em C que imprima 'Hello, World!'")

# Pressionar "Enter"
chat_input_element.send_keys(Keys.ENTER)

# Aguardar até que o elemento de resposta seja exibido
wait = WebDriverWait(driver, timeout)
response_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/footer/div/div/div/textarea')))

# Digitar a pergunta em C++ no chat
chat_input_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/footer/div/div/div/textarea')
chat_input_element.send_keys("Agora me dê um código em C++ que imprima 'Hello, World!'")

# Pressionar "Enter"
chat_input_element.send_keys(Keys.ENTER)

# Pressionar "Enter"
chat_input_element.send_keys(Keys.ENTER)

time.sleep(1000)

