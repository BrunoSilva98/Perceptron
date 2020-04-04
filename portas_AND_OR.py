from Perceptron import Perceptron


# noinspection PyShadowingNames
def teste_portas_logicas(porta):
    entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saidas = None
    print("Porta {}".format(porta.upper()))
    if porta.upper() == "AND":
        saidas = [0, 0, 0, 1]
    elif porta.upper() == "OR":
        saidas = [0, 1, 1, 1]

    perceptron = Perceptron(entradas, saidas, 1)
    perceptron.treinar(epochs=100, verbose=False)
    for i in range(len(entradas)):
        print(perceptron.calcula_saida(entradas[i]))


if __name__ == '__main__':
    teste_portas_logicas("AND")
    print("\n")
    teste_portas_logicas("OR")
