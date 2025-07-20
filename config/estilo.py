import streamlit as st

def aplicar_estilo():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
            background-color: #f9f5f0 !important;
            color: #3e3e3e !important;
        }

        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            color: #4b3621 !important;
        }

        /* Botões bonitos */
        .stButton > button {
            background-color: #d9c4aa !important;
            color: #3e3e3e !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 1rem !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.6rem 1.2rem !important;
            transition: background-color 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #c5b293 !important;
            color: #000000 !important;
        }

        /* Radios com estilo */
        .stRadio > div {
            background-color: #f2ebe3 !important;
            padding: 0.8rem !important;
            border-radius: 10px !important;
            margin-bottom: 1rem !important;
        }

        .stRadio label {
            font-size: 1rem !important;
            font-family: 'Inter', sans-serif !important;
            color: #3e3e3e !important;
        }

        /* Remove fundo/cabeçalho automático */
        [data-testid="stHeader"] {
            background-color: transparent !important;
            background-image: none !important;
        }

        /* Campos de texto */
        input, textarea {
            font-family: 'Inter', sans-serif !important;
            background-color: #ffffff !important;
            color: #3e3e3e !important;
            border-radius: 6px !important;
        }
        </style>
    """, unsafe_allow_html=True)
