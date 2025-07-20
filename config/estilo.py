import streamlit as st

def aplicar_estilo():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
            color: #3e3e3e;
            background-color: #f9f5f0;
        }

        h1, h2, h3 {
            font-family: 'Playfair Display', serif;
            color: #5e412f;
        }

        .stButton > button {
            background-color: #d9c4aa !important;
            color: #3e3e3e !important;
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            border-radius: 8px;
            padding: 0.6rem 1.4rem;
            border: none;
        }

        .stButton > button:hover {
            background-color: #c5b293 !important;
            color: #000000 !important;
        }

        .stRadio > div {
            background-color: #f2ebe3;
            padding: 0.8rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }

        .stRadio > div > label {
            font-family: 'Inter', sans-serif !important;
            font-size: 1rem !important;
        }

        /* Corrige visual do cabeçalho se ainda houver imagem */
        header, [data-testid="stHeader"] {
            background: none;
        }
        </style>
    """, unsafe_allow_html=True)
