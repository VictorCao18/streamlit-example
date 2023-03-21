from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    dollars = (dollars_per_gallon / miles_per_gallon) * miles_driven
    return dollars 


miles_per_gallon = st.number_input('Insert a number')
dollars_per_gallon = st.number_input('Insert a number')

miles1 = driving_cost(miles_per_gallon, dollars_per_gallon, 10.0)
miles2 = driving_cost(miles_per_gallon, dollars_per_gallon, 50.0)
miles3 = driving_cost(miles_per_gallon, dollars_per_gallon, 400.0)

st.write(f'{miles1:.2f}')
st.write(f'{miles2:.2f}')
st.write(f'{miles3:.2f}')
