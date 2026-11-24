import streamlit as st
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
st.title('Кубит и квантовые операции')
text=st.text_input('Гейты через пробел (X H Z Y S T)','H')
gates=text.upper().split()
if any(g not in ['X','H','Z','Y','S','T'] for g in gates):
    st.error('Допустимы только X H Z Y S T'); st.stop()
if len(gates)>100:
    st.error('Не более 100 операций'); st.stop()
qc=QuantumCircuit(1)
for gate in gates:
    getattr(qc,gate.lower())(0)
state=Statevector.from_instruction(qc)
st.code(str(qc.draw()))
st.write({str(i):str(a) for i,a in enumerate(state.data)})
st.bar_chart({'Вероятность':state.probabilities().tolist()})
st.caption('Столбцы 0 и 1 соответствуют результатам измерения.')
fig=plot_bloch_multivector(state); st.pyplot(fig); plt.close(fig)
