# Input deve ser uma lista com os valores, ex [1, 2, 3]

from MCP_Neuron import MCP
import random


class Neuron(MCP):
    def __init__(self, input_length):
        super().__init__()
        self._pesos = self.__set_weights(input_length + 1)

    def set_entradas(self, inputs):
        self.entradas.clear()
        self.entradas.append(1)  # Valor fixo do bias
        for idx in range(len(inputs)):
            self.entradas.append(inputs[idx])

    # noinspection PyMethodMayBeStatic
    def __set_weights(self, qtde):
        weight_value = random.random()
        pesos = list()
        for idx in range(qtde):
            pesos.append(weight_value)
        return pesos

    def update_weights(self, erro, taxa_aprendizagem):
        for idx in range(len(self._pesos)):
            self._pesos[idx] = self._pesos[idx] + (taxa_aprendizagem * self.entradas[idx] * erro)
