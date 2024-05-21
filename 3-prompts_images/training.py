import json

json_padrao_luminosidade = '''
{
  "padrao_luminosidade_culinaria_doce": [
    {
      "padrao_luminosidade": "Luz Natural",
      "descricao": "Iluminação suave e difusa, simulando a luz do dia. Ideal para destacar detalhes, cores vibrantes e criar uma atmosfera fresca e convidativa."
    },
    {
      "padrao_luminosidade": "Backlight",
      "descricao": "A luz posicionada atrás dos doces, criando um contorno luminoso e destacando a silhueta. Ótimo para realçar a textura e criar um efeito visual dramático."
    },
    {
      "padrao_luminosidade": "Luz Suave",
      "descricao": "Iluminação suave e difusa de todos os lados, minimizando sombras. Proporciona uma aparência aconchegante e realça a suavidade das sobremesas."
    },
    {
      "padrao_luminosidade": "Contraluz",
      "descricao": "Iluminação proveniente de trás da cena, destacando contornos e criando uma atmosfera de destaque. Pode ressaltar detalhes e criar um efeito artístico."
    },
    {
      "padrao_luminosidade": "Luz de Estúdio",
      "descricao": "Iluminação controlada, com foco direto nos doces. Permite realçar cores, texturas e criar um ambiente mais refinado. Ideal para fotografias de estúdio."
    },
    {
      "padrao_luminosidade": "Luz Ambiente",
      "descricao": "Iluminação suave e uniforme em todo o ambiente, proporcionando uma atmosfera natural e acolhedora. Adequada para cenas mais relaxadas e casuais."
    },
    {
      "padrao_luminosidade": "Luz Intensa",
      "descricao": "Iluminação forte e direta, destacando detalhes nítidos e criando uma atmosfera energética. Pode ser usada para realçar cores vibrantes e criar contraste."
    },
    {
      "padrao_luminosidade": "Luz Sutil",
      "descricao": "Iluminação suave, com sombras delicadas. Ideal para criar uma atmosfera romântica e destacar detalhes delicados, como decorações de sobremesas."
    }
  ]
}
'''

json_paletas_cores_culinaria_doce = '''
{
  "paletas_cores_culinaria_doce": [
    {
      "nome_paleta": "Doçura",
      "cores": ["Rosa pastel", "Azul claro", "Amarelo suave", "Verde menta"],
      "utilizacao": "Ideal para transmitir uma atmosfera doce e suave, perfeito para imagens de cupcakes, cookies, macarons e sobremesas delicadas."
    },
    {
      "nome_paleta": "Chocolover",
      "cores": ["Marrom chocolate", "Caramelo", "Bege", "Branco"],
      "utilizacao": "Ótimo para imagens de sobremesas de chocolate, trufas, bolos de chocolate, brigadeiros e qualquer doce com ingredientes de chocolate."
    },
    {
      "nome_paleta": "Frutado",
      "cores": ["Vermelho morango", "Laranja tangerina", "Amarelo limão", "Verde kiwi"],
      "utilizacao": "Excelente para imagens de sobremesas com frutas, como tortas de frutas, sorvetes, smoothies, gelatinas e sobremesas refrescantes."
    },
    {
      "nome_paleta": "Mel & Canela",
      "cores": ["Âmbar", "Mel", "Canela", "Creme"],
      "utilizacao": "Perfeito para imagens de doces com sabores quentes e reconfortantes, como tortas de maçã, biscoitos de canela, bolos de mel e sobremesas com especiarias."
    },
    {
      "nome_paleta": "Arco-Íris",
      "cores": ["Vermelho vivo", "Laranja brilhante", "Amarelo vibrante", "Verde esmeralda", "Azul celeste", "Roxo vibrante"],
      "utilizacao": "Ideal para imagens de sobremesas coloridas e divertidas, como bolos de festa, cupcakes decorados, gelatinas coloridas e doces com cobertura colorida."
    },
    {
      "nome_paleta": "Gourmet",
      "cores": ["Ouro", "Prata", "Marrom escuro", "Roxo profundo"],
      "utilizacao": "Excelente para imagens de sobremesas elegantes e sofisticadas, como macarons gourmet, tortas finas, bombons artesanais e sobremesas de alta gastronomia."
    },
    {
      "nome_paleta": "Neutro & Elegante",
      "cores": ["Cinza pérola", "Marfim", "Bege", "Nude"],
      "utilizacao": "Ótimo para imagens de sobremesas com uma estética minimalista e elegante, destacando a textura e a apresentação dos doces sem cores muito vibrantes."
    },
    {
      "nome_paleta": "Sonho de Algodão",
      "cores": ["Rosa algodão doce", "Azul celeste", "Roxo lavanda", "Branco"],
      "utilizacao": "Ideal para imagens de sobremesas com uma atmosfera de conto de fadas, como algodão doce, cupcakes de unicórnio, sobremesas inspiradas em nuvens e sonhos."
    }
  ]
}
'''

json_posicionamento_camera_culinaria_doce = '''
{
  "posicionamento_camera_culinaria_doce": [
    {
      "posicao_camera": "Plongée (ângulo superior)",
      "descricao": "Posicionada acima da mesa, olhando para baixo em direção à comida. Ideal para capturar a disposição dos doces em uma mesa de sobremesas, mostrando a variedade de cores e texturas."
    },
    {
      "posicao_camera": "Nível da mesa",
      "descricao": "Colocada ao nível da mesa, na mesma altura dos doces. Oferece uma perspectiva frontal ou ligeiramente inclinada dos doces, destacando detalhes como coberturas, recheios e decorações."
    },
    {
      "posicao_camera": "Close-up",
      "descricao": "Focalizando de perto um único doce, utensílio ou ingrediente. Perfeito para capturar detalhes intricados, como texturas, camadas, enfeites ou até mesmo as bolhas de ar em um brigadeiro."
    },
    {
      "posicao_camera": "Plano geral",
      "descricao": "Capturando toda a cena da culinária de doces, incluindo a mesa, utensílios, ingredientes e os doces dispostos. Ótimo para estabelecer a atmosfera geral da preparação ou apresentação dos doces."
    },
    {
      "posicao_camera": "Foco seletivo",
      "descricao": "Destacando um doce específico em primeiro plano, enquanto o restante da cena permanece em segundo plano, levemente desfocado. Isso pode criar uma sensação de profundidade e destaque visual."
    },
    {
      "posicao_camera": "Macro",
      "descricao": "Utilizando uma lente macro para capturar detalhes extremamente próximos dos doces, revelando texturas minúsculas, como flocos de chocolate, cristais de açúcar ou grãos de café moído."
    }
  ]
}
'''

json_prompts_negativos_culinaria_doce = '''
{
  "prompts_negativos_culinaria_doce": [
    {
      "prompt": "Imagine uma sobremesa queimada e desfigurada, com uma crosta carbonizada e um interior seco e sem sabor.",
      "descricao": "Evoca uma imagem desagradável de uma sobremesa mal preparada, transmitindo a ideia de decepção e desperdício."
    },
    {
      "prompt": "Visualize uma loja de doces abandonada e decadente, com prateleiras vazias e doces mofados e estragados.",
      "descricao": "Sugere uma cena desoladora e desanimadora de uma loja de doces abandonada, transmitindo a ideia de decadência e abandono."
    },
    {
      "prompt": "Pense em um chef descontente derramando uma mistura de bolo grudenta e sem sabor em uma forma, com uma expressão de frustração.",
      "descricao": "Descreve uma cena frustrante e desanimadora de uma experiência culinária fracassada, sugerindo insatisfação e falta de habilidade."
    },
    {
      "prompt": "Imagine uma festa de aniversário arruinada por um bolo desmoronado e mal decorado, com velas quebradas e glacê derretido.",
      "descricao": "Evoca uma imagem decepcionante de uma festa de aniversário arruinada por uma sobremesa mal feita, transmitindo a ideia de constrangimento e fracasso."
    },
    {
      "prompt": "Visualize um confeiteiro desmotivado tentando decorar um bolo com glacê rachado e cores desbotadas, sem inspiração ou criatividade.",
      "descricao": "Sugere uma cena desanimadora de falta de motivação e habilidade na preparação de uma sobremesa, transmitindo a ideia de desinteresse e desânimo."
    },
    {
      "prompt": "Pense em uma cozinha bagunçada e suja, com utensílios sujos e ingredientes estragados espalhados pelo balcão.",
      "descricao": "Descreve uma cena desagradável e pouco higiênica de uma cozinha desorganizada, sugerindo a ideia de falta de cuidado e negligência na preparação de doces."
    },
    {
      "prompt": "Imagine uma sobremesa infectada por insetos e larvas, com ingredientes estragados e um odor repugnante.",
      "descricao": "Evoca uma imagem repugnante e desagradável de uma sobremesa contaminada por pragas, transmitindo a ideia de nojo e repulsa."
    },
    {
      "prompt": "Visualize um evento de degustação arruinado por sobremesas com sabores desagradáveis e texturas desagradáveis, deixando os convidados insatisfeitos.",
      "descricao": "Sugere uma cena decepcionante e frustrante de um evento culinário mal sucedido, transmitindo a ideia de fracasso e desapontamento."
    }
  ]
}
'''

json_prompts_positivos_culinaria_doce = '''
{
  "prompts_positivos_culinaria_doce": [
    {
      "prompt": "Imagine um bolo de aniversário decorado com confetes coloridos e velas brilhantes, pronto para celebrar uma ocasião especial.",
      "descricao": "Evoca uma imagem festiva e alegre de um bolo de aniversário, sugerindo celebração e felicidade."
    },
    {
      "prompt": "Visualize uma mesa repleta de cupcakes decorados com glacê colorido, delicadamente enfeitados com confeitos cintilantes.",
      "descricao": "Sugere uma cena encantadora e colorida de cupcakes decorados, transmitindo uma atmosfera divertida e apetitosa."
    },
    {
      "prompt": "Pense em um balcão de padaria com uma variedade de tortas de frutas frescas, com camadas de recheio suculento e uma crosta dourada e crocante.",
      "descricao": "Descreve uma cena tentadora de tortas de frutas frescas em uma padaria, despertando o apetite com imagens de sabores e texturas deliciosos."
    },
    {
      "prompt": "Imagine um chef decorando meticulosamente um bolo de casamento com flores de açúcar e detalhes intrincados, criando uma obra de arte comestível.",
      "descricao": "Evoca uma imagem elegante e refinada de um bolo de casamento decorado, sugerindo beleza, habilidade artística e sofisticação."
    },
    {
      "prompt": "Visualize um piquenique ensolarado com uma cesta cheia de biscoitos caseiros, recém-saídos do forno, com uma textura macia e um aroma tentador.",
      "descricao": "Sugere uma cena reconfortante e acolhedora de um piquenique ao ar livre, transmitindo a sensação de frescor e prazer de comer biscoitos caseiros."
    },
    {
      "prompt": "Pense em uma vitrine de doces em uma confeitaria elegante, com uma variedade de doces finos, desde trufas de chocolate até macarons coloridos.",
      "descricao": "Descreve uma cena luxuosa e sofisticada de uma confeitaria, sugerindo indulgência e uma variedade de sabores requintados."
    },
    {
      "prompt": "Imagine uma tarde chuvosa, onde você se aconchega com uma xícara de chocolate quente cremoso, coberto com marshmallows derretidos e raspas de chocolate.",
      "descricao": "Evoca uma sensação de conforto e indulgência, sugerindo uma cena aconchegante e reconfortante em um dia chuvoso."
    },
    {
      "prompt": "Visualize um jardim encantado com árvores frutíferas carregadas de frutas suculentas, prontas para serem colhidas e transformadas em deliciosas sobremesas.",
      "descricao": "Sugere uma cena mágica e inspiradora de um jardim fértil, transmitindo a ideia de frescor, abundância e possibilidades culinárias."
    }
  ]
}
'''