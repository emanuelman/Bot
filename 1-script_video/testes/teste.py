import time
from selenium import webdriver

# Define o caminho para o perfil personalizado do Firefox
profile_path = '/home/octal_chmod777/.mozilla/firefox/sfhtfpab.selenium'

# Configura as opções do Firefox para usar o perfil personalizado
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument(f'--profile={profile_path}')

# Inicializa o navegador com as opções configuradas
driver = webdriver.Firefox(options=firefox_options)

# Abre o site poe.com
driver.get('https://poe.com/ChatGPT')
time.sleep(5)

# Find the input field and enter the question
input_field = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div/div/footer/div/div/div/textarea")
time.sleep(5)
input_field.send_keys("what is the bhaskara formula?")
time.sleep(5)

# Find the submit button and click it

submit_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div/div/footer/div/div/button[2]/svg/path")
time.sleep(5)
submit_button.click()
time.sleep(5)

# Agora você pode interagir com o site usando métodos do Selenium, como clicar em botões, preencher formulários, etc.

# Quando terminar, feche o navegador
driver.quit()
