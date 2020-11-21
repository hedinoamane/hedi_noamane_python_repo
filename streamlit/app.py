import streamlit as st
import numpy as np
import pandas as pd



DATA_URL = 'data/annual-enterprise-survey-2019-financial-year-provisional.csv'
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


data_load_state = st.text('Loading data...')
data = load_data(10000)


data_load_state.text('Done! (using st.cache)')

st.subheader('Data\'s columns')
st.write(data.columns.tolist())

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
