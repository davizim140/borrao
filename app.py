import streamlit as st
import random

st.set_page_config(page_title="Loja GGmax Premium", page_icon="🕹️")

# ========== SESSÃO DO USUÁRIO ==========
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.session_state.inventario = []
    st.session_state.saldo = 100.0  # saldo fictício pra testar

if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# ========== PRODUTOS ==========
produtos = [
    {"nome": "Skin Lendária - Dragão Cósmico", "descricao": "Skin rara com partículas e trilha sonora.", "preco": 29.90, "raridade": "Lendária"},
    {"nome": "Emote - Dança do Caos", "descricao": "Humilhe seus oponentes.", "preco": 9.90, "raridade": "Épica"},
    {"nome": "1000 GrokCoins", "descricao": "Moeda virtual da plataforma.", "preco": 19.90, "raridade": "Comum"},
    {"nome": "Efeito de Morte - Explosão de Memes", "descricao": "Meme aleatório ao morrer.", "preco": 14.90, "raridade": "Rara"},
]

# ========== LOOT BOX ==========
def abrir_loot_box():
    raridades = ["Comum", "Comum", "Comum", "Rara", "Rara", "Épica", "Lendária"]
    sorteio = random.choice(raridades)
    st.session_state.inventario.append(f"Item aleatório ({sorteio}) - da Loot Box")
    return sorteio

# ========== LOGIN ==========
if not st.session_state.logado:
    st.title("🔐 Login - Loja GGmax")
    usuario = st.text_input("Usuário (qualquer um serve)")
    senha = st.text_input("Senha (qualquer uma serve)", type="password")
    if st.button("Entrar"):
        if usuario and senha:
            st.session_state.logado = True
            st.session_state.usuario = usuario
            st.success("Login efetuado (fake) com sucesso!")
            st.rerun()
        else:
            st.error("Preencha os campos, seu lerdo.")
    st.stop()

# ========== LOJA ==========
st.sidebar.write(f"👤 **{st.session_state.usuario}**")
st.sidebar.write(f"💰 Saldo: R$ {st.session_state.saldo:.2f}")
st.sidebar.header("🛒 Carrinho")

total = 0.0
if st.session_state.carrinho:
    for item in st.session_state.carrinho:
        st.sidebar.write(f"- {item['nome']} | R$ {item['preco']:.2f}")
        total += item["preco"]
    st.sidebar.markdown(f"**Total:** R$ {total:.2f}")
    if st.sidebar.button("Finalizar compra"):
        if st.session_state.saldo >= total:
            st.session_state.saldo -= total
            for item in st.session_state.carrinho:
                st.session_state.inventario.append(item["nome"])
            st.session_state.carrinho = []
            st.sidebar.success("Compra realizada! Itens no inventário.")
        else:
            st.sidebar.error("Saldo insuficiente, pobre.")
else:
    st.sidebar.write("Carrinho vazio.")

st.title("🕹️ Loja GGmax Premium")
st.write("Agora com login fake e loot box pra te dar esperança falsa.")

# Produtos
st.subheader("Itens disponíveis")
for i, p in enumerate(produtos):
    with st.container():
        st.markdown(f"### {p['nome']}")
        st.markdown(f"**Raridade:** {p['raridade']}  |  **Preço:** R$ {p['preco']:.2f}")
        st.markdown(p["descricao"])
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Adicionar ao carrinho", key=f"add_{i}"):
                st.session_state.carrinho.append(p)
                st.success(f"{p['nome']} adicionado!")
        with col2:
            if st.button(f"Comprar direto", key=f"buy_{i}"):
                if st.session_state.saldo >= p["preco"]:
                    st.session_state.saldo -= p["preco"]
                    st.session_state.inventario.append(p["nome"])
                    st.success(f"{p['nome']} comprado direto!")
                else:
                    st.error("Sem grana, irmão.")
        st.divider()

# Loot Box
st.subheader("🎁 Loot Box Misteriosa")
st.write("Pague R$ 5,00 e leve um item aleatório (pode ser até lendário! ou não).")
if st.button("Abrir Loot Box (R$ 5,00)"):
    if st.session_state.saldo >= 5.0:
        st.session_state.saldo -= 5.0
        raridade = abrir_loot_box()
        st.success(f"Você ganhou: {raridade}")
    else:
        st.error("Sem grana pra loot box, mendigo digital.")

# Inventário
st.subheader("📦 Seu Inventário")
if st.session_state.inventario:
    for item in st.session_state.inventario:
        st.write(f"- {item}")
else:
    st.write("Nada aqui. Tristeza.")

# Logout
if st.button("Sair da conta"):
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.session_state.inventario = []
    st.session_state.saldo = 100.0
    st.session_state.carrinho = []
    st.rerun()
