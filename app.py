import streamlit as st
import random
from PIL import Image
import io

# ========== CONFIGURAÇÃO ==========
st.set_page_config(page_title="Trindade do Caos", page_icon="🤡", layout="centered")

st.title("🤡 Trindade do Caos")
st.markdown("**Desculpas, Conspirações e Julgamento Visual — tudo em um lugar inútil.**")

# ========== ABA 1: GERADOR DE DESCULPAS ==========
def gerar_desculpa():
    desculpas = [
        "Meu gato comeu o cabo do roteador e agora ele é o gerente de TI da casa.",
        "O Wi-Fi ficou com vergonha de mim e desistiu.",
        "Meu e-mail foi sequestrado por um golpe do nigeriano que prometia R$ 50 milhões.",
        "O sistema pediu pra eu reiniciar e eu obedeci como um bom cidadão.",
        "Um parente distante que eu nem conheço morreu e eu tive que fazer o funeral virtual.",
        "O Excel bugou e transformou minha planilha em um desenho do Bob Esponja.",
        "Eu estava numa reunião importante, mas era tão importante que esqueci qual era.",
        "Meu cachorro comeu meu fone e agora só ouço os pensamentos dele.",
        "O algoritmo do Google me mandou pro YouTube e eu me perdi num vídeo de 3 horas sobre formigas.",
        "O sistema estava em manutenção, mas a manutenção era um funcionário dormindo no servidor."
    ]
    return random.choice(desculpas)

# ========== ABA 2: AVALIADOR DE FOTOS ==========
def avaliar_foto_brutal():
    comentarios = [
        "Você parece alguém que pede desconto em curso de Excel.",
        "Essa foto tem energia de perfil do Tinder que começa com 'sou low profile'.",
        "Você parece que acabou de ver o saldo da conta no fim do mês.",
        "Essa expressão é tipo 'descobri que amanhã tem reunião de alinhamento'.",
        "Seu rosto diz 'confio em processos seletivos que pedem 5 etapas'.",
        "Você parece que acha que 'brainstorm' é uma doença.",
        "Essa foto vai ser usada em algum dia para te cancelarem no Twitter.",
        "Você parece que responde e-mail com 'ok, vou ver isso' e nunca vê.",
        "Essa cara é de quem já viu o código legado de um sistema bancário.",
        "Você parece que come pizza de pizza hut com garfo e faca."
    ]
    return random.choice(comentarios)

# ========== ABA 3: GERADOR DE CONSPIRAÇÕES ==========
def gerar_conspiracao():
    sujeitos = ["Os pombos", "A indústria de chinelos", "Os gatos", "Os influencers de café", "O Mark Zuckerberg", "O Elon Musk", "A Netflix", "O algoritmo do TikTok", "Os entregadores de iFood", "As nuvens do Google Drive"]
    verbos = ["são na verdade", "estão secretamente", "foram criados para", "fazem parte de um plano de", "estão manipulando", "controlam mentalmente", "são uma fachada para", "foram implantados por", "são agentes de", "não existem, são uma ilusão de"]
    objetos = ["controlar o mercado de bananas", "monitorar quem dorme de meia", "te vender curso de IA", "criar uma nova moeda baseada em memes", "te fazer comprar air fryer", "te obrigar a usar calça jeans", "te viciar em séries medíocres", "substituir humanos por estátuas vivas", "inventar a inveja", "te fazer acreditar que segunda-feira é um dia produtivo"]
    return f"{random.choice(sujeitos)} {random.choice(verbos)} {random.choice(objetos)}."

# ========== INTERFACE ==========
tab1, tab2, tab3 = st.tabs(["🚫 Desculpas", "📸 Avaliador Brutal", "🕵️ Conspirações"])

with tab1:
    st.subheader("Gerador de Desculpas Profissionais")
    if st.button("Gerar Desculpa"):
        st.success(gerar_desculpa())

with tab2:
    st.subheader("Avaliador de Fotos com Sinceridade Brutal")
    foto = st.file_uploader("Envie sua foto (qualquer formato)", type=["png", "jpg", "jpeg", "gif"])
    if foto:
        image = Image.open(foto)
        st.image(image, caption="Sua foto", width=250)
        if st.button("Avaliar"):
            st.error(avaliar_foto_brutal())

with tab3:
    st.subheader("Gerador de Conspirações Aleatórias")
    if st.button("Gerar Conspiração"):
        st.info(gerar_conspiracao())

st.markdown("---")
st.caption("Feito com 💀 e Streamlit. Nada disso é sério, nem mesmo sua foto.")
