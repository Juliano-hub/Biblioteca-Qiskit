# fuzzy_diff_operator.py
from qiskit import QuantumCircuit

def diff_fuzzy(qc, qubit1, qubit2, aux_qubit):
    """Aplica o operador de diferença fuzzy no circuito."""
    qc.x(qubit2)  # Aplica NOT no segundo qubit
    qc.ccx(qubit1, qubit2, aux_qubit)  # Aplica porta Toffoli
    qc.x(qubit2)  # Reverte a operação NOT no segundo qubit
