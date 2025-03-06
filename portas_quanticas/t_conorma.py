def apply_or_fuzzy_generic(circuit, control_indices, target_index):
    # Aplica a porta NOT apenas uma vez nos qubits de controle
    for control_index in control_indices:
        circuit.x(control_index)
    
    # Aplica a porta CCX (Toffoli) nas duas qubits de controle e no qubit alvo
    circuit.ccx(control_indices[0], control_indices[1], target_index)
    
    # Aplica a porta NOT no qubit alvo
    circuit.x(target_index)
