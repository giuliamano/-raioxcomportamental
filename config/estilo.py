# Novo estilo.py
import streamlit as st

def aplicar_estilo():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Georgia&display=swap');

            html, body, [class*="css"] {
                font-family: 'Georgia', serif;
                background-color: #f7f0e8;
                color: #333333;
            }

            .main {
                background-color: #ffffff;
                padding: 2rem;
                border-radius: 10px;
            }

            h1, h2, h3 {
                color: #5e412f;
            }

            .stButton>button {
                background-color: #bfa17b;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                border: none;
                padding: 0.6rem 1.2rem;
                font-size: 1rem;
            }

            .stButton>button:hover {
                background-color: #a88966;
                color: #fff;
            }

            .stRadio>div>label {
                background-color: #fffaf3;
                padding: 0.5rem 1rem;
                border-radius: 6px;
                border: 1px solid #e6d8c3;
                margin-bottom: 0.3rem;
                cursor: pointer;
            }

            .stTextInput>div>div>input {
                background-color: #fff;
                border: 1px solid #d6c9b5;
                padding: 0.5rem;
                border-radius: 6px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
