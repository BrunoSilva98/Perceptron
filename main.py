import os
import random
from Perceptron import Perceptron
from Setting import entrada_alfabeto, saida_alfabeto, saida_a_t


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
    print(entradas)

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
    key = 0

    while key != '3':
        print("1. Reconhecimento letras A e T")
        print("2. Reconhecimento Alfabeto")
        print("3. Sair")

        key = input()
        os.system('clear')

        if key == '1':
            print("Escolha entre a letra 'A' ou 'T':")
            entrada = input().upper()
            print("A matriz correspondente é: {}".format(entrada_alfabeto[entrada]))
            entradas_perceptron = entrada_alfabeto[entrada]
            saida_perceptron = saida_a_t[entrada]
            perceptron = Perceptron(inputs=entradas_perceptron, saidas=saida_perceptron, qtde_neuronios=1)
            perceptron.treinar()
            for i in range(len(entradas_perceptron)):
                print("\nA saída da letra {} é: {}".format(entrada, perceptron.calcula_saida(entradas_perceptron[i])))
            input()

        elif key == '2':
            print("Escolha a letra do alfabeto:")
            entrada = input().upper()
            print("A matriz correspondente é: {}".format(entrada_alfabeto[entrada]))
            print("\nDigite a quantidade de epocas para treinamento: ")
            epocas = input()

            entradas_perceptron = entrada_alfabeto[entrada]
            saidas_perceptron = saida_alfabeto[entrada]
            perceptron = Perceptron(inputs=entradas_perceptron, saidas=saidas_perceptron, qtde_neuronios=5)
            perceptron.treinar(epochs=int(epocas))

            for i in range(len(entradas_perceptron)):
                print("A saída da letra {} é: {}".format(entrada, perceptron.calcula_saida(entradas_perceptron[i])))
        input()
