# exemplo: 10,5,15,3,1,20,25,18


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class Arvore:
    def __init__(self):
        self.raiz = None

    def obter_altura(self, no):
        if no is None:
            return 0
        else:
            return no.altura

    def atualizar_altura(self, no):
        altura_esquerda = self.obter_altura(no.esquerda)
        altura_direita = self.obter_altura(no.direita)
        no.altura = 1 + max(altura_esquerda, altura_direita)

    def obter_fator_balanceamento(self, no):
        if no is None:
            return 0

        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    def inserir(self, valor, altura=1):
        caminho = []

        if self.raiz is None:
            self.raiz = No(valor)
            return

        no_atual = self.raiz
        caminho.append(no_atual)

        while True:
            if valor < no_atual.valor:
                if no_atual.esquerda is None:
                    no_atual.esquerda = No(valor)
                    break
                else:
                    no_atual = no_atual.esquerda

            elif valor > no_atual.valor:
                if no_atual.direita is None:
                    no_atual.direita = No(valor)
                    break
                else:
                    no_atual = no_atual.direita
            else:
                break

        for i in range(len(caminho) - 1, -1, -1):
            no_ancestral = caminho[i]
            self.atualizar_altura(no_ancestral)
            fator_balanceamento = self.obter_fator_balanceamento(no_ancestral)

            novo_no = no_ancestral

            if fator_balanceamento > 1:
                if valor < no_ancestral.esquerda.valor:
                    novo_no = self.rotacao_direita(no_ancestral)
                elif valor > no_ancestral.esquerda.valor:
                    no_ancestral.esquerda = self.rotacao_esquerda(no_ancestral.esquerda)
                    novo_no = self.rotacao_direita(no_ancestral)

            elif fator_balanceamento < -1:
                if valor > no_ancestral.direita.valor:
                    novo_no = self.rotacao_esquerda(no_ancestral)
                elif valor < no_ancestral.direita.valor:
                    no_ancestral.direita = self.rotacao_direita(no_ancestral.direita)
                    novo_no = self.rotacao_esquerda(no_ancestral)

            if novo_no != no_ancestral:
                if i > 0:
                    pai = caminho[i - 1]
                    if pai.esquerda == no_ancestral:
                        pai.esquerda = novo_no
                    else:
                        pai.direita = novo_no
                else:
                    self.raiz = novo_no

    def buscar(self, valor):
        no_atual = self.raiz

        if no_atual is None:
            return False

        while no_atual is not None:
            if valor == no_atual.valor:
                return True
            elif valor < no_atual.valor:
                no_atual = no_atual.esquerda
            else:
                no_atual = no_atual.direita

        return False

    def rotacao_direita(self, no_desbalanceado_z):
        y = no_desbalanceado_z.esquerda
        t3 = y.direita

        y.direita = no_desbalanceado_z
        no_desbalanceado_z.esquerda = t3

        self.atualizar_altura(no_desbalanceado_z)
        self.atualizar_altura(y)

        return y

    def rotacao_esquerda(self, no_desbalanceado_z):
        y = no_desbalanceado_z.direita
        t2 = y.esquerda

        y.esquerda = no_desbalanceado_z
        no_desbalanceado_z.direita = t2

        self.atualizar_altura(no_desbalanceado_z)
        self.atualizar_altura(y)

        return y
    
    def imprimir_arvore(self, no=None, nivel=0, prefixo="Raiz: "):
        if no is None:
            no = self.raiz
        print(" " * (nivel * 4) + prefixo + str(no.valor))
        if no.esquerda is not None:
            self.imprimir_arvore(no.esquerda, nivel + 1, "Esq- ")
        if no.direita is not None:
            self.imprimir_arvore(no.direita, nivel + 1, "Dir- ")


if __name__ == "__main__":
    valores = [10, 5, 15, 3, 1, 20, 25, 18]

    arvore = Arvore()

    for valor in valores:
        arvore.inserir(valor)

    for no in valores:
        print(no, arvore.buscar(no))

    print("\nEstrutura da árvore:")
    arvore.imprimir_arvore()

    