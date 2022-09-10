import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import load
import os

st.title("Prevendo o Titanic :passenger_ship: :passenger_ship:")

model = load("titanic.joblib")

train = pd.read_csv("train.csv")
train = train[["Pclass", "Sex", "Age", "Survived"]]
x_train = train.drop(["Survived"], axis=1)
y_train = train["Survived"]

teste = pd.read_csv("teste.csv")
x_test = teste.drop(["Survived"], axis=1)
y_test = teste["Survived"]


score_train = model.score(x_train, y_train)
score_test = model.score(x_test, y_test)

st.header("Vendo nossos scores")

st.slider("Train Score:", min_value=0.0, max_value=1.0, value=float(score_train))
st.slider("Test Score:", min_value=0.0, max_value=1.0, value=float(score_test))

st.markdown("---")

st.dataframe(train.head())

st.markdown("---")

with st.form("predict_data"):
    st.header("Predição de dados do Titanic!")
    gender = st.selectbox("Gênero", ["Masculino", "Feminino"])
    age = st.slider("Idade", 0, 100, value=70)
    class_ = st.radio("Qual classe?", options=["1ª", "2ª", "3ª"])
    st.form_submit_button("Prever!")

gender = "male" if gender == "Masculino" else "female"
class_ = int(class_[0])

data = pd.DataFrame({"Pclass": class_, "Sex": gender, "Age": age}, index=[0])


prediction = model.predict(data)
prob = model.predict_proba(data)


if prediction == 1:
    st.header("Você sobrevive!!")
    st.balloons()
else:
    st.header("Você não sobrevive ☹️")


st.markdown("---")
st.table(data)
prediction[0]
prob
