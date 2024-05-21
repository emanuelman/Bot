import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

def setup_driver(profile_path):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"--user-data-dir={profile_path}")
    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver  # Retorna o driver para o primeiro perfil

profile_ideas = "/home/octal_chmod777/.config/google-chrome/selenium2"

driver = setup_driver(profile_ideas)
url = "https://google.com.br"
driver.get(url)
time.sleep(100)
