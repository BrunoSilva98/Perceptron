# Inputs devem ser no formato de lista aninhada, ex [[1, 2], [3,4]]

from Perceptron_Neuron import Neuron


class Perceptron:
    def __init__(self, inputs, saidas, qtde_neuronios, taxa_aprendizagem=0.01):
        self._saidas = saidas
        self._inputs = inputs
        self._taxa_aprendizagem = taxa_aprendizagem
        self.final_weights = list()
        self._neuronios = self.__cria_neuronios(qtde_neuronios, len(inputs[0]))

    # noinspection PyMethodMayBeStatic
    def __cria_neuronios(self, qtde, input_length):
        neuronios = list()
        for i in range(qtde):
            neuronios.append(Neuron(input_length))
        return neuronios

    # noinspection PyMethodMayBeStatic
    def calcula_erro(self, saida_obtida, saida_correta):
        return saida_correta - saida_obtida

    def save_weights(self):
        for neuronio in self._neuronios:
            self.final_weights.append(neuronio.get_pesos())

    def calcula_saida(self, entrada):
        saidas_neuronios = list()
        for neuronio in self._neuronios:
            neuronio.set_entradas(entrada)
            saidas_neuronios.append(neuronio.evaluate())
        return saidas_neuronios

    def treinar(self, epochs=100):
        for _ in range(epochs):
            print("---Treinando---Epoch " + str(_+ 1) + "/" + str(epochs))
            if len(self._neuronios) == 1:
                for entradas, saidas in zip(self._inputs, self._saidas):
                    neuronio = self._neuronios[0]
                    neuronio.set_entradas(entradas)
                    saida_calculada = neuronio.evaluate()
                    erro = self.calcula_erro(saida_calculada, saidas)
                    neuronio.update_weights(erro, self._taxa_aprendizagem)
            else:
                for entradas, saidas in zip(self._inputs, self._saidas):
                    for idx in range(len(saidas)):
                        saida = saidas[idx]
                        neuronio = self._neuronios[idx]
                        neuronio.set_entradas(entradas)
                        saida_calculada = neuronio.evaluate()
                        erro = self.calcula_erro(saida_calculada, saida)
                        neuronio.update_weights(erro, self._taxa_aprendizagem)

        self.save_weights()
