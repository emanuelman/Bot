from library import *
from Xlib import X, display, protocol
import threading
import pygetwindow as gw

# Diretório para salvar o arquivo sugestoes.py
diretorio_script_video = "~/Desktop/project_youtube_channel/saborarte_namesa/Bot/4-images_video"
# Setar variavel url
url_prompt = ""
# URL para gerar as sugestoes de imagens para colocar em um momento do video
url_ideas = "https://poe.com/chat/26dyhwgufjrp6h9tl2m"
# URL's de chats já existentes que não necessitam de treinamento
url_prompt1 = "https://poe.com/chat/26drgh6ihx5l7t9191g"
url_prompt2 = "https://poe.com/ChatGPT/2"
# URL de uma chat novo
url_prompt_novo = "https://poe.com/ChatGPT"

# Verificar se o usuário quer criar um novo chat ou usar um existente
opcao = input("Escolha a 1 opcao para criar um novo chat ou a 2 opcao para usar um chat existente: ")

if opcao == "1":
    url_prompt = url_prompt_novo
elif opcao == "2":
    print("""
          
        1 --> url_prompt1 = "https://poe.com/chat/26drgh6ihx5l7t9191g"
        2 --> url_prompt2 = "https://poe.com/ChatGPT/2"
          
    """)
    opcao_chat = input("Escolha uma das opções de chats existentes: ")
    if opcao_chat == "1":
        url_prompt = url_prompt1
    elif opcao_chat == "2":
        url_prompt = url_prompt2
    else:
        print("Opção inválida.")
else:
    print("Opção inválida.")

def first_selenuim(index, url_ideas):
    # Diretorio onde se encontra o prifile do chrome que sera utilizado
    profile_ideas = "/home/octal_chmod777/.config/google-chrome/Profile 3"

    # Configurar a instância do driver do profile_ideas
    driver_ideas = setup_driver(profile_ideas)

    # Abrir o profile_ideas
    driver_ideas.get(url_ideas)
    time.sleep(5)

    # Obtém o identificador da janela do Chrome
    chrome_window_id = driver_ideas.current_window_handle

    # Obtém o nome da janela do Chrome usando o identificador
    chrome_window_name = gw.get_window_title(chrome_window_id)
    print(f"Thread {index} Chrome window name: {chrome_window_name}")

    # Conectando ao servidor X
    d = display.Display()

    # Obtendo uma lista de todas as telas disponíveis
    screens = d.screen_count()

    # Verificando se há pelo menos duas telas disponíveis
    if screens >= 2:
        # Obtendo a raiz da tela do segundo monitor
        second_screen_root = d.screen(1).root

        # Obtendo o ID da janela do Chrome convertendo a sequência hexadecimal para um numero inteiro
        window_id = int(chrome_window_id, 16)

        # Obtendo a estrutura de evento para mudança de propriedade
        event = protocol.event.ClientMessage(
            window=window_id,
            client_type=d.intern_atom('_NET_WM_DESKTOP'),
            data=(0, 0, 0, 0, 0) 
        )

        # Enviando o evento de mudança de propriedade para a janela do Chrome
        second_screen_root.send_event(event, event_mask=X.SubstructureRedirectMask)
        d.sync()

def second_selenuim(index, url_prompt):
    # Diretorio onde se encontra o prifile do chrome que sera utilizado
    profile_prompts = "/home/octal_chmod777/.config/google-chrome/Profile 5"

    # Configurar a instância do driver do profile_prompts
    driver_prompts = setup_driver(profile_prompts)

    # Abrir o profile_prompts
    driver_prompts.get(url_prompt)
    time.sleep(5)

    # Obtém o identificador da janela do Chrome
    chrome_window_id = driver_prompts.current_window_handle

    # Obtém o nome da janela do Chrome usando o identificador
    chrome_window_name = gw.get_window_title(chrome_window_id)
    print(f"Thread {index} Chrome window name: {chrome_window_name}")

    # Conectando ao servidor X
    d = display.Display()

    # Obtendo uma lista de todas as telas disponíveis
    screens = d.screen_count()

    # Verificando se há pelo menos duas telas disponíveis
    if screens >= 2:
        # Obtendo a raiz da tela do segundo monitor
        second_screen_root = d.screen(1).root

        # Obtendo o ID da janela do Chrome
        window_id = int(chrome_window_id, 16)

        # Obtendo a estrutura de evento para mudança de propriedade
        event = protocol.event.ClientMessage(
            window=window_id,
            client_type=d.intern_atom('_NET_WM_DESKTOP'),
            data=(1, 0, 0, 0, 0)  # Defina o monitor desejado (0 para o primeiro monitor, 1 para o segundo, etc.)
        )

        # Enviando o evento de mudança de propriedade para a janela do Chrome
        second_screen_root.send_event(event, event_mask=X.SubstructureRedirectMask)
        d.sync()

def main():
    profiles = []

    profiles += [threading.Thread(target=first_selenuim, args=[0])]
    profiles += [threading.Thread(target=second_selenuim, args=[1])]

    for i in profiles:
        i.start()
    
    for i in profiles:
        i.join()

if __name__ == '__main__':
    main()

if url_prompt == url_prompt_novo:
    create_chat_and_train_with_json_files(first_selenuim.driver_ideas, second_selenuim.driver_prompts, url_ideas, url_prompt, json_padrao_luminosidade, json_paletas_cores_culinaria_doce, json_posicionamento_camera_culinaria_doce, json_prompts_negativos_culinaria_doce, json_prompts_positivos_culinaria_doce)
elif url_prompt == url_prompt1 or url_prompt == url_prompt2:
    generate_image_prompts_with_existing_chat(first_selenuim.driver_ideas, second_selenuim.driver_prompts, url_ideas, url_prompt, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao)
else:
    print("Erro!")

first_selenuim.driver_ideas.quit()
second_selenuim.driver_prompts.quit()

