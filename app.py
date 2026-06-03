import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard Indicadores Oriente",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def cargar_datos():
    return pd.read_excel(
        "Data.xlsx",
        sheet_name="EXPORT_WEB"
    )

df = cargar_datos()

st.title("📊 Dashboard Indicadores Oriente")

# FILTROS
col1, col2, col3 = st.columns(3)

with col1:
    mes = st.selectbox(
        "Mes",
        sorted(df["Mes"].dropna().unique())
    )

with col2:
    regional = st.selectbox(
        "Regional",
        ["Todas"] + sorted(df["Regional"].dropna().unique().tolist())
    )

with col3:
    kpi = st.selectbox(
        "KPI",
        ["Todos"] + sorted(df["KPI"].dropna().unique().tolist())
    )

df_filtrado = df[df["Mes"] == mes]

if regional != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Regional"] == regional]

if kpi != "Todos":
    df_filtrado = df_filtrado[df_filtrado["KPI"] == kpi]

# INDICADORES
cumplen = (df_filtrado["Estado"] == "Cumple").sum()
no_cumplen = (df_filtrado["Estado"] == "No Cumple").sum()
total = len(df_filtrado)

porcentaje_cumplimiento = (
    round((cumplen / total) * 100, 2)
    if total > 0 else 0
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Registros", total)
c2.metric("Cumplen", cumplen)
c3.metric("No cumplen", no_cumplen)
c4.metric("% Cumplimiento", f"{porcentaje_cumplimiento}%")

st.divider()

# TABLA
st.subheader("Detalle de Indicadores")

st.dataframe(
    df_filtrado,
    use_container_width=True,
    hide_index=True
)
