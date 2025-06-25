personagens=[]
def exibir_menu():
    while True:
        print('Menu sobre o personagem')
        print('1- Cadastrar novo personagem')
        print('2- Consultar personagens')
        print('3- Buscar por classe')
        print('4- Aumentar nível de um personagem')
        print('5- Sair')
        escolha=str(input('Escolha uma opção: '))
        if escolha=='1':
            cadastrar_personagem()
        elif escolha=='2':
            consultar_personagens()
        elif escolha=='3':
            buscar_por_classe()
        elif escolha=='4':
            aumentar_nivel_personagem()
        elif escolha=='5':
            print('Até a próxima aventura 😎')
            break
        else:
            print('Opção inválida.\n')
def cadastrar_personagem():
    nome = input('Digite o nome do personagem: ')
    classe = input('Qual a classe do personagem (Guerreiro, Mago, Arqueiro, Ladrão, Paladino e Druida): ')
    try:
        nivel = int(input('Qual o nível do personagem (1 a 5): '))
        if nivel < 1 or nivel > 5:
            print('Nível fora do permitido deve ser entre 1 e 5.\n')
            return
    except ValueError:
        print('Digite um número inteiro.\n')
        return
    print('Personagem cadastrado com sucesso!')
    habilidade=str(input('Qual é a habilidade especial (Fogo, Velocidade, Cura, Gelo, Invisibilidade): '))
    confirmar=str(input('Confirmar cadastro?(s/n): '))
    if confirmar.lower()=='s':
        personagem={
            'Nome':nome,
            'Classe':classe,
            'Nível':nivel,
            'Habilidade':habilidade}
        personagens.append(personagem)
        print('Personagem cadastrado com sucesso!\n')
    else:
        print('Cadastro cancelado.\n')
def consultar_personagens():
    if len(personagens) ==0:
        print('Personagem cadastrado.\n')
        return
    contador =1
    for personagem in personagens:
        print(f"[{contador}]Nome:{personagem['Nome']}|Classe:{personagem['Classe']}|Nível:{personagem['Nível']}")
        contador +=1
    print()
def buscar_por_classe():
    classe=str(input('Digite a classe que deseja buscar: '))
    achou=False
    for personagem in personagens:
        if personagem['Classe'].lower()==classe.lower():
            print(f'{personagem['Nome']} - Nível {personagem['Nível']} - Habilidade: {personagem['Habilidade']}')
            achou=True
    if not achou:
        print('Nenhum personagem encontrado nessa classe.\n')
def aumentar_nivel_personagem():
    consultar_personagens()
    if len(personagens) == 0:
        return
    try:
        numero=int(input('Digite o número do personagem que deseja aumentar o nível: '))
        indice=numero-1
        if 0 <=indice<len(personagens):
            personagens[indice]['Nível'] +=1
            print(f"Nível do personagem '{personagens[indice]['Nome']}'aumentado para {personagens[indice]['Nível']}.\n")
        else:
            print('Número de personagem inválido.\n')
    except ValueError:
        print('Número invalido.\n')
exibir_menu()