from qiskit import QuantumCircuit
for n in [2,4,8]:
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(n-1):
        qc.cx(i,i+1)
    print('Кубиты:',n,'операции:',qc.count_ops(),'глубина:',qc.depth())
    print(qc.draw())
