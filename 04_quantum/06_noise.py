from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
qc = QuantumCircuit(2,2)
qc.h(0); qc.cx(0,1); qc.measure([0,1],[0,1])
for p in [0,0.05,0.2]:
    noise = NoiseModel()
    if p:
        noise.add_all_qubit_quantum_error(depolarizing_error(p,2),['cx'])
    sim = AerSimulator(noise_model=noise)
    counts = sim.run(transpile(qc,sim,optimization_level=0),shots=2000,seed_simulator=42).result().get_counts()
    print('Параметр деполяризации:',p,'частоты:',counts)
