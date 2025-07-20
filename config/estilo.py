import streamlit as st
import pandas as pd
import datetime
import gspread
from config.estilo import aplicar_estilo
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Configurações da página
st.set_page_config(page_title="Raio-X Comportamental", layout="centered")
aplicar_estilo()

# Cabeçalho bonito e limpo
st.markdown("<h1 style='text-align: center;'>🧠 Raio-X Comportamental</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 1.1rem;'>Este questionário te ajuda a refletir sobre seus comportamentos alimentares de forma acolhedora e sem julgamentos.</p>",
    unsafe_allow_html=True
)
st.markdown("---")
