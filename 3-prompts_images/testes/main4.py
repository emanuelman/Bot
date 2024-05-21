from library import *
import threading
#from Xlib import X, display
#from Xlib.ext import randr
import subprocess

# Diretório para salvar o arquivo sugestoes.py
diretorio_script_video = "~/Desktop/project_youtube_channel/saborarte_namesa/Bot/4-images_video"
# Setar variavel url
url_prompt = ""
# URL para gerar as sugestoes de imagens para colocar em um momento do video
url_ideas = "https://poe.com/chat/26dyhwgufjrp6h9tl2m"
# URL's de chats já existentes que não necessitam de treinamento
url_prompt1 = "https://poe.com/chat/29y55zwgw5qcc1gpeia"
url_prompt2 = "https://poe.com/ChatGPT"

# Verificar se o usuário quer criar um novo chat ou usar um existente
print("""
          
    1 --> url_prompt1 = "https://poe.com/chat/29y55zwgw5qcc1gpeia"
    2 --> url_prompt2 = "https://poe.com/ChatGPT"
          
""")
opcao_chat = input("Escolha uma das opções de chats existentes: ")
if opcao_chat == "1":
    url_prompt = url_prompt1
elif opcao_chat == "2":
    url_prompt = url_prompt2
else:
    print("Opção inválida.")

# Caminhos para perfis do Chrome
profile_ideas = "/home/octal_chmod777/.config/google-chrome/selenium1"
profile_prompts = "/home/octal_chmod777/.config/google-chrome/selenium2"  # Perfil para segundo driver

# Configurar cada driver usando as funções divididas
driver_ideas = setup_first_driver(profile_ideas)  # Driver para `first_selenium`
driver_prompts = setup_second_driver(profile_prompts)  # Driver para `second_selenium`

def get_chrome_window_id(profile_ideas, profile_prompts):
    # Obter todas as janelas
    window_list = subprocess.check_output(["wmctrl", "-l", "-x"]).decode("utf-8").split("\n")

    # Encontrar a janela com base no caminho do perfil
    for window in window_list:
        if profile_ideas in window:
            first_selenium_window_id = window.split()[0]
            # Mover a janela para o primeiro monitor
            subprocess.run(["wmctrl", "-i", "-r", first_selenium_window_id, "-e", "0,0,0,-1,-1"])
        elif profile_prompts in window:
            second_selenium_window_id = window.split()[0]
            # Mover a janela para o segundo monitor
            subprocess.run(["wmctrl", "-i", "-r", second_selenium_window_id, "-e", "0,1366,0,-1,-1"])  # Posição para o segundo monitor

def first_selenium(driver_ideas, url_ideas):
    # Abrir a URL de ideias
    driver_ideas.get(url_ideas)
    time.sleep(5)


def second_selenium(driver_prompts, url_prompt):
    # Abrir a URL de prompts
    driver_prompts.get(url_prompt)
    time.sleep(5)


def main(profile_ideas, profile_prompts, driver_ideas, driver_prompts, url_ideas, url_prompt):
    profiles = []

    profiles.append(threading.Thread(target=first_selenium, args=[driver_ideas, url_ideas]))
    profiles.append(threading.Thread(target=second_selenium, args=[driver_prompts, url_prompt]))

    for i in profiles:
        i.start()
    
    for i in profiles:
        i.join()

    time.sleep(7)
    get_chrome_window_id(profile_ideas, profile_prompts)

    time.sleep(7)
    # Fluxo principal para evitar execução dupla
    first_profile(driver_ideas, driver_prompts)

if __name__ == '__main__':
    main(profile_ideas, profile_prompts, driver_ideas, driver_prompts, url_ideas, url_prompt)

