class Operacoes:

    def somar(self, matriz_a, matriz_b):
        # Verifica se são de mesmo tamanho
        if matriz_a.i_final != matriz_b.i_final or matriz_a.j_final != matriz_b.j_final:
            print("As matrizes precisam ter as mesmas dimensões para serem somadas.")
            return None

        resultado = []
        for i in range(matriz_a.i_final):
            linha = []
            for j in range(matriz_a.j_final):
                linha.append(matriz_a.matriz[i][j] + matriz_b.matriz[i][j])
            resultado.append(linha)

        return resultado

    def comparar(self, matriz_1, matriz_2):
        contador = 0

        # Verifica se são de mesmo tamanho
        if len(matriz_1) != len(matriz_2) or len(matriz_1[0]) != len(matriz_2[0]):
            print("Matrizes com dimensões diferentes não podem ser comparadas.")
            return False, contador

        iguais = True
        for i in range(len(matriz_1)):
            for j in range(len(matriz_1[0])):
                contador += 1
                if matriz_1[i][j] != matriz_2[i][j]:
                    iguais = False

        return iguais, contador

    def verificar_comutativa(self, matriz_a, matriz_b):
        a_mais_b = self.somar(matriz_a, matriz_b)
        b_mais_a = self.somar(matriz_b, matriz_a)

        # Retorna nada caso sejam de tamanhos diferentes
        if a_mais_b is None or b_mais_a is None:
            return

        iguais, contador = self.comparar(a_mais_b, b_mais_a)

        print(f"A + B == B + A? {iguais}")
        print(f"Número de comparações realizadas: {contador}")

    def gerar_matriz_neutra(self, i_final, j_final):
        return [[0 for x in range(j_final)] for x in range(i_final)]

    def verificar_elemento_neutro(self, matriz_a):
        # Gera matriz neutra (elementos = 0) com as mesmas dimensões da matriz_a
        neutra = self.gerar_matriz_neutra(matriz_a.i_final, matriz_a.j_final)

        # "Empacota" a lista pura 'neutra' dentro de um objeto Matriz,
        # porque o método somar() espera objetos com .i_final, .j_final e .matriz
        matriz_neutra_obj = type(matriz_a)(matriz_a.i_final, matriz_a.j_final)
        matriz_neutra_obj.matriz = neutra

        # Soma A + 0, resultando em uma lista pura ou None, caso as dimensões não batam
        a_mais_neutra = self.somar(matriz_a, matriz_neutra_obj)

        if a_mais_neutra is None:
            return

        iguais, contador = self.comparar(a_mais_neutra, matriz_a.matriz)

        print(f"A + 0 == A? {iguais}")
        print(f"Número de comparações realizadas: {contador}")

    def gerar_matriz_oposta(self, matriz_a):
        oposta = []

        for i in range(matriz_a.i_final):
            linha = []
            for j in range(matriz_a.j_final):
                linha.append(-matriz_a.matriz[i][j])
            oposta.append(linha)

        return oposta

    def verificar_elemento_oposto(self, matriz_a):
        # Gera a matriz oposta de A (cada elemento com o sinal invertido)
        oposta = self.gerar_matriz_oposta(matriz_a)

        # "Empacota" a lista 'oposta' num objeto Matriz, para poder usar em somar()
        matriz_oposta_obj = type(matriz_a)(matriz_a.i_final, matriz_a.j_final)
        matriz_oposta_obj.matriz = oposta

        # Gera a matriz neutra que será usada como referência da comparação
        neutra = self.gerar_matriz_neutra(matriz_a.i_final, matriz_a.j_final)

        # Soma A + (-A); o resultado esperado é a matriz neutra
        a_mais_oposta = self.somar(matriz_a, matriz_oposta_obj)

        if a_mais_oposta is None:
            return

        iguais, contador = self.comparar(a_mais_oposta, neutra)

        print(f"A + (-A) == 0? {iguais}")
        print(f"Número de comparações realizadas: {contador}")

    def verificar_associativa(self, matriz_a, matriz_b, matriz_c):
        # === Lado direito da equação: A + (B + C) ===

        # Soma B + C primeiro
        b_mais_c = self.somar(matriz_b, matriz_c)
        if b_mais_c is None:
            return

        # Empacota o resultado de B+C num objeto Matriz
        matriz_bc_obj = type(matriz_a)(matriz_b.i_final, matriz_b.j_final)
        matriz_bc_obj.matriz = b_mais_c

        # Soma A + (B+C), completando o lado direito
        a_mais_bc = self.somar(matriz_a, matriz_bc_obj)

        # === Lado esquerdo da equação: (A + B) + C ===

        # Soma A + B
        a_mais_b = self.somar(matriz_a, matriz_b)

        # Interrompe se qualquer soma até aqui tiver falhado
        if a_mais_b is None or a_mais_bc is None:
            return

        # Empacota o resultado de A + B num objeto Matriz
        matriz_ab_obj = type(matriz_a)(matriz_a.i_final, matriz_a.j_final)
        matriz_ab_obj.matriz = a_mais_b

        # Soma (A + B) + C
        ab_mais_c = self.somar(matriz_ab_obj, matriz_c)

        if ab_mais_c is None:
            return

        iguais, contador = self.comparar(a_mais_bc, ab_mais_c)

        print(f"(A + B) + C == A + (B + C)? {iguais}")
        print(f"Número de comparações realizadas: {contador}")