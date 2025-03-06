from qiskit import QuantumCircuit

def add_xor_fuzzy(qc):
    print("Adicionando XOR Fuzzy:")
    qubit1 = int(input("Índice do primeiro qubit (começando de 0): "))
    qubit2 = int(input("Índice do segundo qubit (começando de 0): "))
    
    qc.cx(qubit1, qubit2)
    qc.cx(qubit2, qubit1)
    qc.cx(qubit1, qubit2)
