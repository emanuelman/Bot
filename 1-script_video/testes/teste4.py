import shutil
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Criar um novo perfil com o Selenium
new_profile_dir = "/home/octal_chmod777/.config/google-chrome/ProfileA"  # Substitua "/path/to/new_profile" pelo caminho do novo perfil

if os.path.exists(new_profile_dir):
    shutil.rmtree(new_profile_dir)

# Mover os arquivos do perfil antigo para o novo perfil
old_profile_dir = "/home/octal_chmod777/.config/google-chrome/Profile 3"  # Substitua "/path/to/old_profile" pelo caminho do perfil antigo
shutil.copytree(old_profile_dir, new_profile_dir)

print("Transferência de perfil concluída com sucesso!")

# Configurar o Selenium para usar o perfil desejado
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=/home/octal_chmod777/.config/google-chrome")
chrome_options.add_argument("--profile-directory=ProfileA")

# Iniciar o Chrome com o perfil desejado
driver = webdriver.Chrome(options=chrome_options)

# Obter todos os cookies do perfil antigo
old_profile_cookies = driver.get_cookies()

# Adicionar os cookies ao perfil copiado
for cookie in old_profile_cookies:
    new_profile_dir.add_cookie(cookie)

# Acessar o site "poe.com"
driver.get("https://poe.com/ChatGPT")
driver.implicitly_wait(10)

# Realizar outras interações, como navegar para outras páginas, clicar em links, etc.

time.sleep(10)

# Finalizar a sessão do Chrome
driver.quit()

# Excluir o perfil temporário
shutil.rmtree(new_profile_dir)
print("Perfil temporário excluído com sucesso!")

