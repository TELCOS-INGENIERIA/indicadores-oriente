import streamlit as st

st.set_page_config(
    page_title="Dashboard Indicadores Oriente",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Indicadores Oriente")

st.success("La aplicación está funcionando correctamente")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Indicadores", "16")

with col2:
    st.metric("Cumplen", "10")

with col3:
    st.metric("No cumplen", "6")

st.divider()

st.subheader("Próximamente")

st.write("✅ Filtros por Regional")
st.write("✅ Filtros por Ciudad")
st.write("✅ Histórico mensual")
st.write("✅ Detalle de órdenes")
