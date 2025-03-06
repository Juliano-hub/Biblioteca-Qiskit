from qiskit import QuantumCircuit

def toffoli_circuit_interactive(qc):
    print("Configurando a porta Toffoli:")
    control1 = int(input("Índice do primeiro qubit de controle (começando de 0): "))
    control2 = int(input("Índice do segundo qubit de controle (começando de 0): "))
    target = int(input("Índice do qubit alvo (começando de 0): "))

    qc.ccx(control1, control2, target)