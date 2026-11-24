from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
qc = QuantumCircuit(1)
qc.h(0)
# qc.h(0)  # добавьте второй H
state = Statevector.from_instruction(qc)
print(qc.draw())
print('Амплитуды:',state.data)
print('Вероятности:',state.probabilities_dict())
