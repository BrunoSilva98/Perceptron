# Input deve ser uma lista com os valores, ex [1, 2, 3]

import random


class MCP:
    def __init__(self):
        self.entradas = list()
        self._pesos = list()

    # noinspection PyMethodMayBeStatic
    def __activation_function(self, value):
        res = 1 if value > 1 else 0
        return res

    def get_pesos(self):
        return self._pesos

    def set_entradas(self, inputs):
        self.entradas = inputs
        self.__set_pesos()

    def __set_pesos(self):
        weight_value = random.random()
        for idx in range(len(self.entradas)):
            self._pesos.append(weight_value)

    def somatorio(self):
        somatoria = 0
        for idx in range(len(self.entradas)):
            somatoria = somatoria + (self.entradas[idx] * self._pesos[idx])
        return somatoria

    def evaluate(self):
        soma = self.somatorio()
        return self.__activation_function(soma)
