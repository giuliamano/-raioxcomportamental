
import streamlit as st
import datetime

st.set_page_config(page_title="Raio-X Comportamental", layout="centered")

# Estilo personalizado
st.markdown(
    """
    <style>
        body {
            background-color: #fdf6ec;
        }
        .stApp {
            background-color: #fdf6ec;
        }
        h1, h2, h3 {
            color: #5e4b3c;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Raio-X Comportamental")
st.subheader("Por Giulia Mano • Nutricionista • CRN 12345")

st.markdown(
    """
    Este questionário foi desenvolvido para te ajudar a entender seus comportamentos e pensamentos em relação à comida.

    Nenhuma resposta está certa ou errada — seja sincero(a) com você mesmo(a).

    **Se você se identificar com um pensamento ou comportamento semelhante ao descrito, marque-o.**

    **Contato direto com a Giu:**  
    📸 Instagram: [@nutrigiuliamano](https://instagram.com/nutrigiuliamano)  
    💬 WhatsApp: (11) 97592-5467
    """
)

# Identificação
st.markdown("### 👤 Identificação")
nome = st.text_input("Nome completo")
email = st.text_input("E-mail")
celular = st.text_input("Celular / WhatsApp")

st.markdown("---")

# Bloco 1 - Comportamentos alimentares (DEBQ + R21 adaptado)
st.markdown("## 🍽️ Seus Comportamentos com a Comida")
comportamento_perguntas = [
    "1. Quando estou entediado(a), sinto vontade de comer.",
    "2. Quando estou triste ou ansioso(a), a comida me conforta.",
    "3. Sinto que mereço comer algo porque tive um dia difícil.",
    "4. Como mesmo sem fome quando estou sobrecarregado(a) ou sem tempo.",
    "5. Evito desperdiçar comida mesmo se estiver satisfeito(a).",
    "6. Sinto que não consigo parar de comer certos alimentos mesmo sem fome.",
    "7. Quando como fora de casa ou me oferecem algo, não consigo dizer não.",
    "8. Já comi algo só porque paguei ou era uma ocasião especial.",
]

comportamento_respostas = {}
for pergunta in comportamento_perguntas:
    comportamento_respostas[pergunta] = st.radio(pergunta, ["Nunca", "Às vezes", "Frequentemente", "Quase sempre"], key=pergunta)

st.markdown("---")

# Introdução aos pensamentos sabotadores
st.markdown("## 🧠 Pensamentos Sabotadores")
st.info("Selecione os pensamentos que você já teve ou algo parecido. Mesmo que não seja exatamente igual, escolha se você se identifica com a ideia geral.")

pensamento_perguntas = [
    "9. Já pensei: 'Já que comi um pedaço, agora vou comer tudo e recomeço amanhã'.",
    "10. Pensei: 'Não posso desperdiçar, então vou comer mesmo sem fome'.",
    "11. Já me senti obrigado(a) a comer porque insistiram, mesmo sem querer.",
    "12. Pensei: 'Já paguei por isso, preciso aproveitar'.",
    "13. Comi porque era uma ocasião especial, mesmo sem vontade.",
    "14. Evitei seguir o plano alimentar por estar sobrecarregado(a) ou sem tempo.",
    "15. Pensei: 'Já que não estou fazendo tudo certo, não adianta tentar'.",
]

pensamento_respostas = {}
for pergunta in pensamento_perguntas:
    pensamento_respostas[pergunta] = st.radio(pergunta, ["Não me identifico", "Me identifico um pouco", "Me identifico muito"], key=pergunta)

# Botão de envio
st.markdown("---")
if st.button("Enviar respostas"):
    st.success("Respostas enviadas com sucesso! Obrigada por compartilhar ✨")
    st.balloons()
    # Aqui pode ser adicionada integração com planilha no futuro

    # Visualização de resumo
    st.markdown("### ✅ Resumo das respostas:")
    st.write("**Nome:**", nome)
    st.write("**E-mail:**", email)
    st.write("**Celular:**", celular)

    st.markdown("**🍽️ Comportamentos Alimentares**")
    for k, v in comportamento_respostas.items():
        st.write(k, "→", v)

    st.markdown("**🧠 Pensamentos Sabotadores**")
    for k, v in pensamento_respostas.items():
        st.write(k, "→", v)
