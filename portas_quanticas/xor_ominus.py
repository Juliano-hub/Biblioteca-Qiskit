from qiskit import QuantumCircuit

def xor_ominus(circuit, qubits):
    # Aplicar a porta NOT no primeiro qubit
    circuit.x(qubits[0])
    circuit.barrier()

    # Aplicar a porta Toffoli com controle nos qubits[0] e qubits[1], e alvo no qubits[2]
    circuit.ccx(qubits[0], qubits[1], qubits[2])
    circuit.barrier()

    # Aplicar a porta NOT no primeiro qubit (qubits[0])
    circuit.x(qubits[0])
    circuit.barrier()

    # Aplicar a porta NOT no segundo qubit (qubits[1])
    circuit.x(qubits[1])
    circuit.barrier()

    # Aplicar a porta Toffoli com controle nos qubits[0] e qubits[1], e alvo no qubits[3]
    circuit.ccx(qubits[0], qubits[1], qubits[3])
    circuit.barrier()

    circuit.x(qubits[1])
    circuit.barrier()

    # Aplicar a porta NOT nos qubits[2]
    circuit.x(qubits[2])

    # Aplicar a porta NOT nos qubits[3]
    circuit.x(qubits[3])
    circuit.barrier()

    # Aplicar a porta Toffoli com controle nos qubits[2] e qubits[3], e alvo no qubits[4]
    circuit.ccx(qubits[2], qubits[3], qubits[4])
    circuit.barrier()

    # Aplicar a porta NOT nos qubits[2], qubits[3] e qubits[4]
    circuit.x(qubits[2])
    circuit.x(qubits[3])
    circuit.x(qubits[4])