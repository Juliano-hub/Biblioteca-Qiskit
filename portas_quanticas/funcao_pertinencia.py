import numpy as np
from qiskit import QuantumCircuit

def inicializa_circuito_com_probabilidades(num_qubits, probabilidades):
    if len(probabilidades) != num_qubits:
        print("Número de probabilidades não corresponde ao número de qubits. Reinicie o programa.")
        return None
    
    my_circuit = QuantumCircuit(num_qubits)
    matriz(my_circuit, probabilidades)  
    return my_circuit


def matriz(qc, f_A_values):
    num_qubits = qc.num_qubits
    if len(f_A_values) != num_qubits:
        raise ValueError("O número de valores f_A deve ser igual ao número de qubits no circuito.")

    for qubit_index, f_A_value in enumerate(f_A_values):
        theta = 2 * np.arctan(np.sqrt(f_A_value) / np.sqrt(1 - f_A_value))

        qc.u(theta, 0, 0, qubit_index)
