import streamlit as st

def aplicar_estilo():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Playfair Display', serif;
            color: #3e3e3e;
            background-color: #f8f3ec;
        }

        /* Cabeçalhos */
        h1, h2, h3 {
            color: #5e412f;
        }

        /* Campos de input */
        input {
            background-color: #fff !important;
            border-radius: 6px !important;
        }

        /* Botões de envio */
        .stButton > button {
            background-color: #d9c4aa;
            color: #3e3e3e;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            font-size: 1rem;
            transition: 0.3s;
        }

        .stButton > button:hover {
            background-color: #c5b293;
            color: #000000;
        }

        /* Perguntas em radio */
        .stRadio > div {
            background-color: #f2ebe3;
            border-radius: 10px;
            padding: 0.8rem;
            margin-bottom: 1rem;
        }

        /* Estilo do botão selecionado */
        div[data-baseweb="radio"] label[data-selected="true"] {
            background-color: #d9c4aa;
            color: #000000 !important;
            border-radius: 8px;
            padding: 6px 12px;
        }

        /* Estilo do botão não selecionado */
        div[data-baseweb="radio"] label {
            background-color: #f8f3ec;
            color: #3e3e3e;
            border-radius: 8px;
            padding: 6px 12px;
        }

        label {
            font-size: 1rem !important;
        }

        /* Alertas */
        .stAlert {
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)
