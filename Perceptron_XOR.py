from Perceptron import Perceptron


class Perceptron_XOR():

    def __init__(self):
        self._perceptron_input = Perceptron([[0, 0], [0, 1], [1, 0], [1, 1]], [[0, 1], [1, 1], [1, 1], [1, 0]], 2)
        self._perceptron_hidden = Perceptron([[0, 1], [1, 0], [1, 1]], [0, 0, 1], 1)

    def treinar(self, verbose=False):
        self._perceptron_input.treinar(verbose=verbose)
        self._perceptron_hidden.treinar(verbose=verbose)

    def calcula_tabela_verdade(self, entradas):
        saidas = list()
        for entrada in entradas:
            entrada_hidden = self._perceptron_input.calcula_saida(entrada)
            saidas.append(self._perceptron_hidden.calcula_saida(entrada_hidden))
        return saidas


if __name__ == '__main__':
    entradas_tabela_verdade = [[0, 0], [0, 1], [1, 0], [1, 1]]
    xor = Perceptron_XOR()
    xor.treinar()
    tabela_verdade = xor.calcula_tabela_verdade(entradas_tabela_verdade)
    print(tabela_verdade)
