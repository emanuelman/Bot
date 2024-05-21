from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import threading
import time
import config as cf

def start(index):
    options = webdriver.ChromeOptions()
    profile_path = f"user-dasta-dir={cf.local['userDataDir']}{index}"
    options.add_argument(profile_path)

    print(f"Thread {index} profile path: {profile_path}")

    service = Service(cf.local["executablePath"])
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.google.com")

    time.sleep(100)

def worker(index):
    options = webdriver.ChromeOptions()
    profile_path = f"user-dasta-dir={cf.local['userDataDir']}{index}"
    options.add_argument(profile_path)

    print(f"Thread {index} profile path: {profile_path}")

    service = Service(cf.local["executablePath"])
    driver = webdriver.Chrome(service=service, options=options)

    for i in range(10):
        driver.get("https://www.google.com")
        time.sleep(1)

    time.sleep(100)

def main():
    profiles = []

    profiles += [threading.Thread(target=start, args=[0])]
    profiles += [threading.Thread(target=worker, args=[1])]

    for i in profiles:
        i.start()
    
    for i in profiles:
        i.join()

if __name__ == '__main__':
    main()
