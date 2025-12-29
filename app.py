import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Harvey Colchado | #1 Ahora Nación",
    page_icon="⚖️",
    layout="wide"
)

# --- ENCABEZADO ---
st.title("⚖️ Harvey Colchado")
st.subheader("Candidato al Congreso – Ahora Nación #1")
st.markdown("### **Tumbando a la corrupción**")

st.divider()

# --- SIDEBAR ---
menu = st.sidebar.radio(
    "Menú",
    ["Inicio", "Propuestas", "Acciones", "Transparencia", "Donaciones"]
)

# --- CARGA DE DATOS ---
donaciones = pd.read_csv("data/donaciones.csv")
gastos = pd.read_csv("data/gastos.csv")

total_ingresos = donaciones["monto"].sum()
total_gastos = gastos["monto"].sum()
balance = total_ingresos - total_gastos

# --- SECCIONES ---
if menu == "Inicio":
    st.write("""
    Harvey Colchado postula al Congreso con el compromiso de
    enfrentar la corrupción, fortalecer el Estado de derecho
    y recuperar la confianza ciudadana en las instituciones.
    """)

elif menu == "Propuestas":
    st.markdown("""
    **Ejes principales:**
    - Lucha frontal contra la corrupción
    - Control político y fiscalización real
    - Reforma institucional y transparencia
    """)

elif menu == "Acciones":
    acciones = pd.read_csv("data/acciones.csv")
    st.dataframe(acciones)

elif menu == "Transparencia":
    col1, col2, col3 = st.columns(3)

    col1.metric("Ingresos (S/)", f"{total_ingresos:,.2f}")
    col2.metric("Gastos (S/)", f"{total_gastos:,.2f}")
    col3.metric("Balance (S/)", f"{balance:,.2f}")

    st.subheader("Donaciones registradas")
    st.dataframe(donaciones)

    st.subheader("Gastos de campaña")
    st.dataframe(gastos)

    st.caption(
        "Información publicada con fines de transparencia. "
        "Los datos serán reportados conforme a la normativa ONPE."
    )

elif menu == "Donaciones":
    st.markdown("""
    ### Apoya la campaña
    Las donaciones se realizan únicamente a través de
    canales autorizados y conforme a la ley electoral.
    """)

    st.link_button(
        "Donar vía plataforma autorizada",
        "https://example.com"
    )

    st.caption(
        "Las donaciones están sujetas a límites y fiscalización ONPE."
    )
