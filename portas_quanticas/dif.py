# fuzzy_diff_operator.py
from qiskit import QuantumCircuit

def apply_diff_operator(qc, qubit1, qubit2, aux_qubit):
    """ Aplica o operador de diferença fuzzy conforme especificado. """
    qc.x(qubit2)  # Aplica NOT no qubit2
    qc.ccx(qubit1, qubit2, aux_qubit)  # Aplica Toffoli (CCX)
    qc.x(qubit2)  # Reverte NOT no qubit2

def diff_fuzzy(qc, qubit1, qubit2, aux_qubit):
    """ Configura e aplica o operador de diferença fuzzy. """
    apply_diff_operator(qc, qubit1, qubit2, aux_qubit)
