from qiskit import QuantumCircuit

def xor_fuzzy_cross(qc, control_qubits, target_qubits, aux_qubits):
    # Aplica NOT nas entradas antes do AND
    qc.x(control_qubits[0])
    qc.x(control_qubits[1])

    # Primeiro AND após os NOTs nos qubits de controle
    qc.ccx(control_qubits[0], target_qubits[0], aux_qubits[0])
    qc.x(control_qubits[0])  # Reset do qubit de controle ao estado original

    # Segundo AND normal
    qc.ccx(control_qubits[1], target_qubits[1], aux_qubits[1])
    qc.x(control_qubits[1])  # Reset do qubit de controle ao estado original

    # OR das saídas dos ANDs, usando um qubit auxiliar adicional
    qc.cx(aux_qubits[0], aux_qubits[2])
    qc.cx(aux_qubits[1], aux_qubits[2])

    # Final NOT para completar a operação XOR
    qc.x(aux_qubits[2])

    # Limpeza: Reset dos qubits auxiliares usados para AND
    qc.x(aux_qubits[0])
    qc.x(aux_qubits[1])
