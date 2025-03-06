from qiskit import QuantumCircuit

def add_implicacao(qc):
    print("Adicionando Implicação Fuzzy:")
    control = int(input("Índice do qubit de controle (antecedente, começando de 0): "))
    target = int(input("Índice do qubit alvo (consequente, começando de 0): "))
    
    qc.x(control)  # NOT no antecedente para aplicar ¬A
    qc.cx(control, target)  # CNOT para realizar a operação condicional B se ¬A
    qc.x(control)  # Devolver o qubit de controle ao seu estado original se necessário

