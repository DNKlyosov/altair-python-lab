import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
# MaxCut на треугольнике; один слой QAOA, идеальный симулятор.
edges = [(0,1),(1,2),(0,2)]
def score(bitstring):
    bits = bitstring[::-1]
    return sum(bits[a]!=bits[b] for a,b in edges)
def evaluate(gamma,beta):
    qc = QuantumCircuit(3); qc.h(range(3))
    for a,b in edges:
        qc.rzz(-gamma,a,b)
    for i in range(3):
        qc.rx(2*beta,i)
    probs = Statevector.from_instruction(qc).probabilities_dict()
    return sum(score(s)*p for s,p in probs.items()),probs
if __name__ == '__main__':
    best = max((evaluate(g,b)[0],g,b) for g in np.linspace(0,np.pi,21) for b in np.linspace(0,np.pi/2,21))
    print('Средний разрез, gamma, beta:',best)
    print('Распределение:',evaluate(best[1],best[2])[1])
    print('Классический максимум: 2')
