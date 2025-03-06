from qiskit import QuantumCircuit

def add_grouping_function(qc, qubits):
    """ Aplica uma função de Grouping em um conjunto de qubits. """
    # Assume que a agregação é feita por meio de uma sequência de CNOTs
    target = qubits[-1]  # Define o último qubit como alvo para simplificar
    for qubit in qubits[:-1]:  # Aplica CNOT entre cada qubit e o qubit alvo
        qc.cx(qubit, target)
    # Uma porta Hadamard no qubit alvo para finalizar a agregação
    qc.h(target)

