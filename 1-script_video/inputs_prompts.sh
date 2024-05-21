#!/bin/bash

# Pergunta e lê o valor para substituição de {1}
echo "Digite o tom do titulo do video: "
read valor1

# Pergunta e lê o valor para substituição de {2}
echo "Digite o tema do video"
read valor2

# Pergunta e lê o valor para substituição de {3}
echo "Digite o tom da indroducao do video: "
read valor3

# Pergunta e lê o valor para substituição de {7}
echo "Digite o total de tokens: "
read valor4

# Pergunta e lê o valor para substituição de {8}
echo "Digite o tom dos paragrafos: "
read valor5

# Realiza a substituição utilizando o comando sed e cria o arquivo temp_prompts.py
sed "s/{1}/$valor1/g; s/{2}/$valor2/g; s/{3}/$valor3/g; s/{4}/$valor4/g; s/{5}/$valor5/g" prompts.py > temp_prompts.py

echo "Substituição concluída. O arquivo temp_prompts.py foi criado com as alterações."

# Executa o arquivo main.py
python3 main.py

