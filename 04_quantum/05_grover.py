from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
# Поиск состояния 11 среди четырёх вариантов.
qc = QuantumCircuit(2)
qc.h([0,1])
qc.cz(0,1)  # оракул: меняет фазу |11>
qc.h([0,1]); qc.x([0,1]); qc.cz(0,1)
qc.x([0,1]); qc.h([0,1])  # диффузор с точностью до глобальной фазы
print(qc.draw())
print(Statevector.from_instruction(qc).probabilities_dict())
