class Matriz:
    def __init__(self, i_final=0, j_final=0):
        self.i_final = i_final
        self.j_final = j_final
        self.matriz = []

    def construir(self):
        # Cria a matriz vazia
        for i in range(self.i_final):
            self.matriz.append(["?"] * self.j_final)

        i = 0
        j = 0

        while i < self.i_final:
            self.mostrar()
            valor = input('Digite o próximo valor ou apague o anterior com "!": ')

            if valor == "!":
                if i == 0 and j == 0:
                    print("Não há valores para apagar.")
                    continue

                if j == 0:
                    i -= 1
                    j = self.j_final - 1
                else:
                    j -= 1
                self.matriz[i][j] = "?"
            else:
                self.matriz[i][j] = valor
                j += 1

                if j == self.j_final:
                    j = 0
                    i += 1
        self.mostrar()

        while True:
            decisao = input("Você quer trabalhar com essa matriz? (S/N)").upper()

            if decisao == 'S':
                print("Matriz guardada.")
                return self.matriz
            elif decisao == 'N':
                print("Matriz descartada.")
                self.matriz.clear()
                break
            else:
                print("Reponda direito pelo amor do bom pastor.")

    def mostrar(self):
        for linha in self.matriz:
            print("[ " + " ".join(str(valor) for valor in linha) + " ]")
        print()

