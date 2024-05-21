import os
import shutil
import time
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

# Acessar o site "poe.com"
driver.get("https://poe.com/ChatGPT")
driver.implicitly_wait(10)

# Realizar outras interações, como navegar para outras páginas, clicar em links, etc.

# Encontrar o botão de ir para o login pelo XPath e clicar nele
login_button_xpath = """//*[@id="__next"]/div/div[1]/div[1]/main/div/div/div/div/div/div[1]/a"""
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
login_button.click()

# Encontrar o campo de login do email pelo XPath e preenchê-lo
login_field_xpath = """//*[@id="__next"]/div/main/div[2]/div/div[3]/form/input"""
login_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_field_xpath)))
login_field.send_keys("emanuelantunesdealmeida@gmail.com")

# Encontrar o botão de "Go" pelo XPath e clicar nele
login_button_xpath = """//*[@id="__next"]/div/main/div[2]/div/button[3]"""
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
login_button.click()

# Abrir uma nova janela no Chrome
driver.execute_script("window.open('about:blank', 'new_tab')")

# Alternar para a nova janela
driver.switch_to.window(driver.window_handles[1])

# Acessar o Gmail
driver.get('https://mail.google.com')

# Adicionar os cookies do site Gmail
cookies = [
    {'name': 'SID', 'value': 'g.a000gwgzGokOgV_DuZC5tO_pZEgmmIjqUusIjOJhdzE_OPUaEN2Tc97qb2w75KfQkx072kE6nwACgYKAWISAQASFQHGX2MicBF7M2THhN_vqUlXkABvuxoVAUF8yKoX5wuksxRjOVjj0C7qP7Sp0076'},
    {'name': 'SSID', 'value': 'AcTCbo04O4nhp8dcl'},
    {'name': 'SIDCC', 'value': 'ABTWhQECKhNlGtSoiQX7vcwykK7YYtwJ2TMGRNOBN8yP-014mEd0vAO4jyQ6CN1C4CUmw9L9'},
]

for cookie in cookies:
    driver.add_cookie(cookie)

# Procurar o email de verificação na caixa de entrada
driver.implicitly_wait(10)

email_element = driver.find_element_by_xpath('//span[@name="noreply@poe.com"]/ancestor::tr')
email_element.click()

# Extrair o código de verificação da página
driver.implicitly_wait(5)

codigo_element = driver.find_element_by_xpath('//div[contains(@style, "font-family:system-ui,Segoe UI,sans-serif;font-size:19px;font-weight:700;line-height:1.6;text-align:center;color:#333333")]')
codigo = codigo_element.text

# Retornar para a aba do site poe
driver.switch_to.window(driver.window_handles[0])

# Encontrar o campo do codigo pelo XPath e preenchê-lo
password_field_xpath = """//*[@id="__next"]/div/main/div/div/div[3]/form/input"""
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, password_field_xpath)))
password_field.send_keys("{}".formate(codigo))

# Encontrar o botão de login pelo XPath e clicar nele
login_button_xpath = """//*[@id="__next"]/div/main/div/div/button[2]"""
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
login_button.click()

time.sleep(10)

# Finalizar a sessão do Chrome
driver.quit()

# Excluir o perfil temporário
shutil.rmtree(new_profile_dir)
print("Perfil temporário excluído com sucesso!")

