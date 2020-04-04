import os
import random
from Perceptron import Perceptron
from Setting import entrada_alfabeto, saida_alfabeto, saida_a_t


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

            print("\nDigite a quantidade de epocas para treinamento: ")
            epocas = int(input())

            entradas_perceptron = entrada_alfabeto[entrada]
            saida_perceptron = saida_a_t[entrada]
            perceptron = Perceptron(inputs=entradas_perceptron, saidas=saida_perceptron, qtde_neuronios=1)
            perceptron.treinar(epochs=epocas)
            for i in range(len(entradas_perceptron)):
                print("\nA saída correta da letra {} é : {}".format(entrada, saida_a_t[entrada]))
                print("A saída obtida do perceptron é: {}".format(perceptron.calcula_saida(entradas_perceptron[i])))
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
                print("\nA saída correta da letra {} é : {}".format(entrada, saida_alfabeto[entrada]))
                print("A saída obtida do perceptron é: {}".format(perceptron.calcula_saida(entradas_perceptron[i])))
            input()
