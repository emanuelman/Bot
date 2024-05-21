from library import *
import threading
from Xlib import X, display
from Xlib.ext import randr

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

def first_selenium(driver_ideas, url_ideas):
    # Abrir a URL de ideias
    driver_ideas.get(url_ideas)
    time.sleep(5)

def second_selenium(driver_prompts, url_prompt):
    # Abrir a URL de prompts
    driver_prompts.get(url_prompt)
    time.sleep(5)

# Função para mover a janela para um monitor específico
def move_window_to_screen(window_id, screen_index):
    d = display.Display()
    root = d.screen().root

    # Obter a lista de monitores disponíveis
    monitores = randr.get_monitors(d)

    # Se o índice de tela estiver fora do alcance, exibir um erro
    if screen_index < 0 or screen_index >= len(monitores):
        raise ValueError("Índice de tela inválido")

    # Obter a geometria do monitor desejado
    monitor_geometry = monitores[screen_index]

    # Mover a janela para o monitor desejado
    root.configure_window(
        window_id,
        x=monitor_geometry['x'],
        y=monitor_geometry['y'],
        border_width=0,
        stack_mode=X.Above
    )

    d.sync()  # Sincronizar para aplicar as mudanças

# Função para mover janelas do Chrome para monitores diferentes
def position_chrome_windows(driver_ideas, driver_prompts):
    # Obter os identificadores de janela para cada driver
    chrome_window_id_ideas = driver_ideas.current_window_handle
    chrome_window_id_prompts = driver_prompts.current_window_handle

    # Converter identificadores para inteiros (X Window usa inteiros)
    chrome_window_id_ideas_int = int(chrome_window_id_ideas, 16)
    chrome_window_id_prompts_int = int(chrome_window_id_prompts, 16)

    # Mover o driver_ideas para o primeiro monitor
    move_window_to_screen(chrome_window_id_ideas_int, 0)  # Primeiro monitor

    # Mover o driver_prompts para o segundo monitor
    move_window_to_screen(chrome_window_id_prompts_int, 1)  # Segundo monitor

    # Dar um tempo para a aplicação da mudança
    time.sleep(2)

def main(driver_ideas, driver_prompts, url_ideas, url_prompt):
    profiles = []

    profiles.append(threading.Thread(target=first_selenium, args=[driver_ideas, url_ideas]))
    profiles.append(threading.Thread(target=second_selenium, args=[driver_prompts, url_prompt]))

    for i in profiles:
        i.start()
    
    for i in profiles:
        i.join()

if __name__ == '__main__':
    main(driver_ideas, driver_prompts, url_ideas, url_prompt)

position_chrome_windows(driver_ideas, driver_prompts)

# Fluxo principal para evitar execução dupla
first_profile(driver_ideas, driver_prompts)

