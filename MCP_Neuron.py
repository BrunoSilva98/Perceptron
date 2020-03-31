import random


class MCP:
    def __init__(self):
        self.entradas = list()
        self.pesos = list()
        self.saida = None

    # noinspection PyMethodMayBeStatic
    def __activation_function(self, value):
        res = 1 if value > 1 else 0
        return res

    def set_entradas(self, inputs):
        for idx in range(len(inputs)):
            self.entradas.append(inputs[idx])
            self.pesos.append(random.random())

    def somatorio(self):
        somatoria = 0
        for idx in range(len(self.entradas)):
            somatoria = somatoria + (self.entradas[idx] * self.pesos[idx])
        return somatoria

    def evaluate(self):
        soma = self.somatorio()
        return self.__activation_function(soma)
