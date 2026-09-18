from gerenciador import Gerenciador
from operacoes import Operacoes

def menu():
    print(
        "\nSelecione uma operação:\n"
        "1. Adicionar matriz\n"
        "2. Listar matrizes\n"
        "3. Visualizar matriz\n"
        "4. Editar matriz\n"
        "5. Deletar matriz\n"
        "6. Verificar comutativa (A + B)\n"
        "7. Verificar associativa (A + B + C)\n"
        "8. Verificar elemento neutro\n"
        "9. Verificar elemento oposto\n"
        "0. Sair"
    )

def pedir_indice(mensagem):
    return int(input(mensagem))

def main():
    gerenciador = Gerenciador()
    operacoes = Operacoes()

    while True:
        menu()
        escolha = input("Digite o número da operação: ")

        if escolha == "1":
            gerenciador.adicionar_matriz()

        elif escolha == "2":
            gerenciador.listar_matrizes()

        elif escolha == "3":
            indice = pedir_indice("Digite o índice da matriz: ")
            gerenciador.visualizar_matriz(indice)

        elif escolha == "4":
            indice = pedir_indice("Digite o índice da matriz: ")
            gerenciador.editar_matriz(indice)

        elif escolha == "5":
            indice = pedir_indice("Digite o índice da matriz: ")
            gerenciador.deletar_matriz(indice)

        elif escolha == "6":
            i_a = pedir_indice("Índice da matriz A: ")
            i_b = pedir_indice("Índice da matriz B: ")
            if gerenciador.indice_valido(i_a) and gerenciador.indice_valido(i_b):
                operacoes.verificar_comutativa(gerenciador.matrizes[i_a], gerenciador.matrizes[i_b])

        elif escolha == "7":
            i_a = pedir_indice("Índice da matriz A: ")
            i_b = pedir_indice("Índice da matriz B: ")
            i_c = pedir_indice("Índice da matriz C: ")
            if gerenciador.indice_valido(i_a) and gerenciador.indice_valido(i_b) and gerenciador.indice_valido(i_c):
                operacoes.verificar_associativa(gerenciador.matrizes[i_a], gerenciador.matrizes[i_b], gerenciador.matrizes[i_c])

        elif escolha == "8":
            i_a = pedir_indice("Índice da matriz A: ")
            if gerenciador.indice_valido(i_a):
                operacoes.verificar_elemento_neutro(gerenciador.matrizes[i_a])

        elif escolha == "9":
            i_a = pedir_indice("Índice da matriz A: ")
            if gerenciador.indice_valido(i_a):
                operacoes.verificar_elemento_oposto(gerenciador.matrizes[i_a])

        elif escolha == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()