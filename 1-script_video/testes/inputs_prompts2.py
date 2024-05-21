# Importando os prompts
from temp_prompts import titulo_prompt, introducao_prompt, paragrafos_prompt, desenvolvimento_paragrafo_prompt, finalizacao_prompt, ideias_prompt

# Função para substituir os placeholders pelos valores fornecidos
def substituir_placeholders(prompt, valores):
    return prompt.format(*valores)

# Exemplo de uso
titulo_resposta = input("Digite um tom para o título: chamativo, persuasivo, exagerado ou emocionante: ")
tema_resposta = input("Digite o tema do vídeo: ")
tom_introducao_resposta = input("Digite o tom da introdução, impactante, detalhada, explicativa, motivacional): ")
total_paragrafos_resposta = input("Digite o total de parágrafos: ")
paragrafos_tokens_resposta = input("Digite o número de tokens dos parágrafos: ")
tom_paragrafos_resposta = input("Digite o tom dos parágrafos, motivacional, inspirador, calmo, engraçado ou educacional: ")

# Substituindo os placeholders nos prompts
titulo_substituido = substituir_placeholders(titulo_prompt, (titulo_resposta, tema_resposta))
introducao_substituida = substituir_placeholders(introducao_prompt, (tom_introducao_resposta, tema_resposta))
paragrafos_substituidos = substituir_placeholders(paragrafos_prompt, (total_paragrafos_resposta, tema_resposta, paragrafos_tokens_resposta, tom_paragrafos_resposta))
# Manter o valor original
desenvolvimento_paragrafo_substituido = desenvolvimento_paragrafo_prompt
finalizacao_substituida = finalizacao_prompt
ideias_substituidas = ideias_prompt

# Atualizando o arquivo temp_prompts.py
with open("temp_prompts.py", "r") as file:
    lines = file.readlines()

lines[1] = f"titulo_prompt = \"{titulo_substituido}\"\n"
lines[3] = f"introducao_prompt = \"{introducao_substituida}\"\n"
lines[5] = f"paragrafos_prompt = \"{paragrafos_substituidos}\"\n"

with open("temp_prompts.py", "w") as file:
    file.writelines(lines)

