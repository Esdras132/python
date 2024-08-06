import streamlit as st
import pandas as pd

# Logo
st.logo(image='logo_login.png')


# Carregar os dados do CSV
df = pd.read_json("data.json", dtype={'barcode': str, 'internal_code': str})


# Configuração da página
st.set_page_config(page_title='Produtos', page_icon='icon_logo.png')


# Barra lateral para seleção de categoria
categorias = ["TODOS"] + df["categoria"].unique().tolist()
tipo = st.sidebar.selectbox('Categoria', categorias)


# Filtrar os dados com base na categoria selecionada
if tipo == "TODOS":
    filtro = df
else:
    filtro = df[df['categoria'] == tipo]

# Campo de pesquisa por código de barras
pesquisa_barcode = st.sidebar.text_input('Digite o Código de Barras')

# Aplicar filtro pelo código de barras, se houver
if pesquisa_barcode:
    filtro = filtro[filtro['barcode'].str.contains(pesquisa_barcode)]

# Verificar se o filtro resultante está vazio
if filtro.empty:
    st.sidebar.warning('Nenhum resultado encontrado para o código de barras especificado.')
else:
    st.dataframe(filtro)