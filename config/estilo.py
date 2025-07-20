import streamlit as st

def aplicar_estilo():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');

        html, body, [class*="css"] {
            background-color: #f9f5f0 !important;
            font-family: 'Inter', sans-serif;
            color: #3e3e3e;
        }

        h1, h2, h3 {
            font-family: 'Playfair Display', serif;
            color: #5e412f;
        }

        input, textarea {
            background-color: #ffffff !important;
            border-radius: 6px !important;
        }

        .stButton > button {
            background-color: #d9c4aa;
            color: #3e3e3e;
            border: none;
            padding: 0.5rem 1.2rem;
            border-radius: 8px;
            font-size: 1rem;
            font-family: 'Inter', sans-serif;
            transition: 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #c5b293;
            color: #000000;
        }

        .stRadio > div {
            background-color: #f2ebe3;
            border-radius: 10px;
            padding: 0.8rem;
            margin-bottom: 1rem;
        }

        label {
            font-size: 1rem !important;
            font-family: 'Inter', sans-serif;
        }

        .stAlert {
            border-radius: 8px;
        }

        body::before {
            content: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
