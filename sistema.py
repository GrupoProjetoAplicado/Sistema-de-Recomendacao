import streamlit as st
import pandas as pd
from pathlib import Path

# Caminho do repositório
file_path = Path(__file__).parent / "hoteis_sustentaveis_DATASET.xlsx"
df = pd.read_excel(file_path)

st.title("🔎 Sistema de Recomendação de Hotéis Sustentáveis")

# Campos de entrada
nome = st.text_input("Nome do hotel (opcional)")
uf = st.text_input("Estado (UF)").upper()
cidade = st.text_input("Cidade").title()
pratica = st.text_input("Prática sustentável")
certificacao = st.text_input("Certificação")
selo = st.text_input("Selo")

# Filtragem
resultado = df.copy()

if nome:
    resultado = resultado[resultado['Nome'].str.contains(nome, case=False, na=False)]
if uf:
    resultado = resultado[resultado['UF'].str.upper() == uf]
if cidade:
    resultado = resultado[resultado['Município'].str.contains(cidade, case=False, na=False)]
if pratica:
    resultado = resultado[resultado['Práticas de Sustentabilidade'].str.contains(pratica, case=False, na=False)]
if certificacao:
    resultado = resultado[resultado['Certificação'].str.contains(certificacao, case=False, na=False)]
if selo:
    resultado = resultado[resultado['Selo'].str.contains(selo, case=False, na=False)]

st.success(f"✅ Encontramos {resultado.shape[0]} hospedagem(ns) sustentável(is) para você!")
st.dataframe(resultado[['Nome', 'UF', 'Município', 'Práticas de Sustentabilidade', 'Certificação', 'Selo', 'Fonte']].reset_index(drop=True))