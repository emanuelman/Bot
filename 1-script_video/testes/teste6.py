import undetected_chromedriver as webdriver
import time

options = webdriver.ChromeOptions()
profile = "/home/octal_chmod777/.config/google-chrome/Profile 3"
options.add_argument(f"user-data-dir={profile}")
driver = webdriver.Chrome(options=options,use_subprocess=True)
driver.get("https://poe.com/ChatGPT")

# Aguarde até que o elemento "x" do pop-up seja clicável
#time.sleep(3)
#element = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "xpath_do_elemento_x")))

# Clique no elemento "x"
#element.click()

# Aguardar até que o elemento de resposta seja exibido
wait = WebDriverWait(driver, timeout)
response_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/footer/div/div/div/textarea')))

# Digitar a pergunta no chat
chat_input_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/main/div/div/div/footer/div/div/div/textarea')
chat_input_element.send_keys("Me dê um codigo em C que printe hello world")

# Pressionar "Enter"
chat_input_element.send_keys(Keys.ENTER)

time.sleep(1000)

