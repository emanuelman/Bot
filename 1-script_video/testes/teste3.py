import os
import shutil
import time
import requests
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

# Fazer uma solicitação GET para a página web e obter os cookies atualizados
response = requests.get('https://poe.com/ChatGPT')
cookies = response.cookies

# Adicionar os cookies ao Selenium WebDriver
for cookie in cookies:
    if cookie.domain == ".poe.com":  # Substitua ".poe.com" pelo domínio correto do site
        driver.add_cookie({'name': cookie.name, 'value': cookie.value, 'domain': cookie.domain})
    else:
        print("Ignorando cookie inválido para o domínio {}".format(cookie.domain))

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

