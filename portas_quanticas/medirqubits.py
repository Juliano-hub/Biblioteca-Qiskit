from qiskit import ClassicalRegister, transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit_aer import Aer

def medir_qubits(circuit):
    """
    Função para medir qubits específicos e exibir um histograma dos resultados.
    
    :param circuit: O circuito quântico no qual será feita a medição.
    """
    selected_qubits = list(map(int, input("Digite os índices dos qubits que deseja medir, separados por espaço: ").split()))

    if not selected_qubits:
        print("Nenhum qubit selecionado. Nenhuma medição foi realizada.")
        return

    # Criar um registrador clássico APENAS se necessário
    if not circuit.cregs:
        creg = ClassicalRegister(len(selected_qubits), 'c')
        circuit.add_register(creg)
    else:
        creg = circuit.cregs[0]  # Usa o registrador clássico existente

    # Garante que há bits clássicos suficientes no registrador
    if len(creg) < len(selected_qubits):
        print(f"Registrador clássico atual tem {len(creg)} bits, mas {len(selected_qubits)} são necessários.")
        return

    # Adicionar medições associando cada qubit ao bit clássico correspondente
    for i, qubit in enumerate(selected_qubits):
        circuit.measure(qubit, creg[i])

    print("Medições adicionadas para os seguintes qubits:", selected_qubits)
    print(circuit.draw('text'))

    # Configurar o simulador
    simulator = Aer.get_backend('aer_simulator')

    # Transpilar o circuito antes de rodar
    transpiled_circuit = transpile(circuit, simulator)

    # Rodar o circuito no simulador
    result = simulator.run(transpiled_circuit, shots=1000).result()

    # Obter os resultados da medição
    counts = result.get_counts()
    print("Resultados da medição:", counts)

    # Exibir histograma das medições
    plot_histogram(counts)
    plt.show()
