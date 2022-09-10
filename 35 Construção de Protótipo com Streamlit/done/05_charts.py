from random import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import streamlit as st

p = 0.53

x = list(range(100))

y = [10]

for idx, _ in enumerate(x[1:]):
    if random() <= p:
        y.append(y[idx - 1] + 1)
    else:
        y.append(y[idx - 1] - 1)

st.line_chart(y)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)


x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]
group_labels = ["Group 1", "Group 2", "Group 3"]

fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])

st.plotly_chart(fig, use_container_width=True)
