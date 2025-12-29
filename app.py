import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Harvey Colchado - Diputado #1", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #0047ab; color: white; }
    .slogan { font-size: 24px; color: #d32f2f; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVEGACIÓN) ---
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="Harvey Colchado") # Reemplazar con foto real
    st.title("Ahora Nación")
    st.subheader("Número 1")
    menu = st.radio("Ir a:", ["Inicio", "Propuestas", "Transparencia Económica", "Donar Ahora"])

# --- DATOS DE EJEMPLO (En una app real, esto vendría de una base de datos o Google Sheets) ---
donaciones_data = pd.DataFrame({
    "Donante": ["Juan Pérez", "María Ramos", "Anónimo", "Luis Soto"],
    "Monto (S/)": [100, 500, 50, 200],
    "Fecha": ["2025-12-20", "2025-12-22", "2025-12-25", "2025-12-27"]
})

gastos_data = pd.DataFrame({
    "Concepto": ["Publicidad RRSS", "Volantes", "Alquiler Local", "Movilidad"],
    "Monto (S/)": [400, 150, 200, 100]
})

# --- LÓGICA DE NAVEGACIÓN ---

if menu == "Inicio":
    st.title("Harvey Colchado")
    st.markdown("<p class='slogan'>\"Tumbando a la corrupción\"</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("¿Quién es Harvey Colchado?")
        st.write("""
        Con años de experiencia en la lucha contra el crimen organizado y la alta corrupción, 
        Harvey Colchado da el paso a la política para limpiar el Congreso desde adentro. 
        Su compromiso es con la verdad y la justicia para todos los peruanos.
        """)
    with col2:
        st.info("**Partido:** Ahora Nación \n\n **Cargo:** Cámara de Diputados \n\n **Número:** 1")

elif menu == "Propuestas":
    st.header("Nuestras Propuestas para el Cambio")
    with st.expander("1. Reforma del Sistema de Justicia"):
        st.write("Implementar mecanismos
