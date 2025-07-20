import streamlit as st
import pandas as pd
import datetime
import gspread
from config.estilo import aplicar_estilo
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

st.set_page_config(page_title="Raio-X Comportamental", layout="centered")

# Aplica o estilo visual
aplicar_estilo()
