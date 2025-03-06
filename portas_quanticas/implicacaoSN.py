from qiskit import QuantumCircuit

def apply_implication_operator(qc, control_qubit, target_qubit, aux_qubit):
    """Aplica o operador de implicação conforme especificado."""
    # Aplicar NOT no qubit de controle para preparar para a implicação
    qc.x(control_qubit)
    
    # Aplicar Toffoli usando o qubit de controle (já negado), target e auxiliar
    qc.ccx(control_qubit, target_qubit, aux_qubit)
    
    # Reverter o NOT no qubit de controle após a operação
    qc.x(control_qubit)
    
    # Aplicar NOT no qubit auxiliar para finalizar a implicação
    qc.x(aux_qubit)

def implication(qc, control_qubit, target_qubit, aux_qubit):
    """Configura e aplica o operador de implicação."""
    apply_implication_operator(qc, control_qubit, target_qubit, aux_qubit)
