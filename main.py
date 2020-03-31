import MCP_Neuron


def test_neuron():
    neuron = MCP_Neuron.MCP()
    entradas = [0, 1, 2]
    neuron.set_entradas(entradas)
    print(neuron.evaluate())


if __name__ == '__main__':
    test_neuron()
