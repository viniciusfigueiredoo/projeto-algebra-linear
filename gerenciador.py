from matriz import Matriz

class Gerenciador:
    def __init__(self):
        self.matrizes = []

    def indice_valido(self, indice):
        if not self.matrizes:
            print("Nenhuma matriz cadastrada.")
            return False
        if indice < 0 or indice >= len(self.matrizes):
            print("Índice inválido.")
            return False
        return True

    def adicionar_matriz(self):
        i_final = int(input("Digite o número de linhas: "))
        j_final = int(input("Digite o número de colunas: "))

        matriz = Matriz(i_final, j_final)
        matriz.construir()
        self.matrizes.append(matriz)
        print("Matriz adicionada com sucesso.")

    def listar_matrizes(self):
        if not self.matrizes:
            print("Nenhuma matriz cadastrada.")
            return

        for indice, matriz in enumerate(self.matrizes):
            print(f"Matriz {indice}: {matriz.i_final}x{matriz.j_final}")

    def visualizar_matriz(self, indice):
        if not self.indice_valido(indice):
            return
        self.matrizes[indice].mostrar()

    def editar_matriz(self, indice):
        if not self.indice_valido(indice):
            return

        matriz = self.matrizes[indice]
        matriz.mostrar()

        i = int(input("Digite a linha do valor a editar: "))
        j = int(input("Digite a coluna do valor a editar: "))

        if i < 0 or i >= matriz.i_final or j < 0 or j >= matriz.j_final:
            print("Posição inválida.")
            return

        novo_valor = input("Digite o novo valor: ")
        matriz.matriz[i][j] = novo_valor

        print("Matriz atualizada:")
        matriz.mostrar()

    def deletar_matriz(self, indice):
        if not self.indice_valido(indice):
            return
        self.matrizes.pop(indice)
        print("Matriz removida.")