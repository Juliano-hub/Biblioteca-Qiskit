from qiskit import QuantumCircuit

def add_overlap_function(qc, qubit1, qubit2):
    qc.h(qubit1)
    qc.h(qubit2)
    qc.cx(qubit1, qubit2)
    qc.h(qubit1)
    qc.h(qubit2)
