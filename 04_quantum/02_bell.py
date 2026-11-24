from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
state = Statevector.from_instruction(qc)
print(qc.draw())
print('Точные вероятности:',state.probabilities_dict())
state.seed(42)
print('Выборка измерений:',state.sample_counts(1000))
# Qiskit записывает биты справа налево: q1 q0.
