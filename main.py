from Perceptron import Perceptron
import random


def teste_portas_logicas():
    entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saidas = [0, 0, 0, 1]
    perceptron = Perceptron(entradas, saidas, 1)
    perceptron.treinar(epochs=100)
    for i in range(len(entradas)):
        print(perceptron.calcula_saida(entradas[i]))


def teste_letra():
    entradas = list()
    saidas = list()
    for i in range(2):
        entradas.append(gera_vetor_aleatorio(26))
        saidas.append(gera_vetor_aleatorio(5))
    perceptron = Perceptron(entradas, saidas, 5)
    perceptron.treinar(epochs=300)
    print("Saida 0 = ", end="")
    print(saidas[0])
    print("Saida 1 = ", end="")
    print(saidas[1])
    for i in range(len(entradas)):
        print(perceptron.calcula_saida(entradas[i]))


def gera_vetor_aleatorio(tamanho):
    vet = list()
    for i in range(tamanho):
        vet.append(random.randint(0, 1))
    return vet


if __name__ == '__main__':
    teste_portas_logicas()
    teste_letra()
