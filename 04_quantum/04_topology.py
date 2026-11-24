from qiskit import QuantumCircuit, transpile
from qiskit.transpiler import CouplingMap
qc = QuantumCircuit(5,5)
qc.h(0); qc.cx(0,4); qc.measure(range(5),range(5))
for name,topology in [('Линия',CouplingMap.from_line(5)),('Кольцо',CouplingMap.from_ring(5)),('Полная',CouplingMap.from_full(5))]:
    out = transpile(qc,coupling_map=topology,initial_layout=list(range(5)),basis_gates=['h','cx','swap'],optimization_level=0,seed_transpiler=42)
    print(name, 'глубина:',out.depth(),'операции:',out.count_ops())
    print(out.draw())
# SWAP оставлен в учебном базисе для наглядности; физические базисы могут отличаться.
