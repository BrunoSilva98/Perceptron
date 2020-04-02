# Existem duas formas de utilizar
# 1 - Somente um Neuronio
# 2 - Mais de um Neuronio
# Em cada um dos modos, o shape do input e output para TREINAMENTO devem ser diferentes
# Shape do input com somente um neuronio: Entrada = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0]], ou seja, sublistas
# Deve ser utilizado uma sublista mesmo que haja somente uma entrada, EX -> [[1, 0, 1, 0]]
# O Output deve ser fornecido da seguinte maneira quando há somente um neuronio:
# Output = [0, 1], ou seja, um array simples.
# A Proporção de Input/Output deve ser de 1/1, ou seja, um valor no array de saída para cada subArray no input

# A Segunda Forma para treinamento são com multiplos neuronios
# Nesse caso, o input permanece da mesma maneira, sublistas dentro de listas, mesmo que com somente um elemento
# O Output deve vir dentro de uma sublista, ou seja, se o input for [[1,2,3]] e houverem 3 neurônios
# O output deve vir da seguinte maneira: [[0, 1, 2]]
# Cada um dos valores da sublista de output indica a saida de um neuronio
# Caso existam mais neurônios que saídas, os neurônios excedentes serão ignorados
# Caso existam mais saídas que neurônios, ocorrerá erro.
# É possível realizar treinamento de multiplas classes ao mesmo tempo, ou seja:
# Entrada = [[0, 1, 0, 1], [1, 0, 1, 0]], duas classes de entrada
# Saida = [[0,1], [1, 0]]

# Finalizado o treinamento seguindo o padrão acima, para realizar alguma previsão basta chamar a função calcula_saida
# Recebe como parâmetro somente o input de um array simples, ou seja, [0, 1, 0, 1]
# Retornará o output no mesmo formato de array

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
