class Calculadora:

    def _validar_numeros(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Os valores devem ser números (int ou float)")

    def soma(self, a, b):
        self._validar_numeros(a, b)
        return a + b

    def subtracao(self, a, b):
        self._validar_numeros(a, b)
        return a - b

    def multiplicacao(self, a, b):
        self._validar_numeros(a, b)
        return a * b

    def divisao(self, a, b):

        self._validar_numeros(a, b)
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero")
        return a / b
    
# melhoria: validação de tipos

        if b == 0:  # pequena mudança adicionada
            return "Erro: divisão por zero"
        return a / b

    # novo método simples
    def potencia(self, a, b):
        return a ** b
 main
