import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.json.ensure_ascii = False

# Datas dos ensaios (passados e futuros). Formato: data AAAA-MM-DD e lista "detalhes" (uma linha por horário).
# Para adicionar um ensaio, inclua um novo item na lista abaixo.
ENSAIOS = [
    {
        "data": "2026-10-31",
        "detalhes": [
            "16:00 – Peça: cenas 1, 2, 3 e 4"
        ]
    },
    {
        "data": "2026-11-01",
        "detalhes": [
            "14:00 – Peça: cenas 5, 6 e 7"
        ]
    },
    {
        "data": "2026-11-08",
        "detalhes": [
            "14:00 às 16:00 – Peça: cenas 8, 9 e 10",
            "16:00 às 18:00 – Coral"
        ]
    },
    {
        "data": "2026-11-14",
        "detalhes": [
            "14:00 – Coral",
            "16:00 – Peça: cenas 1, 2, 3 e 4"
        ]
    },
    {
        "data": "2026-11-15",
        "detalhes": [
            "14:00 às 16:00 – Coral",
            "16:00 às 18:00 – Peça: cenas 5, 6 e 7"
        ]
    },
    {
        "data": "2026-11-22",
        "detalhes": [
            "14:00 às 16:00 – Ensaio geral",
            "16:00 às 18:00 – Coral"
        ]
    },
    {
        "data": "2026-11-29",
        "detalhes": [
            "14:00 às 16:00 – Ensaio geral",
            "16:00 às 18:00 – Coral"
        ]
    },
    {
        "data": "2026-12-05",
        "detalhes": [
            "13:00 – Ensaio geral da peça e do coral"
        ]
    },
    {
        "data": "2026-12-06",
        "detalhes": [
            "Apresentação"
        ]
    }
]

# Responsáveis por departamento (fotos em static/fotos/)
RESPONSAVEIS = [
    {
        "id": "roteiro",
        "nome": "Roteiro",
        "pessoas": [
            {
                "nome": "Felipe",
                "foto": "felipe.jpg"
            },
            {
                "nome": "Leonardo",
                "foto": "leonardo.jpg"
            },
            {
                "nome": "Nickizinho",
                "foto": "nickizinho.jpg"
            }
        ]
    },
    {
        "id": "ensaios",
        "nome": "Ensaios",
        "pessoas": [
            {
                "nome": "Henrique",
                "foto": "henrique.jpg"
            },
            {
                "nome": "Ruan",
                "foto": "ruan.jpg"
            },
            {
                "nome": "Vinicius",
                "foto": "vinicius.jpg"
            }
        ]
    },
    {
        "id": "luz-e-som",
        "nome": "Luz e som",
        "pessoas": [
            {
                "nome": "Eduardo",
                "foto": "eduardo.jpg"
            },
            {
                "nome": "Julia",
                "foto": "julia.jpg"
            },
            {
                "nome": "Nicolas Augusto",
                "foto": "nicolas-augusto.jpg"
            }
        ]
    },
    {
        "id": "figurino",
        "nome": "Figurino",
        "pessoas": [
            {
                "nome": "Dennys",
                "foto": "dennys.jpg"
            },
            {
                "nome": "Maria Eduarda",
                "foto": "maria-eduarda.jpg"
            },
            {
                "nome": "Mayara",
                "foto": "mayara.jpg"
            }
        ]
    },
    {
        "id": "pascom",
        "nome": "Pascom e divulgação",
        "pessoas": [
            {
                "nome": "Leonardo",
                "foto": "leonardo.jpg"
            },
            {
                "nome": "Luanni",
                "foto": "luanni.jpg"
            },
            {
                "nome": "Maria Sophia",
                "foto": "maria-sophia.jpg"
            }
        ]
    },
    {
        "id": "coral",
        "nome": "Coral",
        "pessoas": [
            {
                "nome": "Julia",
                "foto": "julia.jpg"
            },
            {
                "nome": "Maria Eduarda",
                "foto": "maria-eduarda.jpg"
            }
        ]
    }
]

ROTEIRO = [
 {
  "id": 1,
  "titulo": "Cena 1",
  "sub": "Evangelho de Lucas",
  "personagens": [
   "Lucas"
  ],
  "itens": [
   {
    "t": "r",
    "txt": "Abre as cortinas com Lucas segurando um livro, uma luz acompanha Lucas"
   },
   {
    "t": "f",
    "nome": "Lucas",
    "who": [
     "Lucas"
    ],
    "emo": "Animado",
    "txt": "Tenho uma linda história para contar, mas não uma história qualquer, uma história que começou muito antes de mim de Maria de José e de ti.\nEssa história começa com uma promessa feita por Deus.\nDurante séculos o povo esperou por um líder, um rei, um salvador e cada profeta anunciou isso de uma forma, vejam!"
   },
   {
    "t": "r",
    "txt": "Lucas abre o livro e lê as promessas"
   },
   {
    "t": "f",
    "nome": "Lucas",
    "who": [
     "Lucas"
    ],
    "emo": "",
    "txt": "Em Isaías capítulo 7 diz; Eis que a virgem concebeu e dará à luz um filho.\nEm Miquéias capítulo 5; O Salvador nascerá em Belém e será o pastor que reunirá e protegerá seu povo.\nE em 2° Samuel capítulo 7, está escrito que Deus promete a Davi uma descendência e um reino que durará para sempre."
   },
   {
    "t": "r",
    "txt": "Fecha o livro"
   },
   {
    "t": "f",
    "nome": "Lucas",
    "who": [
     "Lucas"
    ],
    "emo": "",
    "txt": "Uma virgem, um menino, Belém, uma estrela e uma profecia, as palavras foram ditas e o tempo se passou , reis nasceram e reis morreram, impérios surgiram e a palavra permaneceu, e então a história começou, não muito distante em um templo com um sacerdote chamado Zacarias."
   },
   {
    "t": "r",
    "txt": "Fecham-se as cortinas"
   }
  ]
 },
 {
  "id": 2,
  "titulo": "Cena 2",
  "sub": "Lucas 1:5-25",
  "personagens": [
   "Zacarias",
   "Anjo Gabriel",
   "Povo 1",
   "Povo 3",
   "Povo 2"
  ],
  "itens": [
   {
    "t": "r",
    "txt": "Abre-se as cortinas, em cena Zacarias e povo"
   },
   {
    "t": "r",
    "txt": "Zacarias sai do meio do povo para oferecer o incenso a Deus e surge o Anjo"
   },
   {
    "t": "r",
    "txt": "Gabriel"
   },
   {
    "t": "r",
    "txt": "Zacarias chega com o incenso e pede licença ao povo para acender o carvão e se retira para fazer suas orações no templo"
   },
   {
    "t": "f",
    "nome": "Zacarias",
    "who": [
     "Zacarias"
    ],
    "emo": "Calmo",
    "txt": "Deus de meus antepassados, trago aqui as orações de meu povo para que as receba através da fumaça deste incenso."
   },
   {
    "t": "r",
    "txt": "Anjo Gabriel atrás de algo no cenário aparece de supetão"
   },
   {
    "t": "r",
    "txt": "som de anjo ÓÓÓÓóóó"
   },
   {
    "t": "f",
    "nome": "Anjo Gabriel",
    "who": [
     "Anjo Gabriel"
    ],
    "emo": "Confiante",
    "txt": "Não temas Zacarias suas orações foram ouvidas, tua mulher Isabel, te dará um filho homem e tu lhe colocarás o nome de João. Será para ti motivo de orgulho e de alegria, e muitos se alegrarão no seu nascimento; porque ele será grande diante do Senhor, não beberá vinho nem outra bebida que contenha álcool, será cheio do Espírito Santo desde o ventre de sua mãe e converterá muitos dos filhos de Israel ao Senhor seu Deus. Irá adiante de Deus com o espírito e a fortaleza do profeta Elias."
   },
   {
    "t": "f",
    "nome": "Zacarias",
    "who": [
     "Zacarias"
    ],
    "emo": "Assustado/em dúvida",
    "txt": "Como isso irá acontecer ? Eu sou velho e minha mulher também EU DUVIDO! E o que você está falando? Eu nem te conheço."
   },
   {
    "t": "f",
    "nome": "Anjo Gabriel",
    "who": [
     "Anjo Gabriel"
    ],
    "emo": "Indignado",
    "txt": "Estás louco !… Eu sou Gabriel o anjo enviado por Deus,para te anunciar a boa nova, você ainda por cima duvida de mim."
   },
   {
    "t": "r",
    "txt": "Pausa indignado, balançando a cabeça"
   },
   {
    "t": "f",
    "nome": "Anjo Gabriel",
    "who": [
     "Anjo Gabriel"
    ],
    "emo": "",
    "txt": "Visto que não acreditaste nas minhas palavras, ficarás mudo, e não poderás falar até ao dia em que estas coisas acontecerem."
   },
   {
    "t": "r",
    "txt": "Anjo Gabriel sai de cena e Zacarias volta ao povo gesticulando"
   },
   {
    "t": "f",
    "nome": "Zacarias",
    "who": [
     "Zacarias"
    ],
    "emo": "Mudo",
    "txt": "Gesticula pedindo ao povo para que se sentem, que o anjo, anunciou um filho a ele e o deixou mudo."
   },
   {
    "t": "f",
    "nome": "Povo 1",
    "who": [
     "Povo 1"
    ],
    "emo": "Em dúvida",
    "txt": "Zacarias Deus escutou nossas orações? …."
   },
   {
    "t": "f",
    "nome": "Zacarias",
    "who": [
     "Zacarias"
    ],
    "emo": "Mudo",
    "txt": "Positivo"
   },
   {
    "t": "f",
    "nome": "Povo 3",
    "who": [
     "Povo 3"
    ],
    "emo": "Pouco indignado",
    "txt": "Responde … porque não falas, estas mudo ?"
   },
   {
    "t": "f",
    "nome": "Zacarias",
    "who": [
     "Zacarias"
    ],
    "emo": "Mudo",
    "txt": "Gesticula que viu um anjo do Senhor"
   },
   {
    "t": "f",
    "nome": "Povo 2",
    "who": [
     "Povo 2"
    ],
    "emo": "Intensificando indignação",
    "txt": "O que quer dizer com isto, porque fala com as mãos… viu um anjo?"
   },
   {
    "t": "f",
    "nome": "Zacarias",
    "who": [
     "Zacarias"
    ],
    "emo": "Mudo",
    "txt": "Positivo e indica que ficou mudo."
   },
   {
    "t": "f",
    "nome": "Povo 3",
    "who": [
     "Povo 3"
    ],
    "emo": "Esclarecimento",
    "txt": "Ficou mudo por ter uma visão?"
   },
   {
    "t": "f",
    "nome": "Zacarias",
    "who": [
     "Zacarias"
    ],
    "emo": "Mudo",
    "txt": "Positivo"
   },
   {
    "t": "f",
    "nome": "Povo 1",
    "who": [
     "Povo 1"
    ],
    "emo": "Entendimento e dúvida",
    "txt": "O que está visão revelastes a ti?"
   },
   {
    "t": "f",
    "nome": "Zacarias",
    "who": [
     "Zacarias"
    ],
    "emo": "Mudo",
    "txt": "Um filho MEU"
   },
   {
    "t": "f",
    "nome": "Povo 2",
    "who": [
     "Povo 2"
    ],
    "emo": "Tom de esclarecimento",
    "txt": "Ele teve uma visão, ficou mudo por conta dela e terá um filho mesmo depois de velho?"
   },
   {
    "t": "f",
    "nome": "Zacarias",
    "who": [
     "Zacarias"
    ],
    "emo": "Mudo",
    "txt": "Positivo"
   },
   {
    "t": "r",
    "txt": "Povo comemora ardentemente e grita saindo: Vamos comemorar!!"
   },
   {
    "t": "r",
    "txt": "Fecha-se as cortinas"
   }
  ]
 },
 {
  "id": 3,
  "titulo": "Cena 3",
  "sub": "Lucas 1:26-38",
  "personagens": [
   "Narrador",
   "Maria",
   "Anjo Gabriel"
  ],
  "itens": [
   {
    "t": "r",
    "txt": "Abre-se as cortinas, em cena Maria e Gabriel Gabriel anuncia a Nossa Senhora a concepção do menino Jesus mesmo sendo virgem."
   },
   {
    "t": "f",
    "nome": "Narrador",
    "who": [
     "Narrador"
    ],
    "emo": "",
    "txt": "Estando Isabel no sexto mês, foi enviado por Deus, o anjo Gabriel, a uma cidade da Galileia chamada Nazaré, a uma virgem desposada com um varão, chamado José da casa de David; O nome da virgem era Maria."
   },
   {
    "t": "r",
    "txt": "Maria se ajoelha e começa a rezar"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Rezando",
    "txt": "Senhor, meu Deus, eu vos agradeço por tudo o que fizestes em minha vida, por minha família, por vosso amor e por todas as graças que recebi."
   },
   {
    "t": "r",
    "txt": "Pausa."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Rezando",
    "txt": "Hoje, mais uma vez, entrego a minha vida em vossas mãos. Que eu possa sempre fazer a vossa vontade e permanecer fiel a Vós, aconteça o que acontecer. Conduzi os meus passos, Senhor, e fazei de mim aquilo que desejais. Eu confio em Vós e entrego a Vós toda a minha vida."
   },
   {
    "t": "r",
    "txt": "Maria permanece em silêncio. Nesse momento, entra o Anjo Gabriel."
   },
   {
    "t": "f",
    "nome": "Anjo Gabriel",
    "who": [
     "Anjo Gabriel"
    ],
    "emo": "Entusiasmado",
    "txt": "Ave cheia de graça, o senhor é convosco!"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Espantada",
    "txt": "Cheia de graça? O que isso significa?"
   },
   {
    "t": "f",
    "nome": "Anjo Gabriel",
    "who": [
     "Anjo Gabriel"
    ],
    "emo": "Orgulhoso",
    "txt": "Não temas, Maria, teu nome já estava nos planos de Deus desde o princípio, fostes escolhida entre as virgens! Eis que receberá no teu ventre, e darás à luz um filho, que deverá ter o nome de Jesus.\nEle será grande, será chamado Filho do Altíssimo, e o Senhor Deus lhe dará o trono de seu pai Davi; reinará sobre a casa de Jacó eternamente, e o seu reino não terá fim."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Perturbada",
    "txt": "Como isso acontecerá?! Não conheço Homem algum!"
   },
   {
    "t": "f",
    "nome": "Anjo Gabriel",
    "who": [
     "Anjo Gabriel"
    ],
    "emo": "Confiante",
    "txt": "O Espírito Santo descerá sobre você, e a virtude do Altíssimo te cobrirá com a sua luz; por isso mesmo o Menino que nascerá de ti, será santo e será chamado Filho de Deus. Eis que também Isabel, tua prima, recebeu um filho na sua velhice, aquela que todos diziam infértil, já está no sexto mês de gestação, porquê para Deus nada é impossível."
   },
   {
    "t": "r",
    "txt": "Silêncio, Maria olha para o anjo e faz uma afirmação com a cabeça"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Afirmando",
    "txt": "\"Eis aqui a serva do Senhor, faça-se em mim segunda a tua palavra.”"
   },
   {
    "t": "r",
    "txt": "Anjo sai de cena e Maria segue sorrindo e serena, com as mãos na barriga e cortinas se fecham"
   }
  ]
 },
 {
  "id": 4,
  "titulo": "Cena 4",
  "sub": "Lucas 1:39-45",
  "personagens": [
   "Narrador",
   "Maria",
   "Isabel"
  ],
  "itens": [
   {
    "t": "r",
    "txt": "Abre-se as cortinas, em cena Maria e Isabel Maria visita sua prima e as duas se alegram perante suas gestações"
   },
   {
    "t": "f",
    "nome": "Narrador",
    "who": [
     "Narrador"
    ],
    "emo": "",
    "txt": "Logo pela manhã Maria, foi com pressa às montanhas, a uma cidade de Judá para visitar sua prima, Isabel."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Muito Alegre",
    "txt": "Minha querida prima, como está?"
   },
   {
    "t": "r",
    "txt": "João salta alegremente no ventre de Isabel por estar na presença do Senhor"
   },
   {
    "t": "r",
    "txt": "Ambas riem com a presença de João"
   },
   {
    "t": "f",
    "nome": "Isabel",
    "who": [
     "Isabel"
    ],
    "emo": "Alegre",
    "txt": "Bendita és tu entre todas as mulheres, e bendito é o fruto do teu ventre. A que mereço a visita da Mãe do meu Salvador? Logo que ouvi sua voz o menino saltou em meu ventre, ó cheia de graça! Bendita sejas tu, que acreditou nas palavras do Senhor."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Afirmação",
    "txt": "A minha alma glorifica o Senhor; e o meu espírito alegra em Deus meu Salvador, porque olhou para sua serva. Portanto, de hoje em diante, todas as gerações me chamarão de bem-aventurada. Pois em mim fez grandes coisas, o seu nome é santo e sua misericórdia não terá fim. Manifestou teu poder e tirou os poderosos do trono e os entregou aos humildes. Deu de comer aos pobres e arrancou os tesouros dos ricos. Cuidou de Israel mostrando sua misericórdia. Como prometeu aos nossos pais."
   },
   {
    "t": "f",
    "nome": "Isabel",
    "who": [
     "Isabel"
    ],
    "emo": "Agradecendo",
    "txt": "Que bom é receber tua benção sobre mim, minhas orações foram ouvidas por Deus o Senhor."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Aconselhando",
    "txt": "A importância de nunca desistir das orações é exatamente essa, devemos sempre entender que tudo é no tempo Dele, e não devemos nos apavorar com as situações, Deus sabe de todas as coisas."
   },
   {
    "t": "f",
    "nome": "Isabel",
    "who": [
     "Isabel"
    ],
    "emo": "Agradecendo",
    "txt": "A sua sabedoria realmente vem do alto, agora minhas orações serão apenas de agradecimento, afinal terei o filho que sempre sonhei."
   },
   {
    "t": "r",
    "txt": "Zacarias entra em cena mudo, MUITO FELIZ, pois, viu Maria em sua casa!"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Pergunta",
    "txt": "Oi Zacarias, quanto tempo? … Por que Zacarias não fala comigo?"
   },
   {
    "t": "f",
    "nome": "Isabel",
    "who": [
     "Isabel"
    ],
    "emo": "Afirmativa",
    "txt": "Maria, Zacarias está mudo!"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Desentendida",
    "txt": "Mas como ele ficou assim?"
   },
   {
    "t": "f",
    "nome": "Isabel",
    "who": [
     "Isabel"
    ],
    "emo": "Explicando",
    "txt": "Zacarias foi ao templo, fazer suas orações diárias, e voltou mudo."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Desentendida",
    "txt": "Mas como assim Isabel? Me explica isso direito!"
   },
   {
    "t": "f",
    "nome": "Isabel",
    "who": [
     "Isabel"
    ],
    "emo": "Esclarecendo",
    "txt": "Exatamente dessa forma, Zacarias entrou no templo e saiu mudo. Como dizem: São os planos de Deus, Maria. E você prima, fiquei sabendo que está noiva, já o conheceu ? Como ele é ?, vou preparar o café, enquanto me conta tudo."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Alegre",
    "txt": "Eu o conheci e ele parece ser um homem segundo o coração de Deus."
   },
   {
    "t": "f",
    "nome": "Isabel",
    "who": [
     "Isabel"
    ],
    "emo": "Curiosa",
    "txt": "Mas como ele é fisicamente, qual cor de cabelo? Ele tem barba?"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Descrevendo",
    "txt": "Ele tem barba, cabelo curto, ele também é alto, um homem admirável."
   },
   {
    "t": "f",
    "nome": "Narrador",
    "who": [
     "Narrador"
    ],
    "emo": "Sério",
    "txt": "Maria ficou com Isabel cerca de três meses; depois voltou para sua casa."
   }
  ]
 },
 {
  "id": 5,
  "titulo": "Cena 5",
  "sub": "Mateus 1:18-25",
  "personagens": [
   "Narrador",
   "Maria",
   "José",
   "Anjo dos sonhos de José"
  ],
  "itens": [
   {
    "t": "r",
    "txt": "José descobre que Maria está grávida e recebe a mensagem do anjo"
   },
   {
    "t": "f",
    "nome": "Narrador",
    "who": [
     "Narrador"
    ],
    "emo": "Sério",
    "txt": "Após o casamento, Maria encontra-se sozinha com José"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Séria",
    "txt": "José, preciso conversar com você algo muito sério, aconteceu uma coisa que mudará completamente nossas vidas."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Compreensivo",
    "txt": "O que houve, você parece muito preocupada. Maria, minha esposa, agora que estamos casados, não deve me esconder nada, me conte o que você quiser!"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Apreensiva",
    "txt": "Eu estou com medo José."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Confiante",
    "txt": "Não precisa ter medo meu amor, pode confiar em mim, a partir de hoje, sou teu esposo e sempre farei de tudo pelo seu bem."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Séria",
    "txt": "José… Um anjo do Senhor veio até mim, e disse que eu sou a escolhida para receber o filho de Deus, então de repente eu fiquei grávida."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Descrente",
    "txt": "Maria isto é sério? Você está grávida? Que história é essa que um anjo veio até você? Eu acho que preciso de um tempo para orar e pensar em tudo o que você está me falando."
   },
   {
    "t": "r",
    "txt": "São José pega o “colchão” que estava do lado de Maria e leva ao outro lado do palco para “dormir”"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Rezando",
    "txt": "Meu Senhor, hoje eu me casei com Maria, estou muito feliz, porém, depois da festa, Maria veio até mim, e disse que está grávida, pois um anjo contou isso para ela. Eu não sei como reagir com tudo isso, está tudo muito confuso em minha cabeça, mas sei que o Senhor consegue me ajudar."
   },
   {
    "t": "r",
    "txt": "José dorme"
   },
   {
    "t": "r",
    "txt": "som de Óóóóóó´´ e o anjo entra em cena"
   },
   {
    "t": "f",
    "nome": "Anjo dos sonhos de José",
    "who": [
     "Anjo dos sonhos de José"
    ],
    "emo": "Desesperado",
    "txt": "José, José, acorda, eu preciso falar com você!"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Assustado",
    "txt": "Meu Deus, mas quem é você que está invadindo a minha casa!"
   },
   {
    "t": "f",
    "nome": "Anjo dos sonhos de José",
    "who": [
     "Anjo dos sonhos de José"
    ],
    "emo": "Confiante",
    "txt": "Eu vim dar a luz do seu caminho, conforme pediu em suas orações a Deus. José, filho de Davi, não tenha medo de receber tua esposa, Maria, na sua vida, porque o que nela foi concebido é obra do Espírito Santo. Ela dará à luz um filho, que deve se chamar Jesus, porque ele salvará o seu povo dos seus pecados. Tudo isto aconteceu para que se cumprisse a promessa do Senhor, que dizia: Eis que a Virgem dará à luz um filho, e terá o nome de Jesus, que significa: Deus conosco."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Incrédulo",
    "txt": "veja se eu entendi bem, então EU um simples carpinteiro, serei o pai do filho de Deus ?"
   },
   {
    "t": "f",
    "nome": "Anjo dos sonhos de José",
    "who": [
     "Anjo dos sonhos de José"
    ],
    "emo": "Respondendo",
    "txt": "Filho de Davi não se rebaixe, você foi o escolhido por Deus para cuidar de seu Filho o messias. você encontrou graça no coração de Deus por suas virtudes e sua fé inabalável. Não temas José, pois o Senhor teu Deus está contigo."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Descrente",
    "txt": "Isso só pode ser um sonho!"
   },
   {
    "t": "f",
    "nome": "Anjo dos sonhos de José",
    "who": [
     "Anjo dos sonhos de José"
    ],
    "emo": "Sereno",
    "txt": "Você está sonhando. Depois de tudo isso, cuide bem de Maria e Jesus."
   },
   {
    "t": "r",
    "txt": "som de josé acordando"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Sério",
    "txt": "Maria, acorde, rezei muito a Deus ontem… Sonhei com um anjo… Diante do meu sonho e de tudo o que me contou… Eu acredito em Você, vou cuidar de nossa família."
   },
   {
    "t": "r",
    "txt": "Se abraçam e fecha as cortinas"
   }
  ]
 },
 {
  "id": 6,
  "titulo": "Cena 6",
  "sub": "Lucas 2:1–7",
  "personagens": [
   "Mensageiro",
   "Povo 4",
   "Povo 5",
   "José",
   "Povo 6",
   "Maria"
  ],
  "itens": [
   {
    "t": "r",
    "txt": "Abra as cortina"
   },
   {
    "t": "r",
    "txt": "No meio estará José e o povo ouvindo os dizeres do Mensageiro"
   },
   {
    "t": "f",
    "nome": "Mensageiro",
    "who": [
     "Mensageiro"
    ],
    "emo": "Sério",
    "txt": "Por determinação de César Augusto, Imperador de Roma, fica decretado o recenseamento de todos os homens do Império.Cada homem deverá dirigir-se à sua cidade de origem, conforme o registro de sua família, para realizar o devido cadastro. Todos aqueles sob o domínio do Império Romano estão sujeitos a este decreto e deverão cumprir esta determinação dentro do prazo estabelecido.O cumprimento desta ordem é obrigatório para todos os homens abrangidos pelo decreto.Que cada homem se prepare para a viagem e cumpra fielmente a ordem do Imperador."
   },
   {
    "t": "f",
    "nome": "Povo 4",
    "who": [
     "Povo 4"
    ],
    "emo": "Confuso",
    "txt": "O que ele disse? Eu não escutei muito bem."
   },
   {
    "t": "r",
    "txt": "Povo 5 Puxa José que está um pouco mais perto do Mensageiro"
   },
   {
    "t": "f",
    "nome": "Povo 5",
    "who": [
     "Povo 5"
    ],
    "emo": "Eufórico",
    "txt": "José.. José, você estava mais próximo, onde ele nos mandou ir?"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Calmo",
    "txt": "Gente, calma! eu vou explicar para todos vocês. O mensageiro me disse que cada um terá que ir para sua terra natal, para realizar o recenseamento."
   },
   {
    "t": "f",
    "nome": "Povo 5",
    "who": [
     "Povo 5"
    ],
    "emo": "Confuso",
    "txt": "Recenseamento? O que é isso ?"
   },
   {
    "t": "f",
    "nome": "Povo 6",
    "who": [
     "Povo 6"
    ],
    "emo": "Indignado",
    "txt": "Eu sou de Nazaré, vou ter que ir até lá? Isso vai demorar dias."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Explicativo",
    "txt": "Fique calmo, o recenseamento é um registro que o Imperador César Augusto quer fazer com os homens que estão sob o controle do Império Romano."
   },
   {
    "t": "r",
    "txt": "Povo 4,5,6 vão saindo gritando junto(CADA UM SUA FALA)"
   },
   {
    "t": "f",
    "nome": "Povo 4",
    "who": [
     "Povo 4"
    ],
    "emo": "Indignado",
    "txt": "Meu Deus, como pode isso? Vou ter que andar Quilômetros para assinar um papel."
   },
   {
    "t": "f",
    "nome": "Povo 5",
    "who": [
     "Povo 5"
    ],
    "emo": "Indignado",
    "txt": "César quer saber quantos homens tem para nos colocar em suas guerras!"
   },
   {
    "t": "f",
    "nome": "Povo 6",
    "who": [
     "Povo 6"
    ],
    "emo": "Indignado",
    "txt": "O que esse tal de César quer de mim?"
   },
   {
    "t": "r",
    "txt": "Maria puxa josé com delicadeza da multidão para o canto"
   },
   {
    "t": "r",
    "txt": "Joga-se a Luz no casal José e Maria"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Tranquila",
    "txt": "José o que ele estava falando? Eu estava longe, não ouvi muito bem."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Apreensivo",
    "txt": "Maria, ele falou sobre um decreto de César, precisarei partir para Belém, minha cidade de origem, para fazer o registro do império."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Confiante",
    "txt": "Eu irei junto contigo!"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Preocupado",
    "txt": "Mas você está prestes a dar a Luz, não está nas melhores condições para uma viagem dessas, podemos encontrar com tempestades e temporais, isso poderia fazer muito mal a sua saúde ."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Decidida",
    "txt": "Eu sei de tudo isso e entendo sua preocupação ! Mas nós somos uma família, não quero deixar você ir sozinho. Deus que nos trouxe até aqui, não vai ser agora que ele irá nos abandonar."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Sério",
    "txt": "Você me convenceu, vou confiar no que Deus nos preparou, vou arrumar nossas malas e partimos de imediato."
   },
   {
    "t": "r",
    "txt": "Fecham-se as cortinas"
   }
  ]
 },
 {
  "id": 7,
  "titulo": "Cena 7",
  "sub": "Lucas 2:8–14",
  "personagens": [
   "Pastor 1",
   "Pastor 2",
   "Pastor 3",
   "Anjo 1"
  ],
  "itens": [
   {
    "t": "r",
    "txt": "Abram-se as cortinas"
   },
   {
    "t": "r",
    "txt": "Pastores na fogueira conversando"
   },
   {
    "t": "f",
    "nome": "Pastor 1",
    "who": [
     "Pastor 1"
    ],
    "emo": "Tranquilo",
    "txt": "Olha que céu lindo, as ovelhas apascentadas , que noite tranquila para se viver em Belém."
   },
   {
    "t": "f",
    "nome": "Pastor 2",
    "who": [
     "Pastor 2"
    ],
    "emo": "Desafiando",
    "txt": "Até agora, não se esqueça que está acontecendo o recenseamento na cidade."
   },
   {
    "t": "f",
    "nome": "Pastor 3",
    "who": [
     "Pastor 3"
    ],
    "emo": "Dúvida",
    "txt": "O que é recenseamento?"
   },
   {
    "t": "f",
    "nome": "Pastor 2",
    "who": [
     "Pastor 2"
    ],
    "emo": "Explicativo",
    "txt": "O recenseamento é um registro que o Imperador César Augusto quer fazer com os homens que estão sob o controle do Império Romano."
   },
   {
    "t": "f",
    "nome": "Pastor 3",
    "who": [
     "Pastor 3"
    ],
    "emo": "Apreensivo",
    "txt": "Não falem isso, toda vez que vocês comentam, algo acontece!"
   },
   {
    "t": "f",
    "nome": "Pastor 1",
    "who": [
     "Pastor 1"
    ],
    "emo": "Descarado",
    "txt": "Que exagero! Nada vai acontecer"
   },
   {
    "t": "f",
    "nome": "Pastor 2",
    "who": [
     "Pastor 2"
    ],
    "emo": "Brincando",
    "txt": "Tomara mesmo, porque eu já estou cansado de andar de um lado para o outro."
   },
   {
    "t": "f",
    "nome": "Pastor 3",
    "who": [
     "Pastor 3"
    ],
    "emo": "Relaxando",
    "txt": "ÉÉÉÉ, eu só quero terminar essa noite em paz."
   },
   {
    "t": "f",
    "nome": "Pastor 1",
    "who": [
     "Pastor 1"
    ],
    "emo": "Rindo",
    "txt": "Então para de ficar preocupado, e olhe para o céu."
   },
   {
    "t": "r",
    "txt": "Todos olham para o céu"
   },
   {
    "t": "f",
    "nome": "Pastor 2",
    "who": [
     "Pastor 2"
    ],
    "emo": "Pensativo",
    "txt": "Vocês já pensaram que Deus pode estar preparando algo incrível para nós essa noite."
   },
   {
    "t": "f",
    "nome": "Pastor 1",
    "who": [
     "Pastor 1"
    ],
    "emo": "Descontraído",
    "txt": "Deus sempre está preparando algo, mas não acho que vai acontecer justo aqui."
   },
   {
    "t": "f",
    "nome": "Pastor 3",
    "who": [
     "Pastor 3"
    ],
    "emo": "Preocupado",
    "txt": "Não fala isso…"
   },
   {
    "t": "r",
    "txt": "Entra o anjo ÓÓÓóóó"
   },
   {
    "t": "f",
    "nome": "Pastor 1",
    "who": [
     "Pastor 1"
    ],
    "emo": "Assustado",
    "txt": "O QUE É ISSO?"
   },
   {
    "t": "f",
    "nome": "Pastor 3",
    "who": [
     "Pastor 3"
    ],
    "emo": "Debochado",
    "txt": "Olha lá… eu falei !"
   },
   {
    "t": "f",
    "nome": "Anjo 1",
    "who": [
     "Anjo 1"
    ],
    "emo": "Alegre",
    "txt": "Não tenham medo , porque vos anuncio uma boa nova, que será de grande alegria para todo o povo: Nasceu hoje na cidade de Davi um Salvador, que é o Cristo, o Senhor. Vão e encontrem um Menino, ele estará envolto em panos, e deitado numa manjedoura.\""
   },
   {
    "t": "r",
    "txt": "Entra o coro dos celestial cantando"
   },
   {
    "t": "f",
    "nome": "Coro celestial",
    "who": [
     "Coro celestial"
    ],
    "emo": "",
    "txt": "\"Glória a Deus no mais alto dos céus, e paz na terra aos homens, objecto da boa vontade (de Deus).\""
   },
   {
    "t": "r",
    "txt": "Música: Nosso Deus Viu, de 1:06 a 1:27"
   },
   {
    "t": "r",
    "txt": "Saem de cena todos os anjos"
   },
   {
    "t": "f",
    "nome": "Pastor 3",
    "who": [
     "Pastor 3"
    ],
    "emo": "Entusiasmado",
    "txt": "Vamos até a cidade de Belém, e vejamos o que é que o Senhor nos manifestou."
   },
   {
    "t": "f",
    "nome": "Pastor 2",
    "who": [
     "Pastor 2"
    ],
    "emo": "Entusiasmado",
    "txt": "Então anda logo…"
   },
   {
    "t": "r",
    "txt": "Pastor 2 empurra o Pastor 1 e ele cai tropeçando no chão"
   },
   {
    "t": "f",
    "nome": "Pastor 1",
    "who": [
     "Pastor 1"
    ],
    "emo": "Desesperado",
    "txt": "Ei, me esperem, eu quero ir junto!"
   },
   {
    "t": "f",
    "nome": "Pastor 2 / Pastor 3",
    "who": [
     "Pastor 2",
     "Pastor 3"
    ],
    "emo": "Ansiosos",
    "txt": "Então levanta, vamos!"
   },
   {
    "t": "r",
    "txt": "Saem de cena os pastores e se fecha as cortinas"
   }
  ]
 },
 {
  "id": 8,
  "titulo": "Cena 8",
  "sub": "Lucas 2:8-14",
  "personagens": [
   "Gaspar",
   "Belchior",
   "Baltazar",
   "Soldado",
   "Herodes",
   "Sacerdote"
  ],
  "itens": [
   {
    "t": "r",
    "txt": "Abra-se as cortinas"
   },
   {
    "t": "f",
    "nome": "Gaspar",
    "who": [
     "Gaspar"
    ],
    "emo": "Confiante",
    "txt": "Finalmente chegamos em Jerusalém."
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Reclamando",
    "txt": "Que camelo desconfortável e que viagem longa."
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Confiante",
    "txt": "Pelo menos chegamos!"
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Confiante",
    "txt": "Agora que chegamos, temos que falar com O Rei."
   },
   {
    "t": "f",
    "nome": "Gaspar",
    "who": [
     "Gaspar"
    ],
    "emo": "Entusiasmado",
    "txt": "Vamos falar com aquele soldado, ele deve saber onde está o Rei dos judeus."
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Gentil",
    "txt": "Com licença senhor somos Gaspar, Belchior e Baltazar, Magos de uma terra distante do oriente e viemos visitar o Rei dos Judeus."
   },
   {
    "t": "f",
    "nome": "Soldado",
    "who": [
     "Soldado"
    ],
    "emo": "Bravo",
    "txt": "O que vocês querem com Herodes?"
   },
   {
    "t": "f",
    "nome": "Gaspar",
    "who": [
     "Gaspar"
    ],
    "emo": "Entusiasmado",
    "txt": "Viemos trazer presentes para ele."
   },
   {
    "t": "f",
    "nome": "Soldado",
    "who": [
     "Soldado"
    ],
    "emo": "Bravo",
    "txt": "Venham comigo, os levarei até o Rei dos judeus."
   },
   {
    "t": "r",
    "txt": "Soldado faz reverência a Herodes"
   },
   {
    "t": "f",
    "nome": "Soldado",
    "who": [
     "Soldado"
    ],
    "emo": "Sério",
    "txt": "Rei Herodes eis aqui Baltazar, Gaspar e Belchior."
   },
   {
    "t": "f",
    "nome": "Herodes",
    "who": [
     "Herodes"
    ],
    "emo": "Dúvida",
    "txt": "Quem são vocês?"
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Respeitoso",
    "txt": "Olá vossa alteza, somos 3 magos do Oriente e estávamos ansiosos por essa visita."
   },
   {
    "t": "f",
    "nome": "Herodes",
    "who": [
     "Herodes"
    ],
    "emo": "Dúvida",
    "txt": "Como chegaram até mim?"
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Entusiasmado",
    "txt": "Através de uma estrela que fez um clarão nos céus do Oriente, e que fez nossos olhos encherem de esperança para encontrar o Senhor."
   },
   {
    "t": "f",
    "nome": "Herodes",
    "who": [
     "Herodes"
    ],
    "emo": "Desconfiado",
    "txt": "Uma estrela? E o que vocês querem de mim?"
   },
   {
    "t": "f",
    "nome": "Gaspar",
    "who": [
     "Gaspar"
    ],
    "emo": "Respeito",
    "txt": "Vossa alteza,com todo o devido respeito, viemos conhecer e adorar o novo Rei dos Judeus que acaba de nascer, viemos de muito longe e até presentes trouxemos para essa ilustre visita, queremos que ele receba nossa mirra,\nincenso e ouro para mostrar nossa gratidão. Por isso viemos perguntar para você onde o encontramos."
   },
   {
    "t": "r",
    "txt": "Herodes chamou um dos príncipes atrás dele"
   },
   {
    "t": "f",
    "nome": "Herodes",
    "who": [
     "Herodes"
    ],
    "emo": "Sussurrando",
    "txt": "Sacerdote, ele está falando do Rei dos Judeus? o Messias?"
   },
   {
    "t": "f",
    "nome": "Sacerdote",
    "who": [
     "Sacerdote"
    ],
    "emo": "Sério",
    "txt": "Rei Herodes, eu acredito que estão falando dele mesmo, o Messias, o Rei dos Judeus."
   },
   {
    "t": "f",
    "nome": "Herodes",
    "who": [
     "Herodes"
    ],
    "emo": "Sussurrando",
    "txt": "Fala baixo, eles não podem escutar. Você sabe onde ele irá nascer?"
   },
   {
    "t": "f",
    "nome": "Sacerdote",
    "who": [
     "Sacerdote"
    ],
    "emo": "Sussurrando",
    "txt": "Em Belém de Judá, porque assim foi escrito pelo profeta: E tu, Belém, terra de Judá, de modo algum é a menor entre as principais cidades de Judá, porque de ti sairá um chefe, que acolherá Israel, meu povo."
   },
   {
    "t": "f",
    "nome": "Herodes",
    "who": [
     "Herodes"
    ],
    "emo": "Imponência",
    "txt": "Vão até Belém de judá, lá acharam o Messias, e quando encontrá-lo volte e me comuniquem, para que eu possa adorá-lo também."
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Atencioso",
    "txt": "Muito obrigado por nos ajudar, pode contar com a gente, assim que encontrarmos o lugar onde o grande Messias está, voltaremos para contar ao Senhor."
   },
   {
    "t": "r",
    "txt": "Sai os 3 magos, e fica somente o Herodes e seu Sacerdote"
   },
   {
    "t": "f",
    "nome": "Herodes",
    "who": [
     "Herodes"
    ],
    "emo": "Furioso",
    "txt": "Soldado, venha aqui!"
   },
   {
    "t": "f",
    "nome": "Soldado",
    "who": [
     "Soldado"
    ],
    "emo": "Autoritário",
    "txt": "Estou aqui Senhor, o que precisas."
   },
   {
    "t": "f",
    "nome": "Herodes",
    "who": [
     "Herodes"
    ],
    "emo": "Autoritário",
    "txt": "Recrute seus melhores soldados, e os preparem para quando os 3 magos voltarem. Iremos para Belém, para encontrar esse Rei dos Judeus, e faremos de tudo para que ele morra, assim manterei minha coroa."
   },
   {
    "t": "f",
    "nome": "Soldado",
    "who": [
     "Soldado"
    ],
    "emo": "Imponente",
    "txt": "Pode deixar Chefe, farei de tudo para selecionar os melhores soldados. E faremos o melhor para concluir sua missão."
   },
   {
    "t": "r",
    "txt": "fechando as cortinas"
   }
  ]
 },
 {
  "id": 9,
  "titulo": "Cena 9",
  "sub": "Mt 2, 12-13",
  "personagens": [
   "Gaspar",
   "Belchior",
   "Baltazar",
   "Anjo 2"
  ],
  "itens": [
   {
    "t": "r",
    "txt": "Abre-se as cortinas"
   },
   {
    "t": "f",
    "nome": "Gaspar",
    "who": [
     "Gaspar"
    ],
    "emo": "Cansado",
    "txt": "Meus amigos, acho que nosso dia já foi longo demais, podemos descansar um pouco, amanhã teremos um grande dia."
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Afirmando",
    "txt": "Concordo, apesar de que meu espírito esteja ansioso para conhecer o Messias, meu corpo pede uma pausa."
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Sonolento",
    "txt": "Então vamos descansar, amanhã continuaremos nossa jornada."
   },
   {
    "t": "r",
    "txt": "dormem os magos"
   },
   {
    "t": "r",
    "txt": "SOM DE SONO ZZZzzzzz"
   },
   {
    "t": "r",
    "txt": "entra o anjo em cena para acordar os magos"
   },
   {
    "t": "f",
    "nome": "Anjo 2",
    "who": [
     "Anjo 2"
    ],
    "emo": "Urgência",
    "txt": "Acorda baltazar! acorda belchior!"
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Assustado",
    "txt": "O que foi?"
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Assustado",
    "txt": "Quem é você? Gaspar acorda!"
   },
   {
    "t": "r",
    "txt": "sacode Gaspar"
   },
   {
    "t": "f",
    "nome": "Anjo 2",
    "who": [
     "Anjo 2"
    ],
    "emo": "Confiante",
    "txt": "Eu sou um anjo enviado por Deus e tenho algo muito importante para falar para vocês três."
   },
   {
    "t": "f",
    "nome": "Gaspar",
    "who": [
     "Gaspar"
    ],
    "emo": "Ansioso",
    "txt": "Então nos diga a mensagem de Deus."
   },
   {
    "t": "f",
    "nome": "Anjo 2",
    "who": [
     "Anjo 2"
    ],
    "emo": "Sério",
    "txt": "Deus me enviou para alertar vocês, a mensagem é que vocês não devem voltar para Jerusalém para avisar Herodes, devem voltar para o oriente por outro caminho."
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Dúvida",
    "txt": "Mas por que não devemos voltar para Jerusalém ?"
   },
   {
    "t": "f",
    "nome": "Anjo 2",
    "who": [
     "Anjo 2"
    ],
    "emo": "Sério",
    "txt": "O orgulho de Herodes o cegou e, fez com que ele amasse sua coroa acima de seu amor por Deus. Por causa disso ele planeja segui-los até o Messias e depois MATÁ-LO !"
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Surpreso",
    "txt": "Então aquele discurso de Herodes sobre querer adorar o menino era mentira?"
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Bravo",
    "txt": "Que homem traiçoeiro, nos mandou procurar o menino somente para descobrir onde ele estava."
   },
   {
    "t": "f",
    "nome": "Anjo 2",
    "who": [
     "Anjo 2"
    ],
    "emo": "Afirmando",
    "txt": "Exatamente. Por isso não devem voltar para o Rei Herodes. Não permitam que o caminho que vocês trilharam seja usado contra o Messias."
   },
   {
    "t": "f",
    "nome": "Gaspar",
    "who": [
     "Gaspar"
    ],
    "emo": "Sério",
    "txt": "Somos enviados para presenteá-lo, não deixaremos que nada de mal aconteça."
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Desesperado",
    "txt": "Mas e agora como vamos saber qual caminho seguir?"
   },
   {
    "t": "f",
    "nome": "Anjo 2",
    "who": [
     "Anjo 2"
    ],
    "emo": "Autoritário",
    "txt": "Não se preocupem, Deus está com vocês."
   },
   {
    "t": "f",
    "nome": "Anjo 2",
    "who": [
     "Anjo 2"
    ],
    "emo": "Autoritário",
    "txt": "Agora vão, façam a vontade dele!"
   },
   {
    "t": "r",
    "txt": "eles voltam para a cama, e depois Gaspar acorda"
   },
   {
    "t": "f",
    "nome": "Gaspar",
    "who": [
     "Gaspar"
    ],
    "emo": "Ansioso/assustado",
    "txt": "Amigos acordem rápido, sonhei com vocês e tinha um anjo também e ele trazia uma mensagem ….."
   },
   {
    "t": "r",
    "txt": "é interrompido por Baltazar"
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Confuso",
    "txt": "Uma mensagem dizendo para não voltarmos para Jerusalém e que..."
   },
   {
    "t": "r",
    "txt": "é interrompido por Belchior"
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Surpreso",
    "txt": ".... E que Herodes queria matar o Menino!!!"
   },
   {
    "t": "f",
    "nome": "Gaspar / Belchior / Baltazar",
    "who": [
     "Gaspar",
     "Belchior",
     "Baltazar"
    ],
    "emo": "Surpresos",
    "txt": "Estávamos todos no mesmo sonho!"
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Orgulhoso",
    "txt": "Certamente isso foi uma mensagem de Deus, e devemos seguir o que o anjo nos disse!"
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Agitado",
    "txt": "Já está de manhã, vamos levantar depressa, dar água aos camelos e partir para nossa jornada, que Deus proteja o Messias e também proteja nossos passos."
   },
   {
    "t": "r",
    "txt": "3 Magos se levantam saem, Fecha-se as cortinas"
   }
  ]
 },
 {
  "id": 10,
  "titulo": "Cena 10",
  "sub": "Nascimento de Jesus",
  "personagens": [
   "José",
   "Maria",
   "Hospedeiro",
   "Pastor 1",
   "Pastor 2",
   "Pastor 3",
   "Gaspar",
   "Belchior",
   "Baltazar",
   "Anjo 3",
   "Anjo 4",
   "Anjo 5",
   "Anjo 6"
  ],
  "itens": [
   {
    "t": "r",
    "txt": "Abre as cortinas"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Aliviado",
    "txt": "Finalmente chegamos em Belém. Maria como você está?"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Calma",
    "txt": "Estou bem José, só estou cansada"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Cansado",
    "txt": "Precisamos encontrar uma hospedaria para descansarmos,e deixar para amanhã o registro para o recenseamento."
   },
   {
    "t": "r",
    "txt": "José vai procurar algum lugar nas hospedagens para dormirem"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Atencioso",
    "txt": "Boa noite senhor!"
   },
   {
    "t": "f",
    "nome": "Hospedeiro",
    "who": [
     "Hospedeiro"
    ],
    "emo": "Respeitoso",
    "txt": "Boa noite."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Pedindo",
    "txt": "Minha esposa e eu precisamos de um lugar para ficar esta noite, nossa viagem foi longa e ela está grávida."
   },
   {
    "t": "f",
    "nome": "Hospedeiro",
    "who": [
     "Hospedeiro"
    ],
    "emo": "Desinteressado",
    "txt": "Sinto muito, não temos mais lugar para vocês, a cidade está cheia, por conta do recenseamento."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Súplica",
    "txt": "Senhor, nós não precisamos de muito, apenas uma cama para minha esposa descansar."
   },
   {
    "t": "f",
    "nome": "Hospedeiro",
    "who": [
     "Hospedeiro"
    ],
    "emo": "Afirmando",
    "txt": "Não há lugar na hospedaria."
   },
   {
    "t": "r",
    "txt": "José volta para Maria triste"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Triste",
    "txt": "Maria aqui também não tem lugar."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Calma",
    "txt": "Não se preocupe José, Deus irá prover o necessário para nós."
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Calmo",
    "txt": "Você sempre sabe o que dizer, sou grato a Deus por ter me entregado uma mulher tão doce e serena."
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Desesperada",
    "txt": "José… Acho que chegou a hora"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Desesperado",
    "txt": "Precisamos encontrar um lugar urgentemente, talvez tenha um lugar aqui perto"
   },
   {
    "t": "f",
    "nome": "Maria",
    "who": [
     "Maria"
    ],
    "emo": "Calorosa",
    "txt": "José você não está me entendendo AGORA !!"
   },
   {
    "t": "r",
    "txt": "Fecha as cortinas"
   },
   {
    "t": "r",
    "txt": "um som de choro de bebê bem alto"
   },
   {
    "t": "f",
    "nome": "José",
    "who": [
     "José"
    ],
    "emo": "Empolgado falando ainda com cortinas fechadas",
    "txt": "NASCEU MEU FILHO,"
   },
   {
    "t": "r",
    "txt": "E o nome dele será jesus"
   },
   {
    "t": "r",
    "txt": "Abra-se as cortinas a manjedoura no centro, Maria e José ao lado"
   },
   {
    "t": "f",
    "nome": "Pastor 1",
    "who": [
     "Pastor 1"
    ],
    "emo": "Duvidoso",
    "txt": "É aqui ! O anjo disse que encontraremos o menino envolto em panos e deitado numa manjedoura."
   },
   {
    "t": "r",
    "txt": "Pastor 1 se ajoelha diante da manjedoura"
   },
   {
    "t": "f",
    "nome": "Pastor 2",
    "who": [
     "Pastor 2"
    ],
    "emo": "Alegre",
    "txt": "O anúncio do Anjo se cumpriu e ele está exatamente como nos foi dito"
   },
   {
    "t": "r",
    "txt": "Pastor 2 se ajoelha diante da manjedoura"
   },
   {
    "t": "f",
    "nome": "Pastor 3",
    "who": [
     "Pastor 3"
    ],
    "emo": "Feliz",
    "txt": "O salvador Nasceu."
   },
   {
    "t": "r",
    "txt": "Pastor 3 se ajoelha diante da manjedoura"
   },
   {
    "t": "r",
    "txt": "Reis magos aparecem"
   },
   {
    "t": "f",
    "nome": "Gaspar",
    "who": [
     "Gaspar"
    ],
    "emo": "Sério",
    "txt": "A estrela nos trouxe até aqui"
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Sério",
    "txt": "Depois de uma longa jornada finalmente encontramos o Rei que procurávamos"
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Sério",
    "txt": "Aquele que nasceu para trazer a salvação ao seu povo"
   },
   {
    "t": "r",
    "txt": "Os reis magos se aproximam da manjedoura, falam do presente que trouxeram e o entregam e depois se ajoelham."
   },
   {
    "t": "f",
    "nome": "Belchior",
    "who": [
     "Belchior"
    ],
    "emo": "Exaltando",
    "txt": "Receba o ouro Digno de um rei."
   },
   {
    "t": "f",
    "nome": "Gaspar",
    "who": [
     "Gaspar"
    ],
    "emo": "Exaltando",
    "txt": "Receba o incenso como sinal de adoração."
   },
   {
    "t": "f",
    "nome": "Baltazar",
    "who": [
     "Baltazar"
    ],
    "emo": "Exaltando",
    "txt": "Receba mirra como um sinal de reverência."
   },
   {
    "t": "r",
    "txt": "Entra os anjos com som ÓÓÓóóóóo"
   },
   {
    "t": "f",
    "nome": "Anjo 3",
    "who": [
     "Anjo 3"
    ],
    "emo": "Entusiasmado",
    "txt": "Durante séculos, o povo esperou… Esperou pelo Rei anunciado pelos profetas Esperou pelo Salvador prometido por Deus"
   },
   {
    "t": "r",
    "txt": "Anjo olha para Jesus."
   },
   {
    "t": "f",
    "nome": "Anjo 4",
    "who": [
     "Anjo 4"
    ],
    "emo": "Entusiasmado",
    "txt": "E hoje, diante dos nossos olhos… A promessa se cumpriu. O Rei nasceu O Salvador chegou A Luz veio ao mundo"
   },
   {
    "t": "f",
    "nome": "Anjo 5",
    "who": [
     "Anjo 5"
    ],
    "emo": "Entusiasmado",
    "txt": "Aquele que foi anunciado pelos profetas, aquele que foi esperado por tantas gerações, está aqui… O Filho de Deus, Jesus Cristo"
   },
   {
    "t": "r",
    "txt": "Todos olham para Jesus."
   },
   {
    "t": "f",
    "nome": "Anjo 6",
    "who": [
     "Anjo 6"
    ],
    "emo": "Entusiasmado",
    "txt": "Glória a Deus nas alturas! E paz na terra aos homens de bem. Hoje, Belém não recebeu apenas um menino… Recebeu o Salvador do mundo"
   },
   {
    "t": "r",
    "txt": "O anjo se ajoelha diante de Jesus."
   },
   {
    "t": "r",
    "txt": "Todos cantam a música de Natal"
   }
  ]
 }
]


@app.route("/")
def index():
    return render_template("index.html", roteiro=ROTEIRO, ensaios=ENSAIOS, responsaveis=RESPONSAVEIS)


@app.route("/api/roteiro")
def api_roteiro():
    return jsonify(ROTEIRO)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
