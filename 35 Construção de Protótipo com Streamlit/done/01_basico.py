import streamlit as st

import numpy as np
import pandas as pd

# 01 - Exibindo um texto básico
st.title("Boas vindas ao Streamlit 🎉🎉!")

# 02 - Estruturas simples podem ser exibidas como no Terminal ou Jupyter
st.header("Exibindo valores literais")
10

"test"

["listas", "também", "funcionam!!"]

{"conjuntos", "também!"}

st.header("Exibindo dataframes")

# 03 - Também é possível usarmos o `st.write`
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

st.write(df)

df

st.table(df)
st.header("Um pouco de Interatividade")

# 04 - observe como o valor é dinamico!
show_df = st.checkbox("Show dataframe")

