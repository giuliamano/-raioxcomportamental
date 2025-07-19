
import streamlit as st

st.set_page_config(page_title="Raio-X Comportamental", layout="centered")

st.markdown("""
# Raio-X Comportamental

Bem-vindo(a)! Este questionário foi desenvolvido pela **Nutricionista Giulia Mano (@nutrigiuliamano)** para te ajudar a entender melhor seu comportamento alimentar.

Seus dados e respostas são confidenciais. Ao final, você pode receber orientações personalizadas.

**Contato:**  
📲 WhatsApp: (11) 97592-5467  
📸 Instagram: [@nutrigiuliamano](https://instagram.com/nutrigiuliamano)

---  
## Informações iniciais
""")

name = st.text_input("Nome completo")
email = st.text_input("E-mail")
phone = st.text_input("Celular / WhatsApp")

st.markdown("## Questionário de Comportamento Alimentar")

questions = [
    "1. Quando estou entediado(a), sinto vontade de comer.",
    "2. Quando estou triste ou ansioso(a), a comida me conforta.",
    "3. Sinto que mereço comer algo porque tive um dia difícil.",
    "4. Já comi algo só porque paguei ou era uma ocasião especial.",
    "5. Como mesmo sem fome quando estou sobrecarregado(a) ou sem tempo.",
    "6. Sinto que não consigo parar de comer certos alimentos mesmo sem fome.",
    "7. Quando como fora de casa ou me oferecem algo, não consigo dizer não.",
    "8. Evito desperdiçar comida mesmo se estiver satisfeito(a).",
]

respostas = {}
for q in questions:
    respostas[q] = st.radio(q, ["Nunca", "Às vezes", "Frequentemente", "Quase sempre"])

if st.button("Enviar"):
    st.success("Respostas registradas com sucesso! Obrigada por participar 💛")
    st.balloons()
