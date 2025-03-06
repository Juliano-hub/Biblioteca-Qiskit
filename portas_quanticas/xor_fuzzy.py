from qiskit import QuantumCircuit

def xor_ominus(qc, control_qubits, target_qubits, aux_qubits):
    # Verifica se os parâmetros são suficientes para a operação
    if len(control_qubits) < 2:
        raise ValueError("Insira pelo menos dois qubits de controle.")
    if len(target_qubits) < 2:
        raise ValueError("Insira pelo menos dois qubits alvo.")
    if len(aux_qubits) < 3:
        raise ValueError("Insira pelo menos três qubits auxiliares.")

    # Aplicar NOT nos qubits de controle conforme a lógica do XOR ôminus
    for qubit in control_qubits:
        qc.x(qubit)

    # Realizar operações AND entre os qubits de controle e alvo, armazenando os resultados nos qubits auxiliares
    for i in range(min(len(control_qubits), len(target_qubits))):
        qc.ccx(control_qubits[i], target_qubits[i], aux_qubits[i])

    # Realizar a operação OR com os resultados do AND, usando um qubit auxiliar extra
    for i in range(len(aux_qubits)-1):  # Exclui o último qubit auxiliar que armazenará o resultado final
        qc.cx(aux_qubits[i], aux_qubits[-1])

    # Aplicar NOT final no último qubit auxiliar para completar a operação XOR
    qc.x(aux_qubits[-1])

    # Reset dos qubits de controle para seus estados originais se necessário
    for qubit in control_qubits:
        qc.x(qubit)