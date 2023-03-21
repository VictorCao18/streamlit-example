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


miles_per_gallon = st.number_input('Insert miles per gallon', max_value=100.00000)
dollars_per_gallon = st.number_input('Insert dollar cost per gallon', max_value=100.00000)

miles1 = driving_cost(miles_per_gallon, dollars_per_gallon, 10.0)
miles2 = driving_cost(miles_per_gallon, dollars_per_gallon, 50.0)
miles3 = driving_cost(miles_per_gallon, dollars_per_gallon, 400.0)

st.write(miles1.style.format("{:.2}"))
st.write(miles2.style.format("{:.2}"))
st.write(miles3.style.format("{:.2}"))
