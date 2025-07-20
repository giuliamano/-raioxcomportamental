import streamlit as st

def aplicar_estilo():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');

        /* Fundo com textura bege sofisticada */
        body {
            background-image: url('https://i.imgur.com/YAr2S9r.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        html, body, [class*="css"] {
            font-family: 'Playfair Display', serif;
            color: #3e3e3e;
            background-color: rgba(255, 255, 255, 0.85);
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

        /* Botões */
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

        /* Perguntas */
        .stRadio > div {
            background-color: #f2ebe3;
            border-radius: 10px;
            padding: 0.8rem;
            margin-bottom: 1rem;
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
