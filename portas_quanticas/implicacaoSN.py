from qiskit import QuantumCircuit

def implication(qc, control_qubit, target_qubit, aux_qubit):
    """Aplica o operador de implicação diretamente no circuito quântico especificado."""
    # Aplicar NOT no qubit de controle para preparar para a implicação
    qc.x(control_qubit)
    
    # Aplicar Toffoli usando o qubit de controle (já negado), target e auxiliar
    qc.ccx(control_qubit, target_qubit, aux_qubit)
    
    # Aplicar NOT no qubit auxiliar para finalizar a implicação
    qc.x(aux_qubit)
