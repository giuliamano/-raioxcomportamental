import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from config.estilo import aplicar_estilo

st.set_page_config(page_title="Raio-X Comportamental", layout="centered")
aplicar_estilo()

# Cabeçalho do app
st.markdown("<h1 style='text-align: center;'>🧠 Raio-X Comportamental</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Entenda seus padrões alimentares e comportamentais</p>", unsafe_allow_html=True)
st.markdown("---")

# Coleta de dados iniciais
with st.form(key="formulario_inicial"):
    nome = st.text_input("Nome completo")
    email = st.text_input("E-mail")
    celular = st.text_input("Celular (com DDD)")
    iniciar = st.form_submit_button("📋 Iniciar Questionário")

if "pagina" not in st.session_state:
    st.session_state.pagina = 0

# Perguntas principais (23)
perguntas_comportamento = [
    "Sinto vontade de comer quando estou ansiosa(o), triste ou entediada(o)",
    "Como para me acalmar ou me sentir melhor emocionalmente",
    "Como mesmo sem fome, só pelo prazer de comer",
    "Sinto vontade de comer depois de brigas, frustrações ou decepções",
    "Associo comida a recompensa (como quando mereço algo)",
    "Como mais quando estou sozinha(o) ou escondida(o)",
    "Sinto que perco o controle quando começo a comer certos alimentos",
    "Sinto culpa ou vergonha após comer em excesso",
    "Tenho dificuldade de parar de comer mesmo estando satisfeita(o)",
    "Como mais quando estou em festas ou eventos sociais",
    "Como mais quando vejo outras pessoas comendo",
    "Tenho dificuldade de resistir a promoções ou propagandas de comida",
    "Sinto vontade de comer ao passar por lugares com cheiro ou visão de comida",
    "Sinto que como automaticamente ao ver comida por perto",
    "Penso frequentemente em comida mesmo sem fome",
    "Planejo minha alimentação com antecedência",
    "Costumo respeitar meus sinais de fome e saciedade",
    "Sinto que tenho controle sobre minhas escolhas alimentares",
    "Consigo lidar bem com vontades sem precisar comer",
    "Meus valores pessoais influenciam minhas escolhas alimentares",
    "Consigo manter uma alimentação equilibrada mesmo sob estresse",
    "Consigo dizer 'não' à comida quando não estou com fome",
    "Tenho orgulho das minhas atitudes em relação à alimentação"
]

# Pensamentos sabotadores (10)
pensamentos = [
    "Já que comi algo 'errado', agora vou exagerar de vez",
    "Hoje é uma exceção, começo de verdade amanhã",
    "Não posso desperdiçar comida, então tenho que comer tudo",
    "É falta de educação recusar comida que me oferecem",
    "Estou muito estressada(o), mereço esse prazer agora",
    "Comi em maior quantidade só porque era uma ocasião especial ou algo que não como frequentemente.",
    "Se eu não comer agora, posso me arrepender depois",
    "Só mais um pedacinho não vai fazer diferença",
    "Se eu comer escondido, é como se não contasse",
    "Não adianta tentar, eu sempre fracasso mesmo"
]

# Divisão em páginas
respostas_comportamento = []
respostas_pensamentos = []

if iniciar or st.session_state.pagina > 0:
    blocos = [perguntas_comportamento[i:i+5] for i in range(0, len(perguntas_comportamento), 5)]
    if st.session_state.pagina < len(blocos):
        st.markdown(f"### Parte {st.session_state.pagina + 1}")
        with st.form(key=f"pagina_{st.session_state.pagina}"):
            for pergunta in blocos[st.session_state.pagina]:
                resposta = st.radio(pergunta, ["Nunca", "Raramente", "Às vezes", "Frequentemente", "Quase sempre"], key=pergunta)
                respostas_comportamento.append(resposta)
            if st.form_submit_button("Próxima página"):
                st.session_state.pagina += 1
    elif st.session_state.pagina == len(blocos):
        st.markdown("### Pensamentos Sabotadores")
        st.markdown("Com que frequência você se identifica com os pensamentos abaixo?")
        with st.form(key="pensamentos_form"):
            for pensamento in pensamentos:
                resposta = st.radio(pensamento, ["Nunca", "Raramente", "Às vezes", "Frequentemente", "Quase sempre"], key=pensamento)
                respostas_pensamentos.append(resposta)
            if st.form_submit_button("Finalizar questionário"):
                st.session_state.pagina += 1

# Conversão de respostas em pontuação
mapa_pontuacao = {"Nunca": 1, "Raramente": 2, "Às vezes": 3, "Frequentemente": 4, "Quase sempre": 5}

def calcular_media(respostas):
    return round(sum([mapa_pontuacao[r] for r in respostas]) / len(respostas), 2)

# Análise final
if st.session_state.pagina > len(blocos):
    st.success("Questionário concluído! Veja abaixo sua análise comportamental:")

    categorias = {
        "Fome Emocional": perguntas_comportamento[:8],
        "Comer por Influência Externa": perguntas_comportamento[8:14],
        "Autocontrole e Valores": perguntas_comportamento[14:]
    }

    for categoria, perguntas in categorias.items():
        respostas_cat = [st.session_state.get(pergunta) for pergunta in perguntas]
        media = calcular_media(respostas_cat)
        st.markdown(f"#### {categoria}: {media}")

        if categoria == "Fome Emocional":
            if media >= 4:
                st.write("Alerta de fome emocional intensa. Busque estratégias de regulação emocional que não envolvam comida.")
            elif media >= 2.5:
                st.write("Você apresenta sinais de fome emocional em algumas situações. Fique atenta(o) aos gatilhos.")
            else:
                st.write("Você demonstra bom controle sobre sua alimentação emocional.")
        elif categoria == "Comer por Influência Externa":
            if media >= 4:
                st.write("Você se deixa levar bastante por estímulos externos. Isso pode afetar suas escolhas.")
            elif media >= 2.5:
                st.write("Há influência externa moderada sobre sua alimentação. Trabalhe seu foco interno.")
            else:
                st.write("Você demonstra autonomia diante de influências externas.")
        elif categoria == "Autocontrole e Valores":
            if media >= 4:
                st.write("Você demonstra excelente autocontrole e alinhamento com seus valores pessoais.")
            elif media >= 2.5:
                st.write("Seu autocontrole está em desenvolvimento. Há espaço para fortalecimento.")
            else:
                st.write("Você pode estar enfrentando dificuldades com controle e consistência. Que tal buscar apoio?")
    
    st.info("⚠️ Este questionário não possui validação científica formal, mas foi baseado em instrumentos reconhecidos. Use como ferramenta de autoconhecimento.")

    # Envio para planilha
    if st.button("📨 Enviar respostas"):
        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            secret_dict = st.secrets["gcp_service_account"]
            creds = ServiceAccountCredentials.from_json_keyfile_dict(secret_dict, scope)
            client = gspread.authorize(creds)
            sheet = client.open("Raio-X Comportamental - Respostas").sheet1

            dados = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), nome, email, celular]
            dados += [st.session_state.get(p) for p in perguntas_comportamento]
            dados += [st.session_state.get(p) for p in pensamentos]

            sheet.append_row(dados)
            st.success("Respostas enviadas com sucesso! Obrigada por participar 💛")
        except Exception as e:
            st.error(f"Erro ao salvar na planilha: {e}")
