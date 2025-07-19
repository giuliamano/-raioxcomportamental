import streamlit as st

def aplicar_estilo():
    st.markdown(
        """
        <style>
            body {
                background-color: #f7f0e8;
            }

            .main {
                background-color: #fff;
                padding: 2rem;
                border-radius: 12px;
            }

            h1, h2, h3 {
                color: #5e412f;
            }

            .stButton>button {
                background-color: #c7a17a;
                color: white;
                border: none;
                padding: 0.6rem 1.2rem;
                border-radius: 6px;
            }

            .stButton>button:hover {
                background-color: #a67c52;
            }

            .stTextInput>div>div>input {
                background-color: #fffaf2;
            }

            .stRadio>div>label {
                background-color: #fff;
                padding: 0.5rem;
                border-radius: 8px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
