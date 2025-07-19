
import streamlit as st

st.set_page_config(page_title="Raio-X Comportamental", layout="centered")

# Cores e estilo
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #fdf6ec;
        }
        h1, h2, h3 {
            color: #4e3d30;
        }
        .css-18ni7ap.e8zbici2 {background-color: #fff8ef;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Raio-X Comportamental")
st.markdown("##### Por **Nutricionista Giulia Mano** — CRN 12345")

st.markdown("""
Olá! Eu sou a **Giu** e esse é o seu Raio-X Comportamental.  
Ele foi criado para te ajudar a entender melhor **seus comportamentos alimentares e seus pensamentos automáticos mais frequentes**.

Não existe resposta certa ou errada.  
O mais importante é você se reconhecer com sinceridade.

---

**Se você se identificar com um pensamento semelhante (mesmo que não seja exatamente igual), marque a opção correspondente.**

💬 Se quiser falar comigo:  
📱 WhatsApp: (11) 97592-5467  
📸 Instagram: [@nutrigiuliamano](https://instagram.com/nutrigiuliamano)
""")

# Identificação
st.header("👤 Seus dados")
nome = st.text_input("Nome completo")
email = st.text_input("E-mail")
telefone = st.text_input("Celular / WhatsApp")

st.divider()

# Bloco 1: Comportamentos Alimentares
st.header("🍽️ Comportamentos Alimentares")

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
    "Faço escolhas alimentares diferentes quando estou com outras pessoas.",
]

respostas_comportamento = {}
for i, pergunta in enumerate(comportamentos):
    respostas_comportamento[f"c{i}"] = st.radio(pergunta, ["Nunca", "Às vezes", "Frequentemente", "Quase sempre"], key=f"c{i}")

st.divider()

# Bloco 2: Pensamentos Sabotadores
st.header("🧠 Pensamentos Sabotadores")

st.info("Selecione os pensamentos que você já teve ou algo **parecido**. O importante é se identificar com a ideia geral.")

pensamentos = [
    "Já pensei: 'Já que comi um pedaço, agora vou comer tudo e recomeço amanhã'.",
    "Já pensei: 'Estou tão sem tempo, não consigo seguir nada agora'.",
    "Pensei: 'Não posso desperdiçar, então vou comer mesmo sem fome'.",
    "Me senti obrigado(a) a comer porque insistiram, mesmo sem querer.",
    "Pensei: 'Já paguei por isso, preciso aproveitar'.",
    "Comi algo porque era uma ocasião especial, mesmo sem vontade.",
    "Pensei: 'Já que não estou fazendo tudo certo, não adianta tentar'.",
    "Pensei: 'Depois eu compenso isso'.",
    "Acreditei que merecia comer algo porque tive um dia ruim.",
    "Me deixei levar pela ideia de que 'é só hoje'.",
]

respostas_pensamentos = {}
for i, pensamento in enumerate(pensamentos):
    respostas_pensamentos[f"p{i}"] = st.radio(pensamento, ["Não me identifico", "Me identifico um pouco", "Me identifico muito"], key=f"p{i}")

st.divider()

if st.button("Enviar respostas"):
    st.success("Respostas enviadas com sucesso! ✨ Obrigada por se conhecer mais com a Giu.")
    st.balloons()

    st.markdown("### ✅ Resumo das suas respostas:")

    st.write("**Nome:**", nome)
    st.write("**E-mail:**", email)
    st.write("**Celular:**", telefone)

    st.markdown("#### 🍽️ Comportamentos Alimentares")
    for i, pergunta in enumerate(comportamentos):
        st.write(f"- {pergunta} → **{respostas_comportamento[f'c{i}']}**")

    st.markdown("#### 🧠 Pensamentos Sabotadores")
    for i, pensamento in enumerate(pensamentos):
        st.write(f"- {pensamento} → **{respostas_pensamentos[f'p{i}']}**")
