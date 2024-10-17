from models import Eleitor

eleitores_cadastrados = []

def cadastrar_eleitor():
    nome = input("Digite o nome do eleitor: ")
    endereco = input("Digite o endereco do eleitor: ")
    telefone = input("Digite o telefone do eleitor: ")
    secao = input("Digite a seção do eleitor: ")
    zona = input("Digite a zona do eleitor: ")
    data_nascimento = input("Digite a data de nascimento do eleitor: ")
    email = input("Digite o e-mail do eleitor: ")

    eleitor = Eleitor(nome, endereco, telefone, secao, zona, data_nascimento, email)
    eleitores_cadastrados.append(eleitor)
    print("\nEleitor cadastrado com sucesso!")
    print(eleitor)

def exibir_eleitores():
    if not eleitores_cadastrados:
        print("\nNenhum eleitor cadastrado até o momento")
    else:
        print("\n-- Eleitores Cadastrados --")
        for eleitor in eleitores_cadastrados:
            print(eleitor)
            print("--------------------------")

def main():
    while True:
        print("\n-- Sistema de Gerenciamento de Eleitores --")
        print("1. Cadastrar Eleitor")
        print("2. Exibir Eleitores Cadastrados")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_eleitor()
        elif opcao == "2":
            exibir_eleitores()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente")

if __name__ == "__main__":
    main()