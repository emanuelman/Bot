# Importacoes de bibliotecas para auxiliar na automação do navegador, manipulação de arquivos e parsing de HTML.
import time
import os
import shutil
import json
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup

# Importacao da biblioteca de inspects
from inspects import *
from training import *
from script_video import *

class Prompts:
    def __init__(self, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao):
        self.titulo = titulo
        self.introducao = introducao
        self.primeiro_paragrafo = primeiro_paragrafo
        self.segundo_paragrafo = segundo_paragrafo
        self.terceiro_paragrafo = terceiro_paragrafo
        self.quarto_paragrafo = quarto_paragrafo
        self.finalizacao = finalizacao

# Função para configurar e retornar uma instância do driver
def setup_first_driver(profile_path):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"-user-data-dir={profile_path}")
    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver  # Retorna o driver para o primeiro perfil

def setup_second_driver(profile_path):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"-user-data-dir={profile_path}")
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

class ResponseStorage:
    def __init__(self, driver_ideas, driver_prompts, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao):
        # Atributos da classe, baseados nos parâmetros originais
        self.driver_ideas = driver_ideas
        self.driver_prompts = driver_prompts
        self.titulo = titulo
        self.introducao = introducao
        self.primeiro_paragrafo = primeiro_paragrafo
        self.segundo_paragrafo = segundo_paragrafo
        self.terceiro_paragrafo = terceiro_paragrafo
        self.quarto_paragrafo = quarto_paragrafo
        self.finalizacao = finalizacao
        self.prompt_idx = 0  # Índice para acompanhar a prompt

    def store_responses(self, sugestao):
        # Obter os prompts de texto do script_video.py
        prompts = [self.titulo, self.introducao, self.primeiro_paragrafo, self.segundo_paragrafo, self.terceiro_paragrafo, self.quarto_paragrafo, self.finalizacao]

        # Enviar prompts de texto para gerar os prompts das imagens
        for idx, prompt in enumerate(prompts):
            command = (
                "Com base nos prompts de padrao_luminosidade_culinaria_doce, paletas_cores_culinaria_doce, posicionamento_camera_culinaria_doce, prompts_positivos_culinaria_doce e prompts_negativos_culinaria_doce, gere um prompt de texto para isso: " + sugestao
            )
            send_question_prompts(self.driver_ideas, self.driver_prompts, command)
            response = get_response_prompts(self.driver_ideas, self.driver_prompts)
            
            # Armazenar a resposta em um arquivo prompt_images.py
            with open(f"prompt_images_{self.prompt_idx}.py", "w") as prompt_file:
                prompt_file.write("# Arquivo com o prompt de imagem gerado pela AI\n")
                prompt_file.write(f"{prompt} = {repr(response)}\n")
            
            self.prompt_idx += 1  # Incrementar o índice da prompt
            break  # Quebrar o loop após a primeira iteração

        sugestao = ""
        
        # Alternando para a janela do perfil "driver_ideas"
        self.driver_ideas.switch_to.window(self.driver_ideas.window_handles[0])
        time.sleep(5)

class GenerateImagePrompts:
    def __init__(self, driver_ideas, driver_prompts, titulo, introducao, primeiro_paragrafo, segundo_paragrafo, terceiro_paragrafo, quarto_paragrafo, finalizacao):
        # Atributos da classe, baseados nos parâmetros originais
        self.driver_ideas = driver_ideas
        self.driver_prompts = driver_prompts
        self.titulo = titulo
        self.introducao = introducao
        self.primeiro_paragrafo = primeiro_paragrafo
        self.segundo_paragrafo = segundo_paragrafo
        self.terceiro_paragrafo = terceiro_paragrafo
        self.quarto_paragrafo = quarto_paragrafo
        self.finalizacao = finalizacao
        self.sugestao = ""
        self.prompt_idx = 0  # Variável para acompanhar o índice atual da prompt

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

    def generate_prompts(self):
        # Transformar os atributos da classe em uma lista
        prompts = [self.titulo, self.introducao, self.primeiro_paragrafo, self.segundo_paragrafo, self.terceiro_paragrafo, self.quarto_paragrafo, self.finalizacao]
        prompts_validos = ["titulo", "introducao", "primeiro_paragrafo", "segundo_paragrafo", "terceiro_paragrafo", "quarto_paragrafo", "finalizacao"]
        
        for prompt, prompt_valido in zip(prompts, prompts_validos):
            if prompt_valido in locals() and prompt == locals()[prompt_valido]:
                dicionario_prompts = self.dividir_prompt_em_partes([prompt])
                
                texto = "Me dê apenas uma sugestão de imagem para eu colocar nesta parte do meu vídeo no meu canal no YouTube de culinária: "
                
                send_question_ideas(self.driver_ideas, texto)
                
                for parte_prompt in dicionario_prompts.values():
                    send_question_ideas(self.driver_ideas, parte_prompt)
                
                self.sugestao += get_response_ideas(self.driver_ideas) + "\n"
                
                second_profile(self.driver_ideas, self.driver_prompts, self.sugestao, self.titulo, self.introducao, self.primeiro_paragrafo, self.segundo_paragrafo, self.terceiro_paragrafo, self.quarto_paragrafo, self.finalizacao)

                # Armazenar as respostas em um arquivo
                #store_responses_in_file(self.driver_ideas, self.driver_prompts, self.prompt_idx, self.sugestao, self.titulo, self.introducao, self.primeiro_paragrafo, self.segundo_paragrafo, self.terceiro_paragrafo, self.quarto_paragrafo, self.finalizacao)
            else:
                print(f"Erro: O prompt '{prompt_valido}' não foi passado corretamente.")
        
        return self.sugestao
    
def first_profile(driver_ideas, driver_prompts):
    
    instance_prompts = Prompts(
        titulo,
        introducao,
        primeiro_paragrafo,
        segundo_paragrafo,
        terceiro_paragrafo,
        quarto_paragrafo,
        finalizacao
    )
    
    # Criar uma instância de GenerateImagePrompts
    instance = GenerateImagePrompts(
        driver_ideas,
        driver_prompts,
        instance_prompts.titulo
        instance_prompts.introducao
        instance_prompts.primeiro_paragrafo
        instance_prompts.segundo_paragrafo
        instance_prompts.terceiro_paragrafo
        instance_prompts.quarto_paragrafo
        instance_prompts.finalizacao
    )

    # Chamar o método generate_prompts da instância
    sugestao = instance.generate_prompts()  # Chamar método da instância

    return sugestao

def second_profile(driver_ideas, driver_prompts, sugestao):
    
    
    # Criar uma instância de ResponseStorage
    response_storage = ResponseStorage(
        driver_ideas,
        driver_prompts,
        *prompts
)

    # Chamar o método para armazenar as respostas
    response_storage.store_responses(sugestao)

