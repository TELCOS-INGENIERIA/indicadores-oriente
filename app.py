import streamlit as st
import pandas as pd

st.title("Prueba Excel")

archivo = pd.ExcelFile("Data.xlsx")

st.write("Hojas encontradas:")

st.write(archivo.sheet_names)
