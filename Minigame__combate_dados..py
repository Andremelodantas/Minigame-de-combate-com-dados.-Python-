from random import randint
from time import sleep

#Listagem dos personagens disponíveis para uso.
listaPersonagens = ['Scorpion',
                    'Sonya Blade',
                    'Jhonny Cage',
                    'Raiden',
                    'Sub-Zero',
                    'Liu Kang',
                    'Smoke',
                    'Ednaldo Pereira',
                    'Super Xandão']

def timer():
    sleep(1)

def pularLinha3():
    print('+' * 60)

def pularLinha():
    print(' ' * 60)

def pularLinha2():
    print('-' * 60)


print('Minigame de combate com dados.')

#Laço for para listar e enumerar todos os personagens para o jogador
for index, personagens in enumerate(listaPersonagens):
    print(index + 1, personagens)


#Criação de variáveis para que os jogadores escolham os seus personagens (com as validações)
pularLinha2()


entradaValida1 = False
entradaValida2 = False

while entradaValida1 is False:
    jogador1 = str(input('Jogador 1, escolha o seu personagem [Apenas Números]: '))
    if not jogador1.isnumeric():
        print('Inválido, tente novamente.')
    elif int(jogador1)>9 or int(jogador1)<1:
        print('Inválido, tente novamente.')
    else:
        Int1 = int(jogador1)
        entradaValida1 = True

while entradaValida2 is False:
    jogador2 = str(input('Jogador 2, escolha o seu personagem [Apenas Números]: '))
    if not jogador2.isnumeric():
        print('Inválido, tente novamente.')
    elif int(jogador2)>9 or int(jogador2)<1:
        print('Inválido, tente novamente.')
    else:
        Int2 = int(jogador2)
        entradaValida2 = True



#Criação de dois contadores referentes à vida total dos personagens
vidaJogador1=20
vidaJogador2=20

print('Iniciando o jogo...')
sleep(2)



#Laço while pra manter o jogo em andamento enquanto nenhum dos jogadores estiver com sua vida zerada
while vidaJogador1 or vidaJogador2 > 0:


#Conjunto de ações referentes ao movimento de ataque do jogador 1
    pularLinha2()
    pularLinha()
    print(f'{listaPersonagens[Int1 - 1]}, é sua vez de atacar')
    pularLinha()
    pularLinha2()
    acao1 = input('Role o dado [Digite qualquer tecla]')
    pularLinha2()
    timer()
    valorDadoJogador1 = randint(1, 15)
    pularLinha()
    pularLinha2()
    print('O valor de ataque foi igual a ', valorDadoJogador1)
    pularLinha2()

#Conjunto de ações referentes ao de defesa do jogador 2
    pularLinha()
    timer()
    print(f'{listaPersonagens[Int2 - 1]}, é sua vez de se defender')
    pularLinha()
    pularLinha2()
    acao2 = input('Role o dado [Digite qualquer tecla]')
    pularLinha2()
    timer()
    valorDadoJogador2 = randint(1, 15)
    pularLinha()
    pularLinha2()
    print('O valor de defesa foi igual a ', valorDadoJogador2)
    pularLinha2()

    pularLinha()
    sleep(1.5)

    pularLinha()


#Condicional para apresentar os resultados dos combates realizados
    if valorDadoJogador1 > valorDadoJogador2:
        dano = valorDadoJogador1 - valorDadoJogador2
        vidaJogador2 = vidaJogador2 - dano
        pularLinha3()
        print('{}, sua vida diminuiu em {} unidades. Vida total atual: {}.'.format(listaPersonagens[Int1 - 1],dano, vidaJogador2))
        pularLinha3()
    elif valorDadoJogador1 <= valorDadoJogador2:
        pularLinha3()
        print('Defesa prevaleceu')
        pularLinha3()


    pularLinha()
    pularLinha()
    pularLinha2()

    if vidaJogador1 <= 0:
        print('''Parabéns {}, você venceu!
                 Jogo encerrado.'''.format(listaPersonagens[Int2 - 1]))
        break
    elif vidaJogador2 <= 0:
        print('''Parabéns {}, você venceu!
                 Jogo encerrado.'''.format(listaPersonagens[Int1 - 1]))
        break

    print('Iniciando a segunda parte Round!')
    sleep(1.5)

#Cojunto de ações referentes ao ataque do jogador 2
    pularLinha2()
    pularLinha()
    print('{}, é sua vez de atacar'.format(listaPersonagens[Int2 - 1]))
    pularLinha()
    pularLinha2()
    acao1 = input('Role o dado [Digite qualquer tecla]')
    pularLinha2()
    timer()
    pularLinha()
    valorDadoJogador2 = randint(1, 15)
    pularLinha2()
    print('O valor de ataque foi igual a ', valorDadoJogador2)
    pularLinha2()


#Conjunto de ações referentes à defesa do jogador 1
    pularLinha()
    timer()
    print('{}, é sua vez de se defender'.format(listaPersonagens[Int1 - 1]))
    pularLinha()
    pularLinha2()
    acao2 = input('Role o dado [Digite qualquer tecla]')
    pularLinha2()
    timer()
    pularLinha()
    pularLinha2()
    valorDadoJogador1 = randint(1, 15)
    print('O valor de defesa foi igual a ', valorDadoJogador1)
    pularLinha2()

    pularLinha()
    sleep(1.5)
    pularLinha()


#Condicional para apresentar os resultados dos combates realizados
    if valorDadoJogador2 > valorDadoJogador1:
        dano = valorDadoJogador2 - valorDadoJogador1
        vidaJogador1 = vidaJogador1 - dano
        pularLinha3()
        print('{}, sua vida diminuiu {}, agora ela está com {}.'.format(listaPersonagens[Int2 - 1],dano, vidaJogador1))
        pularLinha3()
    elif valorDadoJogador2 <= valorDadoJogador1:
        pularLinha3()
        print('Defesa prevaleceu')
        pularLinha3()


    pularLinha()
    pularLinha2()

    print('Carregando...')
    pularLinha2()
    pularLinha()
    sleep(1.5)

#Condicionais para finalizar o jogo quando a vida de lgum dos jogadores chegar a zero
    if vidaJogador1 <= 0 :
        print('''Parabéns {}, você venceu!
                 Jogo encerrado.'''.format(listaPersonagens[Int2 - 1]))
        break
    elif vidaJogador2 <= 0 :
        print('''Parabéns {}, você venceu!
                 Jogo encerrado.'''.format(listaPersonagens[Int1 - 1]))
        break
