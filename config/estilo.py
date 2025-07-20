import streamlit as st

def aplicar_estilo():
    st.markdown("""
        <style>
            /* Fundo geral da aplicação */
            .stApp {
                background-color: #f9f3e8;
            }
            /* Container principal */
            section[data-testid="stAppViewContainer"] > div {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 2rem;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            }
            /* Cabeçalhos */
            h1, h2, h3 {
                color: #5e412f !important;
                font-family: 'Segoe UI', sans-serif;
            }
            /* Botões */
            .stButton > button {
                background-color: #c7a17a;
                color: #ffffff;
                border-radius: 6px;
                padding: 0.6rem 1.2rem;
                font-size: 1rem;
                font-weight: bold;
            }
            .stButton > button:hover {
                background-color: #a67c52;
            }
            /* Inputs e radio */
            input, textarea, .stRadio > div {
                background-color: #fffaf2 !important;
            }
        </style>
        """, unsafe_allow_html=True)
