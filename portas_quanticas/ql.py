from qiskit import QuantumCircuit, QuantumRegister

def ql_implication(qc, qubits):
    """
    Aplica o circuito com Toffoli e NOT nos 5 qubits escolhidos pelo usuário.
    
    Parâmetros:
    qc (QuantumCircuit): Circuito quântico no qual as operações serão aplicadas.
    qubits (list): Lista com 5 índices dos qubits escolhidos pelo usuário.
    """

    # Aplicar a porta Toffoli com controle nos qubits 1 e 2 e alvo no qubit 3
    qc.ccx(qubits[1], qubits[2], qubits[3])

    # Aplicar a porta NOT no qubit 3
    qc.x(qubits[3])

    # Aplicar a porta Toffoli com controle nos qubits 0 e 3 e alvo no qubit 4
    qc.ccx(qubits[0], qubits[3], qubits[4])

    # Aplicar a porta NOT no qubit 4
    qc.x(qubits[4])
