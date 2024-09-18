import os

restaurantes = [{'nome': 'churascaria bom gosto', 'categoria:': 'churasco', 'ativo': True}, 
                {'nome': 'pizza sagrada', 'categoria': 'italiana', 'ativo': False}, 
                {'nome': 'kioto', 'categoria': 'japonesa', 'ativo': False}]

def exibir_nome_do_programa():
    print('𝓢𝓪𝓫𝓸𝓻 𝓮𝔁𝓹𝓻𝓮𝓼𝓼\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
  exibir_subtitolu('Finalizando app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar no menu pricipal: ')
    main()

def opcao_invalida():
    print('Opção inválida!!!\n')
    voltar_ao_menu_principal()

def exibir_subtitolu(texto):
    os.system('cls')
    print(texto)

def cadastrar_novo_restaurante():
    exibir_subtitolu('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitolu('Listando os restaurantes\n')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo =restaurante['ativo']
        print(f'-{nome_restaurante} | {categoria} | {ativo}')
        voltar_ao_menu_principal()


def escolher_opcao():
     try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()

     except:
         opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
