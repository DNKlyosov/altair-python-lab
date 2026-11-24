import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
from engine import route
st.title('Маршрутизация')
blocked=st.checkbox('Перекрыть участок B–D')
graph,path,cost=route(blocked)
st.metric('Стоимость',cost)
st.write(' → '.join(path))
fig,ax=plt.subplots()
pos={'A':(0,0),'B':(1,1),'C':(1,-1),'D':(2,0)}
nx.draw(graph,pos,with_labels=True,ax=ax)
nx.draw_networkx_edge_labels(graph,pos,edge_labels=nx.get_edge_attributes(graph,'weight'),ax=ax)
nx.draw_networkx_edges(graph,pos,edgelist=list(zip(path,path[1:])),edge_color='green',width=3,ax=ax)
st.pyplot(fig); plt.close(fig)
