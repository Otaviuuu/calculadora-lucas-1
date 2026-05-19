class Calculadora:

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:  # pequena mudança adicionada
            return "Erro: divisão por zero"
        return a / b

    # novo método simples
    def potencia(self, a, b):
        return a ** b