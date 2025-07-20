import streamlit as st

def aplicar_estilo():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #f9f5f0;
            color: #3e3e3e;
        }

        h1, h2, h3 {
            font-family: 'Playfair Display', serif;
            color: #4b3621;
        }

        /* Botões */
        .stButton > button {
            background-color: #d9c4aa !important;
            color: #3e3e3e !important;
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            transition: background-color 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #c5b293 !important;
            color: #000000 !important;
        }

        /* Estilo das perguntas (st.radio) */
        .stRadio > div {
            background-color: #f2ebe3;
            padding: 0.8rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }

        .stRadio label {
            font-size: 1rem !important;
            font-family: 'Inter', sans-serif !important;
            color: #3e3e3e !important;
        }

        /* Remove imagem ou cor do cabeçalho padrão do Streamlit */
        [data-testid="stHeader"] {
            background-color: transparent !important;
            background-image: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
