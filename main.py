import streamlit as st
import numpy as np
import plotly.graph_objects as go
from PIL import Image
import matplotlib.pyplot as plt
import sympy as sp #pode apagar este comentaria

st.header('Média e Desvio Padrão')

sss = Image.open('imgs/logo_cabecalho.png')
st.sidebar.image(sss)





col1, col2, col3 = st.columns(3)
with col1:
    mu = st.slider('Média', 0, 40, 20)

with col2:
    dj = st.slider("Djonny", 0., 65., 1.)
    st.write(dj)

with col3:
    x, w, f = sp.symbols('x, \omega, f')
    f = sp.Function("f")
    equacao = sp.Eq(f(x), sp.diff(f(x),x))
    solucao = sp.dsolve(equacao, ics={f(0): 2})
    sollll = sp.latex(solucao)
    st.latex(sollll)




xxx = np.linspace(0, 10, 101)
yyy = np.sin(dj*xxx)

fig = plt.figure() 
plt.plot(xxx, yyy)
st.pyplot(fig)








sigma = st.slider('Desvio Padrão', 0, 10, 2)
numeros = np.random.normal(mu, sigma, 100000)
lim_inferior = mu - 4*sigma
lim_superior = mu + 4*sigma

print(numeros)


fig = go.Figure()
fig.add_trace(go.Histogram(x=numeros))
fig.update_traces(xbins=dict(start=lim_inferior, end=lim_superior, size=0.5))
fig.update_layout(xaxis_range=[0, 40])
fig.update_layout(xaxis_title="Valor Obtido", yaxis_title="A área até aqui é a probabilidade")

st.plotly_chart(fig, use_container_width=False)