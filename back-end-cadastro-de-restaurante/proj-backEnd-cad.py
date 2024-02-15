import os

restaurantes = [{'nome': 'Burguers do Nahu', 'categoria': 'Lanches', 'ativo': False},
                {'nome': 'Huan spetoz', 'categoria': 'Carnes', 'ativo': True},
                {'nome': 'Huan sushis', 'categoria': 'Japonesa', 'ativo': True}]

def exibir_nome_do_programa():
    """ Função responsável por exibir o nome do programa """

    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    """ Função responsável por exibir as opções disponíveis no programa """

    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar/Desativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    """ Função responsável por finalizar a execução do programa """

    exibir_subtitulo("Encerrando o programa")

def voltar_ao_menu_principal():
    """ Função responsável por voltar ao menu principal """

    input("\n>>> Digite uma tecla para voltar ao menu: ")
    main()

def opcao_invalida():
    """ Função responsável por dizer que a opção escolhida é inválida e voltar ao menu principal """

    print("Opção inválida! Tente novamente...\n")

    voltar_ao_menu_principal()

def exibir_subtitulo(subtitulo):
    """ Função responsável por exibir o subtítulo da opção escolhida """

    os.system('cls')
    linha = '*' * (len(subtitulo) + 4)
    print(linha)
    print(f"* {subtitulo} *")
    print(f"{linha}\n")

def cadastrar_novo_restaurante():
    """ Função responsável por cadastrar um novo restaurante 
    
    INPUTS:
    - Nome do restaurante
    - Categoria do restaurante
    - Dados do restaurante

    OUTPUTS:    
    - Adiciona os dados de um restaurante cadastrado ao dicionário "restaurantes"
    - Imprime na tela o nome do novo restaurante cadastrado
    
    """

    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante \"{nome_do_restaurante}\": ")
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante \"{nome_do_restaurante}\" foi cadastrado com sucesso!")

    voltar_ao_menu_principal()

def listar_restaurantes():
    """ Função responsável por listar todos os restaurantes já cadastrados """

    exibir_subtitulo("Listando os restaurantes")

    print(f"{">>> Nome do Restaurante".ljust(33)} | {">>> Categoria do Restaurante".ljust(30)} | >>> Status\n")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = "Ativado" if restaurante['ativo'] else "Desativado"
        
        print(f"-> {nome_restaurante.ljust(30)} | {categoria_restaurante.ljust(30)} | {ativo}")

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    """ Função responsável por ativar/desativar um restaurante já cadastrado """

    exibir_subtitulo("Alternando estado do restaurante")

    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

            mensagem = f"O restaurante \"{nome_restaurante}\" foi ativado com sucesso!" if restaurante['ativo'] else f"O restaurante \"{nome_restaurante}\" foi desativado com sucesso!"
            print(mensagem)

    if not restaurante_encontrado:
        print(f"O restaurante \"{nome_restaurante}\" não foi encontrado nos restaurantes já cadastrados")

    voltar_ao_menu_principal()

def escolher_opcao():
    """ Função responsável por capturar a escolha de opção do usuário e executar uma função correspondente a essa escolha """

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    """ Função raíz - aquela que será a função inicial para o funcionamento do programa """

    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()