from Perceptron import Perceptron


if __name__ == '__main__':
    entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saidas = [0, 1, 1, 1]
    perceptron = Perceptron(entradas, saidas, 1)
    perceptron.treinar()
    for i in range(len(entradas)):
        print(perceptron.calcula_saida(entradas[i]))
