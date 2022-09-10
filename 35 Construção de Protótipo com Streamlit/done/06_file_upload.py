from datetime import datetime, time
import numpy as np
import pandas as pd
import streamlit as st
import great_expectations as ge
import json

uploaded_file = st.file_uploader("submeta um arquivo!")

df = pd.DataFrame()
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    df = ge.from_pandas(df)

    df.expect_column_values_to_be_unique(column="PassengerId")


    uniqueness = df.expect_column_values_to_be_unique(column="PassengerId")
    
    uniqueness
    # st.markdown(f"uniqueness test is {uniqueness}")


    age_is_coherent = df.expect_column_values_to_be_between(
        column="Age", min_value=0, max_value=120
    )

    age_is_coherent



