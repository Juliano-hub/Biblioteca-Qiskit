from qiskit import QuantumCircuit

def implication(qc, control_qubit, input_qubit, target_qubit):

    # Aplicar NOT no qubit de controle para preparar a operação
    qc.x(control_qubit)
    
    # Aplicar a porta Toffoli (CCX) usando o qubit de controle (já negado), input e target
    qc.ccx(control_qubit, input_qubit, target_qubit)
    
    # Aplicar NOT no qubit alvo para finalizar a implicação fuzzy
    qc.x(target_qubit)
