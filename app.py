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
            <strong>Importante:</strong> Não existe resposta certa ou errada.  O mais importante é você se reconhecer com sinceridade.<br>
            Caso alguma frase não represente exatamente o que você pensa, mas se aproxima, selecione a que <strong>mais se aproxima</strong>.
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
celular = st.text_input("Celular (WhatsApp)")
st.markdown("---")

# Perguntas principais
perguntas_comportamento = [
    "Estar com alguém que está comendo me dá vontade de comer também.",
    "Quando me sinto tenso(a) ou estressado(a), frequentemente sinto necessidade de comer.",
    "Belisco entre as refeições. Ex: pego umas uvas na geladeira enquanto caminho.",
    "Eu conscientemente me controlo durante as refeições para evitar ganhar peso.",
    "Quando a comida me parece muito apetitosa, como mais do que o habitual.",
    "Quando meu peso aumenta, reduzo a quantidade do que como.",
    "Quando vejo ou sinto o aroma de algo muito gostoso, sinto um desejo forte de comer.",
    "Quando tenho algo muito saborosa para comer, como imediatamente.",
    "Durante as refeições, controlo a quantidade do que como.",
    "Tenho vontade de comer quando estou adiando alguma tarefa.",
    "Consigo resistir a alimentos muito apetitosos.",
    "Levo em consideração meus objetivos e valores na hora de escolher o que comer.",
    "Enquanto preparo a comida, costumo petiscar alguma coisa.",
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

pensamentos_sabotadores = [
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

opcoes_freq = ["Nunca", "Às vezes", "Frequentemente", "Quase sempre"]
opcoes_sabotagem = ["Não me identifico", "Me identifico um pouco", "Me identifico muito"]

# Estados de sessão
por_pagina = 6
total_paginas = (len(perguntas_comportamento) + por_pagina - 1) // por_pagina

if "pagina" not in st.session_state:
    st.session_state.pagina = 1
if "respostas_comportamento" not in st.session_state:
    st.session_state.respostas_comportamento = [""] * len(perguntas_comportamento)
if "respostas_pensamentos" not in st.session_state:
    st.session_state.respostas_pensamentos = [""] * len(pensamentos_sabotadores)
if "respostas_enviadas" not in st.session_state:
    st.session_state.respostas_enviadas = False
# Exibe perguntas de acordo com a página atual
indice_inicial = (st.session_state.pagina - 1) * por_pagina
indice_final = indice_inicial + por_pagina

with st.form(key=f"pagina_{st.session_state.pagina}"):
    st.subheader(f"Bloco {st.session_state.pagina}")
    for i in range(indice_inicial, min(indice_final, len(perguntas_comportamento))):
        resposta = st.radio(
            f"{i + 1}. {perguntas_comportamento[i]}",
            opcoes_freq,
            index=opcoes_freq.index(st.session_state.respostas_comportamento[i]) if st.session_state.respostas_comportamento[i] else 0,
            key=f"comportamento_{i}"
        )
        st.session_state.respostas_comportamento[i] = resposta

    col1, col2 = st.columns([1, 1])
    if st.session_state.pagina > 1:
        voltar = col1.form_submit_button("Voltar")
    else:
        voltar = False
    if st.session_state.pagina < total_paginas:
        avancar = col2.form_submit_button("Próximo")
    else:
        avancar = col2.form_submit_button("Ir para Pensamentos Sabotadores")

    if voltar:
        st.session_state.pagina -= 1
    elif avancar:
        st.session_state.pagina += 1
# Página dos Pensamentos Sabotadores
if st.session_state.pagina == total_paginas + 1:
    st.subheader("🧠 Pensamentos Sabotadores")
    st.markdown("Esses são **pensamentos comuns que podem atrapalhar** seus resultados. Se identificar com algum deles já é um grande passo.")

    with st.form(key="pensamentos_form"):
        for i, pensamento in enumerate(pensamentos_sabotadores):
            resposta = st.radio(
                f"{i + 1}. {pensamento}",
                opcoes_sabotagem,
                index=opcoes_sabotagem.index(st.session_state.respostas_pensamentos[i]) if st.session_state.respostas_pensamentos[i] else 0,
                key=f"pensamento_{i}"
            )
            st.session_state.respostas_pensamentos[i] = resposta

        enviado = st.form_submit_button("📨 Enviar respostas")

        if enviado:
            if nome and email and celular:
                try:
                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                    secret_dict = st.secrets["gcp_service_account"]
                    creds = ServiceAccountCredentials.from_json_keyfile_dict(secret_dict, scope)
                    client = gspread.authorize(creds)

                    sheet = client.open("Raio-X Comportamental - Respostas").sheet1
                    data = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), nome, email, celular] + st.session_state.respostas_comportamento + st.session_state.respostas_pensamentos
                    sheet.append_row(data)

                    st.session_state.respostas_enviadas = True
                    st.success("Respostas enviadas com sucesso! Obrigada por participar 💛")
                except Exception as e:
                    st.error(f"Erro ao salvar na planilha: {e}")
            else:
                st.warning("Por favor, preencha todos os campos antes de enviar.")
# Análise (somente após envio)
if st.session_state.respostas_enviadas:
    st.subheader("🔍 Sua Análise Comportamental")

    valores = {"Nunca": 0, "Às vezes": 1, "Frequentemente": 2, "Quase sempre": 3}
    respostas_numericas = [valores.get(r, 0) for r in st.session_state.respostas_comportamento]

    categorias = {
        "Fome Emocional": [1, 9, 14, 15, 16, 17],
        "Comer por Influência Externa": [0, 2, 4, 6, 7, 12, 20, 22],
        "Autocontrole e Valores": [3, 5, 8, 10, 11, 13]
    }

    explicacoes = {
        "Fome Emocional": """
**Fome Emocional** refere-se ao impulso de comer em resposta a emoções — como estresse, tristeza, ansiedade ou tédio — e não à fome física.

- **Pontuação baixa (0–1):** você demonstra equilíbrio ao lidar com emoções sem recorrer à comida.
- **Pontuação média (1.1–2):** indica que, às vezes, a comida é usada como válvula de escape. Isso é comum e pode ser trabalhado!
- **Pontuação alta (2.1–3):** a alimentação pode estar sendo usada com frequência para regular emoções. Isso merece atenção, mas é totalmente possível de ser transformado com dedicação e as estratégias certas.
""",
        "Comer por Influência Externa": """
**Comer por Influência Externa** acontece quando comemos mais por estímulos do ambiente do que por necessidade física — como cheiro, visão de comida, pressão social ou hábitos automáticos.

- **Pontuação baixa (0–1):** você tende a se guiar bem pelos seus sinais internos de fome e saciedade.
- **Pontuação média (1.1–2):** mostra que alguns estímulos externos influenciam sua alimentação.
- **Pontuação alta (2.1–3):** o ambiente pode estar determinando grande parte do seu comportamento alimentar. Pequenas mudanças bem direcionadas podem ter grande impacto.
""",
        "Autocontrole e Valores": """
**Autocontrole e Valores** refletem o quanto suas escolhas alimentares estão alinhadas aos seus objetivos e autorregulação.

- **Pontuação baixa (0–1):** pode haver dificuldade em aplicar escolhas conscientes.
- **Pontuação média (1.1–2):** você está no caminho, com espaço para fortalecimento do autocontrole.
- **Pontuação alta (2.1–3):** você demonstra alinhamento entre seus valores e comportamento. Muito positivo!
"""
    }

    for categoria, indices in categorias.items():
        respostas_cat = [respostas_numericas[i] for i in indices]
        media = sum(respostas_cat) / len(respostas_cat)
        st.markdown(f"### 🔸 {categoria}")
        st.markdown(f"**Sua pontuação média:** `{media:.1f}`")
        st.markdown(explicacoes[categoria])
        st.markdown("---")

    st.info("🔍 Este questionário ainda não foi validado cientificamente em estudos publicados, mas foi baseado em instrumentos previamente validados na literatura. Os resultados não têm valor diagnóstico, mas funcionam como um guia valioso para reflexões e acompanhamento nutricional.")
