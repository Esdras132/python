import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# onde esta o arquivo 
df = pd.read_csv("test01\dados.csv", sep=";", decimal=',', encoding='utf-8')
df["Data"] = pd.to_datetime(df["Data"])
df=df.sort_values("Data")

df["Month"] = df["Data"].apply(lambda x: str(x.year) + '/' + str(x.month))

# Designer do filtro 
Month = st.sidebar.selectbox('Mês', df["Month"].unique().tolist())

# filtro 
df_filtered= df[df["Month"] == Month]
df_filtered

# Aqui é para dizer que o metodo df e uma tabela e que é para ele aparecer
st.dataframe(df)

# iniciar sistema 
# streamlit run test01\main.py 