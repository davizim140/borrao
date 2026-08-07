import streamlit as st
import random
from PIL import Image
import io

# ========== CONFIGURAÇÃO ==========
st.set_page_config(page_title="Hexagrama do Caos", page_icon="🔥", layout="centered")

st.title("🔥 Hexagrama do Caos")
st.markdown("**6 ideias inúteis em 1 site. Você é bem-vindo e também culpado.**")

# ========== FUNÇÕES ==========

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

def gerar_conspiracao():
    sujeitos = ["Os pombos", "A indústria de chinelos", "Os gatos", "Os influencers de café", "O Mark Zuckerberg", "O Elon Musk", "A Netflix", "O algoritmo do TikTok", "Os entregadores de iFood", "As nuvens do Google Drive"]
    verbos = ["são na verdade", "estão secretamente", "foram criados para", "fazem parte de um plano de", "estão manipulando", "controlam mentalmente", "são uma fachada para", "foram implantados por", "são agentes de", "não existem, são uma ilusão de"]
    objetos = ["controlar o mercado de bananas", "monitorar quem dorme de meia", "te vender curso de IA", "criar uma nova moeda baseada em memes", "te fazer comprar air fryer", "te obrigar a usar calça jeans", "te viciar em séries medíocres", "substituir humanos por estátuas vivas", "inventar a inveja", "te fazer acreditar que segunda-feira é um dia produtivo"]
    return f"{random.choice(sujeitos)} {random.choice(verbos)} {random.choice(objetos)}."

# ========== NOVAS FUNÇÕES ==========

def gerar_email_passivo_agressivo():
    aberturas = [
        "Prezados, espero que este e-mail encontre todos bem... ou pelo menos acordados.",
        "Bom dia. Seguindo nosso alinhamento (que na verdade foi um monólogo), gostaria de reforçar...",
        "Conforme conversamos (ou melhor, conforme eu falei e ninguém respondeu)...",
        "Vimos que o prazo passou. Mas sem problemas, a gente se acostuma.",
        "Abaixo o resumo da reunião que ninguém prestou atenção."
    ]
    corpos = [
        "Sugiro que da próxima vez leiam os e-mails antes de perguntar o que foi dito.",
        "Reforço que o anexo estava no e-mail anterior. Sim, aquele que você não abriu.",
        "Se houver dúvidas, sugiro reler o histórico (todas as 47 mensagens).",
        "Agradeço a atenção de todos, especialmente de quem vai ignorar este e-mail.",
        "Fico à disposição para esclarecer o que já estava claro no documento original."
    ]
    fechos = [
        "Atenciosamente, mas não muito.",
        "Sem mais para o momento, até o próximo e-mail que ninguém vai ler.",
        "Grato pela paciência (a minha, não a sua).",
        "Abs, e que os deuses do Outlook tenham piedade de nós.",
        "Fim. (Dessa vez, leia até o final.)"
    ]
    return f"{random.choice(aberturas)}\n\n{random.choice(corpos)}\n\n{random.choice(fechos)}"

def traduzir_sarcastico(frase):
    # Simula tradução pra emoji sarcástico baseado em palavras-chave
    palavras_chave = {
        "bem": "😀👍🔫",
        "tudo bem": "😀👍🔫",
        "feliz": "😃💥",
        "triste": "😢💀",
        "cansado": "😴⚰️",
        "puto": "😡🔥",
        "ansioso": "😰🔄",
        "ok": "👌😐",
        "amor": "❤️🤡",
        "odeio": "💀👎",
        "trabalho": "💼🔫",
        "fé": "🙏😬",
        "obrigado": "🙃👍",
        "desculpa": "😬🚩",
        "não": "🚫😤",
    }
    frase_lower = frase.lower()
    for palavra, emoji in palavras_chave.items():
        if palavra in frase_lower:
            return f"'{frase}' → {emoji}"
    # Se não achar nada, responde com um genérico
    return f"'{frase}' → 🤷‍♂️💩"

def adivinhar_filme():
    descricoes = [
        ("Um homem comum descobre que tem um destino especial e precisa salvar o mundo de uma força sombria. No final, ele descobre que o poder estava dentro dele.", "Qualquer filme do Harry Potter, Star Wars ou Senhor dos Anéis"),
        ("Uma mulher forte e independente enfrenta um sistema opressor, mas no final descobre que o verdadeiro inimigo era o patriarcado (e um ex-namorado).", "Qualquer filme da Marvel fase 4 ou um drama genérico da Netflix"),
        ("Um grupo de pessoas aleatórias se une para realizar uma missão impossível, mas no final um deles se sacrifica e todos choram.", "Velozes e Furiosos 7, Vingadores: Ultimato, ou qualquer filme de ação genérico"),
        ("Um cara acorda e descobre que está preso em um loop temporal e precisa repetir o mesmo dia até aprender uma lição.", "Feitiço do Tempo, ou qualquer comédia romântica da Netflix"),
        ("Uma criança descobre um mundo mágico escondido dentro de um armário/guarda-roupa/buraco no chão.", "As Crônicas de Nárnia, ou qualquer filme infantil genérico"),
    ]
    descricao, resposta = random.choice(descricoes)
    return descricao, resposta

# ========== INTERFACE ==========
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🚫 Desculpas",
    "📸 Avaliador Brutal",
    "🕵️ Conspirações",
    "📧 E-mail PA",
    "😤 Tradutor Sarcástico",
    "🎬 Adivinhe o Filme"
])

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

with tab4:
    st.subheader("Gerador de E-mails Passivo-Agressivos")
    if st.button("Gerar E-mail"):
        st.text_area("Seu e-mail:", gerar_email_passivo_agressivo(), height=200)

with tab5:
    st.subheader("Tradutor de Sentimentos pra Emoji (Versão Sarcástica)")
    frase = st.text_input("Digite uma frase:")
    if frase:
        st.markdown(f"**Tradução:** {traduzir_sarcastico(frase)}")

with tab6:
    st.subheader("Adivinhe o Filme Só pela Descrição Cringe")
    if "descricao_atual" not in st.session_state:
        st.session_state.descricao_atual, st.session_state.resposta_atual = adivinhar_filme()
    st.markdown(f"**Descrição:** {st.session_state.descricao_atual}")
    if st.button("Mostrar Resposta"):
        st.info(f"**Resposta:** {st.session_state.resposta_atual}")
    if st.button("Nova Descrição"):
        st.session_state.descricao_atual, st.session_state.resposta_atual = adivinhar_filme()
        st.rerun()

st.markdown("---")
st.caption("Feito com 💀 e Streamlit. Agora com 6 abas de pura perda de tempo.")
