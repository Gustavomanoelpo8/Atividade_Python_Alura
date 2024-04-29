#os é uma das bibliotecas em python
import os

#lista de restaurantes
restaurantes=[]

#limpar o codigo
def clear():
    os.system('cls')

#variavel para finalizar o e limpar o terminal
def finalizar_app():
    clear()
    print('programa finalzado\n')

#menu principal
def exibir_nome():
    print('''

█▀▀ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 █▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
▀▀█ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 █▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ▀▀▀ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀

''')
    
#menu de opções
def exibir_opções():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. ativar restaurante')
    print('4. sair\n')    

def opcao_invalida():
    print('opcao invalida\n')
    input('digite uma tecla para voltar a opção princial')
    main()

#função para recolher o nome do restaurante
def cadastrar_restaurantes():
        clear()
        print('cadastrar novo restaurante')
        nome_restaurante = input('digite o nome do restaurante: ')
#append para colocar o nome do restaurante na lista
        restaurantes.append(nome_restaurante)
        print(f'o restaurante {nome_restaurante} foi cadastrado com sucecsso')
        input('digite uma tecla para voltar ao menu principal')
        main()


def escolher_opções():
    try:
        opção_escolhida = int(input('escolha uma opção:'))
        print(f' você escolheu a opção {opção_escolhida}')

    #tabela de opções
        if opção_escolhida == 1:
            cadastrar_restaurantes()
        elif opção_escolhida == 2:
            print('listar resutante')
        elif opção_escolhida == 3:
            print('ativar resturante')
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        print('opção inválida')
        input('digite uma opção válida')
        main()
       

#arquivo main
def main():
    clear()
    exibir_nome()
    exibir_opções()
    escolher_opções()



if __name__ == '__main__':
    main()