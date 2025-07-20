import streamlit as st

def aplicar_estilo():
    st.markdown(
        """
        <style>
            /* Fundo geral da página */
            .stApp {
                background-color: #f9f3e8;
            }

            /* Título e subtítulos */
            h1, h2, h3 {
                color: #5e412f;
                font-family: 'Segoe UI', sans-serif;
            }

            /* Caixa branca em volta dos inputs */
            .block-container {
                background-color: #ffffff;
                padding: 2rem;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
            }

            /* Botões */
            .stButton>button {
                background-color: #c7a17a;
                color: white;
                border: none;
                padding: 0.6rem 1.2rem;
                border-radius: 6px;
                font-size: 1rem;
            }

            .stButton>button:hover {
                background-color: #a67c52;
            }

            /* Inputs */
            input, textarea {
                background-color: #fffaf2 !important;
            }

            /* Rádio buttons */
            .stRadio > div {
                background-color: #fff;
                padding: 0.5rem;
                border-radius: 8px;
            }

            /* Mensagens de sucesso e info */
            .stAlert {
                border-radius: 8px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
