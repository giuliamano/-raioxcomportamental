
import streamlit as st
import pandas as pd
import datetime
st.write("CLIENT EMAIL:", st.secrets["gcp_service_account"].get("client_email", "Chave não encontrada"))
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import json

st.set_page_config(page_title="Raio-X Comportamental", layout="centered")

st.markdown(
    """
    <style>
        body { background-color: #f9f3e8; }
        .main { background-color: #f9f3e8; }
    </style>
    """, unsafe_allow_html=True
)

st.title("📋 Raio-X Comportamental")
st.markdown("""Olá! Eu sou a **nutricionista Giulia Mano**. Este questionário foi desenvolvido para ajudar você a entender melhor seus padrões alimentares e pensamentos que podem estar interferindo nos seus resultados.

**Importante:** todas as respostas são confidenciais e utilizadas apenas para acompanhamento nutricional.

Caso alguma frase não represente exatamente o que você pensa, selecione a que **mais se aproxima**.

📲 Instagram: [@nutrigiuliamano](https://instagram.com/nutrigiuliamano)  
📞 WhatsApp: (11) 97592-5467
""")

st.markdown("---")

# Dados pessoais
st.header("Seus dados")
nome = st.text_input("Nome completo")
email = st.text_input("E-mail")
celular = st.text_input("Celular (WhatsApp)")

st.markdown("---")

# Perguntas - Comportamentos Alimentares
st.subheader("🍽️ Comportamentos Alimentares")
comportamentos = [
    "Costumo comer quando estou entediado(a).",
    "A comida me conforta quando estou triste, ansioso(a) ou frustrado(a).",
    "Sinto que mereço comer algo gostoso depois de um dia difícil.",
    "Como mesmo sem fome quando estou sobrecarregado(a) ou sem tempo.",
    "Evito desperdiçar comida mesmo quando estou satisfeito(a).",
    "Sinto que não consigo parar de comer certos alimentos, mesmo sem fome.",
    "Tenho dificuldade em recusar comida quando insistem, mesmo sem querer.",
    "Como mais do que quero só porque paguei ou é uma ocasião especial.",
    "Quando estou em eventos sociais, como para agradar ou acompanhar os outros.",
    "Faço escolhas alimentares diferentes quando estou com outras pessoas."
]

opcoes_comportamento = ["Nunca", "Às vezes", "Frequentemente", "Quase sempre"]
respostas_comportamento = []

for pergunta in comportamentos:
    resposta = st.radio(pergunta, opcoes_comportamento, key=pergunta)
    respostas_comportamento.append(resposta)

st.markdown("---")

# Pensamentos sabotadores
st.subheader("🧠 Pensamentos Sabotadores")
st.markdown("Esses são **pensamentos comuns que podem atrapalhar** seus resultados. Se identificar com algum deles já é um grande passo.")

pensamentos = [
    "Já pensei: 'Já que comi um pedaço, agora vou comer tudo e recomeço amanhã'.",
    "Já pensei: 'Estou tão sem tempo, não consigo seguir nada agora.'",
    "Pensei: 'Não posso desperdiçar, então vou comer mesmo sem fome.'",
    "Me senti obrigado(a) a comer porque insistiram, mesmo sem querer.",
    "Pensei: 'Já paguei por isso, preciso aproveitar.'",
    "Comi algo porque era uma ocasião especial, mesmo sem vontade.",
    "Pensei: 'Já que não estou fazendo tudo certo, não adianta tentar.'",
    "Pensei: 'Depois eu compenso isso.'",
    "Acreditei que merecia comer algo porque tive um dia ruim.",
    "Me deixei levar pela ideia de que 'é só hoje'."
]

opcoes_pensamentos = ["Não me identifico", "Me identifico um pouco", "Me identifico muito"]
respostas_pensamentos = []

for pensamento in pensamentos:
    resposta = st.radio(pensamento, opcoes_pensamentos, key=pensamento)
    respostas_pensamentos.append(resposta)

st.markdown("---")

# Função para salvar no Google Sheets usando secrets
def salvar_resposta():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        secret_dict = st.secrets["gcp_service_account"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(secret_dict, scope)
        client = gspread.authorize(creds)

        sheet = client.open("Raio-X Comportamental - Respostas").sheet1
        data = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), nome, email, celular] + respostas_comportamento + respostas_pensamentos
        sheet.append_row(data)

        return True
    except Exception as e:
        st.error(f"Erro ao salvar na planilha: {e}")
        return False

# Botão de envio
if st.button("📨 Enviar respostas"):
    if nome and email and celular:
        sucesso = salvar_resposta()
        if sucesso:
            st.success("Respostas enviadas com sucesso! Obrigada por participar 💛")
    else:
        st.warning("Por favor, preencha todos os campos antes de enviar.")
