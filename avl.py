# exemplo: 10,5,15,3,1,20,25,18

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class Arvore:
    def __init__(self):
        self.raiz = None
        self.altura = 1

    def obter_altura(self, no):
        if no is None:
            return 0
        else:
            return no.altura
        
    def atualizar_altura(self, no):
        altura_esquerda = self.obter_altura(no.esquerda)
        altura_direita = self.obter_altura(no.direita)
        no.altura =  1 + max(altura_esquerda, altura_direita)

    def obter_fator_balanceamento(self, no):
        if no is None:
            return 0
        
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)
    

    def inserir(self, valor, altura = 1):
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


if __name__ == "__main__":
    print("Teste principal")
