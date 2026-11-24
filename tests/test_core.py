import unittest, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(path):
    spec=importlib.util.spec_from_file_location(Path(path).stem,ROOT/path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
class CoreTests(unittest.TestCase):
    def test_route(self):
        m=load('06_web/engine.py')
        self.assertEqual(m.route()[2],7)
        self.assertEqual(m.route(True)[2],9)
    def test_dijkstra(self):
        m=load('02_graphs/03_dijkstra.py'); self.assertEqual(m.dijkstra(m.G,'A','D'),(7,['A','B','D']))
    def test_knapsack(self):
        self.assertEqual(load('03_optimization/02_knapsack.py').solve(7)[0],19)
    def test_maxcut(self):
        from itertools import product
        m=load('03_optimization/03_maxcut.py'); self.assertEqual(max(map(m.score,product([0,1],repeat=4))),4)
    def test_qubo(self):
        from itertools import product
        m=load('03_optimization/04_qubo.py'); self.assertEqual(min(product([0,1],repeat=3),key=m.objective),(0,1,0))
    @unittest.skipUnless(importlib.util.find_spec('qiskit'),'Qiskit не установлен')
    def test_quantum(self):
        from qiskit import QuantumCircuit
        from qiskit.quantum_info import Statevector
        qc=QuantumCircuit(2); qc.h(0); qc.cx(0,1)
        self.assertAlmostEqual(Statevector.from_instruction(qc).probabilities_dict()['11'],.5)
        m=load('04_quantum/07_qaoa_grid.py'); self.assertAlmostEqual(m.evaluate(0,0)[0],1.5)
if __name__=='__main__': unittest.main()
