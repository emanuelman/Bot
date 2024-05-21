import subprocess
from temp_prompts import titulo_prompt, introducao_prompt, paragrafos_prompt, desenvolvimento_paragrafo_prompt, finalizacao_prompt, ideias_prompt

def generate_question(prompt):
    question = ""

    if prompt == titulo_prompt:
        tom_titulo = input("Digite o tom do titulo do video, como: chamativo, persuasivo, exagerado ou emocionante: ")
        tema_video = input("Digite o tema do vídeo: ")
        question = prompt.replace("(tom do titulo do video)", tom_titulo)
        question = question.replace("(tema do vídeo)", tema_video)
    elif prompt == introducao_prompt:
        tom_introducao = input("Digite o tom da introdução do video, como: impactante, detalhada, explicativa ou motivacional: ")
        question = prompt.replace("(tom da introdução do video)", tom_introducao)
    elif prompt == paragrafos_prompt:
        total_paragrafos = input("Digite o total de parágrafos: ")
        total_tokens = input("Digite o total de tokens para gerar os paragrafos: ")
        tom_paragrafos = input("Digite o tom dos paragrafos, como: motivacional, inspirador, calmo, engraçado ou educacional: ")
        question = prompt.replace("(total de parágrafos)", total_paragrafos)
        question = question.replace("(total de tokens para gerar os parágrafos)", total_tokens)
        question = question.replace("(tom dos parágrafos)", tom_paragrafos)
    elif prompt == desenvolvimento_paragrafo_prompt:
        pass  # Não há perguntas específicas para este prompt
    elif prompt == finalizacao_prompt:
        pass  # Não há perguntas específicas para este prompt
    elif prompt == ideias_prompt:
        pass  # Não há perguntas específicas para este prompt
    else:
        question = prompt

    return question

# Usar os prompts importados
titulo_question = generate_question(titulo_prompt)
introducao_question = generate_question(introducao_prompt)
paragrafos_question = generate_question(paragrafos_prompt)
desenvolvimento_paragrafo_question = generate_question(desenvolvimento_paragrafo_prompt)
finalizacao_question = generate_question(finalizacao_prompt)
ideias_question = generate_question(ideias_prompt)

# Sobrescrever os prompts no arquivo temp_prompts.py
with open("temp_prompts.py", "w") as file:
    file.write(f"titulo_prompt = \"{titulo_prompt}\"\n")
    file.write(f"introducao_prompt = \"{introducao_prompt}\"\n")
    file.write(f"paragrafos_prompt = \"{paragrafos_prompt}\"\n")
    file.write(f"desenvolvimento_paragrafo_prompt = \"{desenvolvimento_paragrafo_prompt}\"\n")
    file.write(f"finalizacao_prompt = \"{finalizacao_prompt}\"\n")
    file.write(f"ideias_prompt = \"{ideias_prompt}\"\n")

# Executar o arquivo main.py
#subprocess.run(["python3", "main.py"])

