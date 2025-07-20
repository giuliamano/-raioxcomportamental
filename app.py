import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.estilo import aplicar_estilo

# Aplica o estilo visual refinado
aplicar_estilo()

st.set_page_config(page_title="Raio-X Comportamental", layout="centered")

st.markdown("<h1 style='text-align: center;'>🧠 Raio-X Comportamental</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Responda com sinceridade para descobrir padrões do seu comportamento alimentar.</p>", unsafe_allow_html=True)
st.markdown("---")

# Dados iniciais
nome = st.text_input("Seu nome completo")
email = st.text_input("Seu e-mail")
celular = st.text_input("Seu celular (com DDD)")

# Blocos de perguntas organizados por página
blocos = [
    [
        "Costumo comer quando estou entediado(a), mesmo sem fome.",
        "Comi mesmo sem estar com fome porque estava ansioso(a), triste ou estressado(a).",
        "Sinto que mereço comer algo gostoso depois de um dia difícil.",
        "Como mesmo sem fome quando estou sobrecarregado(a) ou sem tempo.",
        "Tenho desejo de comer quando estou procrastinando algo.",
        "Acreditei que merecia comer algo porque tive um dia ruim.",
    ],
    [
        "Estar com alguém que está comendo me dá vontade de comer também.",
        "Se vejo ou sinto o aroma de algo muito gostoso, sinto um desejo forte de comer.",
        "Se a comida me parece apetitosa, como mais do que o habitual.",
        "Quando estou em eventos sociais, como para acompanhar os outros.",
        "Me senti obrigado(a) a comer porque insistiram, mesmo sem querer tanto.",
        "Tenho dificuldade em recusar comida quando insistem.",
        "Como mais do que quero só porque paguei ou é uma ocasião especial.",
    ],
    [
        "Eu conscientemente me controlo nas refeições para evitar ganhar peso.",
        "Durante as refeições, controlo a quantidade do que como.",
        "Consigo deixar de comer alimentos muito apetitosos.",
        "Levo em consideração meus objetivos e valores quando escolho o que vou comer.",
        "Evito desperdiçar comida mesmo quando estou satisfeito(a).",
        "Já pensei: 'Depois eu compenso isso.'",
        "Já pensei: 'Já que comi um pedaço, agora vou comer tudo e recomeço amanhã'.",
        "Já pensei: 'Já que não estou fazendo tudo certo, não tem problema comer isso.'"
    ]
]

opcoes = ["Nunca", "Às vezes", "Frequentemente", "Quase sempre"]

# Estado da página
if "pagina" not in st.session_state:
    st.session_state.pagina = 0

# Coleta das respostas por página
if "respostas" not in st.session_state:
    st.session_state.respostas = []

# Mostra perguntas da página atual
pagina_atual = st.session_state.pagina
respostas_pagina = []
for i, pergunta in enumerate(blocos[pagina_atual]):
    resposta = st.radio(pergunta, opcoes, key=f"pergunta_{pagina_atual}_{i}")
    respostas_pagina.append(resposta)

# Botões de navegação
col1, col2 = st.columns(2)
with col1:
    if st.session_state.pagina > 0:
        if st.button("⬅️ Voltar"):
            st.session_state.pagina -= 1

with col2:
    if st.button("Próximo ➡️"):
        st.session_state.respostas.extend(respostas_pagina)
        if st.session_state.pagina < len(blocos) - 1:
            st.session_state.pagina += 1
        else:
            st.session_state.pagina += 1  # Vai para tela final

# Última página: envio e análise
if st.session_state.pagina == len(blocos):
    st.markdown("---")
    st.markdown("### Enviar respostas")

    if st.button("📨 Enviar respostas"):
        if nome and email and celular:
            try:
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                secret_dict = st.secrets["gcp_service_account"]
                creds = ServiceAccountCredentials.from_json_keyfile_dict(secret_dict, scope)
                client = gspread.authorize(creds)
                sheet = client.open("Raio-X Comportamental - Respostas").sheet1

                data = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), nome, email, celular] + st.session_state.respostas
                sheet.append_row(data)

                st.success("Respostas enviadas com sucesso! Obrigada por participar 💛")
            except Exception as e:
                st.error(f"Erro ao salvar na planilha: {e}")
        else:
            st.warning("Por favor, preencha todos os campos antes de enviar.")

    if len(st.session_state.respostas) == sum(len(b) for b in blocos):
        st.markdown("---")
        st.markdown("### 🧾 Resultado do Raio-X Comportamental")

        # Mapeia respostas para pontuações
        mapa = {"Nunca": 0, "Às vezes": 1, "Frequentemente": 2, "Quase sempre": 3}
        pontuacoes = [mapa[r] for r in st.session_state.respostas]

        # Cálculo das médias por categoria
        categorias = {
            "Fome Emocional": pontuacoes[0:6],
            "Comer por Influência Externa": pontuacoes[6:13],
            "Autocontrole e Valores": pontuacoes[13:23]
        }

        for nome_cat, valores in categorias.items():
            media = sum(valores) / len(valores)
            st.markdown(f"**{nome_cat}** — Média: **{media:.2f}**")

            if nome_cat == "Fome Emocional":
                if media >= 2.5:
                    st.write("👉 Você apresenta sinais claros de comer em resposta às emoções. Observar e acolher esses momentos pode ser um passo importante.")
                elif media >= 1.5:
                    st.write("👉 Há momentos em que as emoções influenciam sua alimentação. Reflita sobre esses padrões.")
                else:
                    st.write("✅ Pouca influência emocional na sua alimentação.")

            elif nome_cat == "Comer por Influência Externa":
                if media >= 2.5:
                    st.write("👉 Influências externas impactam fortemente suas escolhas alimentares. Isso pode atrapalhar seus objetivos.")
                elif media >= 1.5:
                    st.write("👉 Certos contextos sociais ou visuais podem levar você a comer mais.")
                else:
                    st.write("✅ Boa autonomia frente às influências externas.")

            elif nome_cat == "Autocontrole e Valores":
                if media >= 2.5:
                    st.write("✅ Você demonstra ótimo alinhamento com seus valores e autocontrole.")
                elif media >= 1.5:
                    st.write("👉 Seu autocontrole varia dependendo da situação. Há espaço para fortalecer esse aspecto.")
                else:
                    st.write("⚠️ Baixo alinhamento com seus valores e controle. Que tal desenvolver isso com mais atenção?")

        st.info("📝 Este questionário é baseado em instrumentos científicos, mas **não foi validado como ferramenta diagnóstica**.")
