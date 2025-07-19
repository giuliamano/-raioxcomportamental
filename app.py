
import streamlit as st
import pandas as pd
import datetime
import gspread
from config.estilo import aplicar_estilo
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import json

st.set_page_config(page_title="Raio-X Comportamental", layout="centered")

aplicar_estilo()
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
    "Estar com alguém que está comendo me dá frequentemente vontade de comer também.",
    "Quando me sinto tenso(a) ou estressado(a), frequentemente sinto que preciso comer.",
    "Entre as refeições principais, eu frequentemente belisco pedaços de alimentos. Ex: abro a geladeira, pego umas uvas e como andando.",
    "Eu conscientemente me controlo nas refeições para evitar ganhar peso.",
    "Se a comida me parece apetitosa, como mais do que o habitual.",
    "Se meu peso aumenta, como menos do que o habitual.",
    "Se vejo ou sinto o aroma de algo muito gostoso, sinto um desejo muito forte de comer.",
    "Se tenho alguma coisa muito saborosa para comer, como-a de imediato.",
    "Durante as refeições, controlo a quantidade do que como.",
    "Tenho desejo de comer quando estou procrastinando algo.",
    "Consigo deixar de comer alimentos muito apetitosos.",
    "Levo em consideração meus objetivos e valores quando escolho o que vou comer.",
    "Quando preparo uma refeição, costumo petiscar alguma coisa.",
    "Eu deliberadamente consumo pequenas porções para controlar meu peso.",
    "Comi mesmo sem estar com fome porque estava entediado(a).",
    "Comi mesmo sem estar com fome porque estava me sentindo ansioso(a), triste ou estressado(a).",
    "Sinto que mereço comer algo gostoso depois de um dia difícil.",
    "Como mesmo sem fome quando estou sobrecarregado(a) ou sem tempo.",
    "Evito desperdiçar comida mesmo quando estou satisfeito(a).",
    "Sinto que não consigo parar de comer certos alimentos, mesmo sem fome.",
    "Tenho dificuldade em recusar comida quando insistem.",
    "Como mais do que quero só porque paguei ou é uma ocasião especial.",
    "Quando estou em eventos sociais, como para acompanhar os outros."
]


opcoes_comportamento = ["Nunca", "Às vezes", "Frequentemente", "Quase sempre"]
respostas_comportamento = []


for i, pergunta in enumerate(comportamentos):
    resposta = st.radio(pergunta, opcoes_comportamento, key=f"comp_{i}")
    respostas_comportamento.append(resposta)

st.markdown("---")

# Pensamentos sabotadores
st.subheader("🧠 Pensamentos Sabotadores")
st.markdown("Esses são **pensamentos comuns que podem atrapalhar** seus resultados. Se identificar com algum deles já é um grande passo.")

pensamentos = [
    "Já pensei: 'Já que comi um pedaço, agora vou comer tudo e recomeço amanhã'.",
    "Já pensei: 'Estou tão sem tempo, não consigo seguir nada agora.'",
    "Já pensei: 'Não posso desperdiçar, então vou comer mesmo sem fome.'",
    "Me senti obrigado(a) a comer porque insistiram, mesmo sem querer tanto.",
    "Já pensei: 'Já que paguei por isso, preciso aproveitar.'",
    "Comi em maior quantidade só porque era uma ocasião especial ou algo que não como frequentemente.",
    "Já pensei: 'Já que não estou fazendo tudo certo, não tem problema comer isso.'",
    "Já pensei: 'Depois eu compenso isso.'",
    "Acreditei que merecia comer algo porque tive um dia ruim.",
    "Me deixei levar pela ideia de que 'é só hoje'."
]

opcoes_pensamentos = ["Não me identifico", "Me identifico um pouco", "Me identifico muito"]
respostas_pensamentos = []

for i, pensamento in enumerate(pensamentos):
    resposta = st.radio(pensamento, opcoes_pensamentos, key=f"pens_{i}")
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
        # --- Etapa 5: Análise dos Resultados por Categoria ---

# Mapear perguntas para categorias
mapa_categorias = {
    "Fome Emocional": [
        "Costumo comer quando estou entediado(a).",
        "A comida me conforta quando estou triste, ansioso(a) ou frustrado(a).",
        "Sinto que mereço comer algo gostoso depois de um dia difícil.",
        "Como mesmo sem fome quando estou sobrecarregado(a) ou sem tempo.",
        "Tenho desejo de comer quando estou procrastinando algo.",
        "Quando me sinto tenso(a) ou estressado(a), frequentemente sinto que preciso comer.",
        "Comi mesmo sem estar com fome porque estava entediado(a).",
        "Comi mesmo sem estar com fome porque estava me sentindo ansioso(a), triste ou estressado(a).",
    ],
    "Comer por Influência Externa": [
        "Estar com alguém que está comendo me dá frequentemente vontade de comer também.",
        "Se vejo ou sinto o aroma de algo muito gostoso, sinto um desejo muito forte de comer.",
        "Se tenho alguma coisa muito saborosa para comer, como-a de imediato.",
        "Quando preparo uma refeição, costumo petiscar alguma coisa.",
        "Se a comida me parece apetitosa, como mais do que o habitual.",
        "Quando estou em eventos sociais, como para acompanhar os outros.",
        "Tenho dificuldade em recusar comida quando insistem.",
        "Entre as refeições principais, eu frequentemente belisco pedaços de alimentos.",
    ],
    "Autocontrole e Valores": [
        "Eu conscientemente me controlo nas refeições para evitar ganhar peso.",
        "Se meu peso aumenta, como menos do que o habitual.",
        "Durante as refeições, controlo a quantidade do que como.",
        "Consigo deixar de comer alimentos muito apetitosos.",
        "Levo em consideração meus objetivos e valores quando escolho o que vou comer.",
        "Eu deliberadamente consumo pequenas porções para controlar meu peso.",
    ]
}

# Converter respostas em valores numéricos
valores = {
    "Nunca": 0,
    "Às vezes": 1,
    "Frequentemente": 2,
    "Quase sempre": 3
}

respostas_dict = dict(zip(comportamentos, respostas_comportamento))

medias = {}
for categoria, perguntas in mapa_categorias.items():
    soma = 0
    total = 0
    for pergunta in perguntas:
        resposta = respostas_dict.get(pergunta)
        if resposta is not None:
            soma += valores.get(resposta, 0)
            total += 1
    medias[categoria] = round(soma / total, 2) if total > 0 else 0

# --- Exibir Resultados com interpretação ---
st.markdown("## 📊 Sua Análise Comportamental")
st.write("Abaixo está um resumo da sua pontuação por categoria. Esses dados ajudam a identificar padrões que podem estar influenciando sua alimentação.")

interpretacao_categoria = {
    "Fome Emocional": """
**Fome Emocional** refere-se ao impulso de comer em resposta a emoções — como estresse, tristeza, ansiedade ou tédio — e não à fome física.

- **Pontuação baixa (0–1):** você demonstra equilíbrio ao lidar com emoções sem recorrer à comida.
- **Pontuação média (1.1–2):** indica que, às vezes, a comida é usada como válvula de escape. Isso é comum e pode ser trabalhado com estratégias práticas.
- **Pontuação alta (2.1–3):** a alimentação pode estar sendo usada com frequência para regular emoções. Isso merece atenção, mas é totalmente possível de ser transformado com apoio e consciência.
""",
    "Comer por Influência Externa": """
**Comer por Influência Externa** acontece quando comemos mais por estímulos do ambiente do que por necessidade física — como cheiro, visão de comida, pressão social ou hábitos automáticos.

- **Pontuação baixa (0–1):** você tende a se guiar bem pelos seus sinais internos de fome e saciedade.
- **Pontuação média (1.1–2):** mostra que alguns estímulos externos influenciam sua alimentação.
- **Pontuação alta (2.1–3):** o ambiente pode estar determinando grande parte do seu comportamento alimentar. Pequenas mudanças podem ter grande impacto.
""",
    "Autocontrole e Valores": """
**Autocontrole e Valores** refletem o quanto suas escolhas alimentares estão alinhadas aos seus objetivos, valores pessoais e autorregulação.

- **Pontuação baixa (0–1):** pode haver dificuldade em aplicar escolhas conscientes e consistentes.
- **Pontuação média (1.1–2):** você está no caminho, com espaço para fortalecimento do autocontrole.
- **Pontuação alta (2.1–3):** você demonstra consciência e alinhamento entre seus valores e comportamento alimentar. Muito positivo!
"""
}

for categoria, media in medias.items():
    st.markdown(f"### 🔸 {categoria}")
    st.markdown(f"**Sua pontuação média:** `{media}`")
    st.markdown(interpretacao_categoria[categoria])
    st.markdown("---")

# Aviso sobre validação científica
st.info("🔍 **Este questionário ainda não foi validado cientificamente em estudos publicados**, mas foi baseado em instrumentos previamente validados na literatura. Os resultados não têm valor diagnóstico, mas funcionam como um guia valioso para reflexões e acompanhamento nutricional.")

