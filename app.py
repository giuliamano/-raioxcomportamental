import streamlit as st
import pandas as pd
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.estilo import aplicar_estilo
from datetime import datetime

st.set_page_config(page_title="Raio-X Comportamental", layout="centered")
aplicar_estilo()

# Cabeçalho com imagem
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #5e412f;">🧠 Raio-X Comportamental</h1>
        <p style="font-size: 1.1rem; max-width: 700px; margin: 0 auto;">
            Olá! Prazer, meu nome é <strong>Giulia</strong>. Sou nutricionista e desenvolvi este questionário para ajudar você a entender melhor seus padrões alimentares e pensamentos que podem estar interferindo nos seus resultados.
        </p>
        <p style="font-size: 1rem; color: #6a5d4d;">
            <strong>Importante:</strong> Não existe resposta certa ou errada. O mais importante é você se reconhecer com sinceridade.<br>
            Caso alguma frase não represente exatamente o que você pensa, mas se aproxima, selecione-a mesmo assim.
        </p>
        <p style="margin-top: 1rem;">
            📲 Instagram: <a href="https://instagram.com/nutrigiuliamano" target="_blank">@nutrigiuliamano</a><br>
            📞 WhatsApp: (11) 97592-5467
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Dados pessoais
st.header("Seus dados")
nome = st.text_input("Nome completo")
email = st.text_input("E-mail")
celular = st.text_in_
