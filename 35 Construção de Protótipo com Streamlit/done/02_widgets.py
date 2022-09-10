from datetime import datetime, time
import numpy as np
import pandas as pd
import streamlit as st

st.title("Um pouco de Interatividade!")

# 01 - um input básico
name = st.text_input("Qual seu nome?")

# 02 - como fazer com que o texto acima não apareça caso não exista nome?

if name:
    st.markdown(f"Olá, *{name}*")

st.selectbox(
    "Você se identifica como...",
    options=["Homem", "Mulher", "N/B", "Prefiro não Declarar"],
)

rate = st.select_slider(
    "Qual a chance de você recomendar nosso produto?",
    options=np.arange(0, 10.5, 0.5),
    value=7,
)

age = st.number_input("Qual sua idade?", min_value=0, max_value=200, step=1)

if st.button("Submeter!"):
    st.write("Obrigado!!")

st.markdown("---")

like = st.checkbox("Você gostou do nosso produto?")

if like:
    st.balloons()
    st.text("Yay!")
else:
    st.text("Poxa 😕. Por favor, deixe um feedback!")

st.markdown("---")
work = st.slider("Que horas você costuma trabalhar?", value=(time(9), time(18)))
work
travel = st.slider(
    "Quando você viaja?",
    min_value=datetime(2020, 1, 1),
    max_value=datetime(2022, 1, 1),
    value=(datetime(2021, 6, 1), datetime(2022, 1, 1)),
    format="DD/MM/YY",
)
st.markdown("---")

st.select_slider(
    "Qual sua cor favorita?",
    options=["Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta"],
)


st.date_input("Quando é seu aniversário?")
st.time_input("Que horas você quer almoçar?")


