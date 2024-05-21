# Importacoes de bibliotecas para auxiliar na automação do navegador, manipulação de arquivos e parsing de HTML.
import time
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Importacao da biblioteca de inspects
from inspects import *
from training import *

# Função para configurar e retornar uma instância do driver
def setup_first_driver(profile_path):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"--user-data-dir={profile_path}")
    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver  # Retorna o driver para o primeiro perfil

def setup_second_driver(profile_path):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"--user-data-dir={profile_path}")
    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver  # Retorna o driver para o segundo perfil

def send_question_ideas(driver_ideas, question):
    timeout = 60
    wait = WebDriverWait(driver_ideas, timeout)

    # Espera até que o elemento esteja presente na página
    response_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))
    chat_input_element = driver_ideas.find_element(By.XPATH, xpath_textarea)

    # Limpar o campo de entrada antes de enviar a pergunta
    #chat_input_element.clear()

    # Enviar a pergunta completa para o chat
    chat_input_element.send_keys(question)

    # Aguardar um momento
    time.sleep(5)

def send_question_prompts(driver_prompts, question):
    timeout = 60
    wait = WebDriverWait(driver_prompts, timeout)

    # Espera até que o elemento esteja presente na página
    response_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))
    chat_input_element = driver_prompts.find_element(By.XPATH, xpath_textarea)

    # Limpar o campo de entrada antes de enviar a pergunta
    #chat_input_element.clear()

    # Enviar a pergunta completa para o chat
    chat_input_element.send_keys(question)

    # Aguardar um momento
    time.sleep(5)

def get_response_ideas(driver_ideas):
    timeout = 60
    wait = WebDriverWait(driver_ideas, timeout)

    wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))
    chat_input_element = driver_ideas.find_element(By.XPATH, xpath_textarea)

    # Enviar a pergunta pressionando a tecla Enter
    time.sleep(5)  # Espera um pouco antes de enviar a pergunta para evitar conflitos
    chat_input_element.send_keys(Keys.ENTER)

    time.sleep(22) # Espera um pouco depois de enviar a pergunta para evitar conflitos
    driver_ideas.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)

    response_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_response_div)))

    return response_div.text.strip()

def get_response_prompts(driver_prompts):
    timeout = 60
    wait = WebDriverWait(driver_prompts, timeout)

    wait.until(EC.presence_of_element_located((By.XPATH, xpath_textarea)))
    chat_input_element = driver_prompts.find_element(By.XPATH, xpath_textarea)

    # Enviar a pergunta pressionando a tecla Enter
    time.sleep(5)  # Espera um pouco antes de enviar a pergunta para evitar conflitos
    chat_input_element.send_keys(Keys.ENTER)

    time.sleep(22) # Espera um pouco depois de enviar a pergunta para evitar conflitos
    driver_prompts.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)

    response_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_response_div)))

    return response_div.text.strip()

class GenerateImagePrompts:
    def __init__(self, driver_ideas, driver_prompts, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao):
        # Atributos da classe, baseados nos parâmetros originais
        self.driver_ideas = driver_ideas
        self.driver_prompts = driver_prompts
        self.prompt_idx = 0  # Variável para acompanhar o índice atual da prompt
        # Usar a instância de Prompts passada como argumento
        self.titulo = titulo
        self.introducao = introducao
        self.primeiro_paragrafo = primeiro_paragrafo
        self.segundo_paragrafo = segundo_paragrafo
        self.terceiro_paragrafo = terceiro_paragrafo
        self.quarto_paragrafo = quarto_paragrafo
        self.finalizacao = finalizacao

    def divide_texto(self, texto):
        tamanho_maximo_parte = 100
        partes = []
        parte_atual = ""
        
        for palavra in texto.split():
            parte_atual += palavra + " "
            if len(parte_atual) >= tamanho_maximo_parte:
                partes.append(parte_atual.strip())
                parte_atual = ""
        
        if parte_atual:
            partes.append(parte_atual.strip())
        
        return partes

    def dividir_prompt_em_partes(self, prompts):
        prompts_divididos = {}
        
        for idx, prompt in enumerate(prompts):
            partes_prompt = self.divide_texto(prompt)
            numero_partes = len(partes_prompt)
            for i, parte in enumerate(partes_prompt):
                chave = f"prompt_{chr(ord('A') + i)}"
                prompts_divididos[chave] = parte
        
        return prompts_divididos
    
    def store_responses(self, sugestao):
        prompts = [
        self.titulo, self.introducao, self.primeiro_paragrafo, self.segundo_paragrafo, self.terceiro_paragrafo, self.quarto_paragrafo, self.finalizacao
        ]

        # Enviar prompts de texto para gerar os prompts das imagens
        for idx, prompt in enumerate(prompts):
            command = (
                "Com base nos prompts de padrao_luminosidade_culinaria_doce, paletas_cores_culinaria_doce, posicionamento_camera_culinaria_doce, prompts_positivos_culinaria_doce e prompts_negativos_culinaria_doce, gere um prompt de texto para isso: " + sugestao
            )
            send_question_prompts(self.driver_prompts, command)
            response = get_response_prompts(self.driver_prompts)
            
            # Armazenar a resposta em um arquivo prompt_images.py
            with open(f"prompt_images_{self.prompt_idx}.py", "w") as prompt_file:
                prompt_file.write("# Arquivo com o prompt de imagem gerado pela AI\n")
                prompt_file.write(f"{prompt} = {repr(response)}\n")
            
            self.prompt_idx += 1  # Incrementar o índice da prompt
            break  # Quebrar o loop após a primeira iteração
        
        # Alternando para a janela do perfil "driver_ideas"
        self.driver_ideas.switch_to.window(self.driver_ideas.window_handles[0])
        time.sleep(5)

    def generate_prompts(self):
        # Transformar os atributos da classe em uma lista
        prompts = [
            self.titulo, self.introducao, self.primeiro_paragrafo, self.segundo_paragrafo, self.terceiro_paragrafo, self.quarto_paragrafo, self.finalizacao
        ]
        prompts_validos = ["titulo", "introducao", "primeiro_paragrafo", "segundo_paragrafo", "terceiro_paragrafo", "quarto_paragrafo", "finalizacao"]

        # Verificar se todos os prompts têm valores válidos
        for prompt_valido, prompt in zip(prompts_validos, prompts):
            if not prompt:
                raise ValueError(f"O prompt '{prompt_valido}' não pode ser vazio ou nulo.")

        # Loop para processar cada prompt
        for prompt_valido, prompt in zip(prompts_validos, prompts):
            # Dividir o prompt em partes
            partes = self.dividir_prompt_em_partes([prompt])

            # Enviar a pergunta inicial
            texto = f"Me dê apenas uma sugestão de imagem para eu colocar nesta parte do meu vídeo no meu canal no YouTube de culinária: {prompt_valido}."
            send_question_ideas(self.driver_ideas, texto)

            # Enviar cada parte do prompt para obter sugestões
            for parte in partes.values():
                send_question_ideas(self.driver_ideas, parte)

            # Obter resposta para cada parte do prompt
            sugestao = ""
            sugestao = get_response_ideas(self.driver_ideas)

        # Armazenar as respostas depois de processar todos os prompts
        self.store_responses(sugestao)  # Certifique-se de que está bem implementado

