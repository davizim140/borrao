import streamlit as st

st.set_page_config(page_title="Loja GGmax Fake", page_icon="🕹️")

# Dados de exemplo
produtos = [
    {
        "nome": "Skin Lendária - Dragão Cósmico",
        "descricao": "Skin rara com efeitos de partículas e trilha sonora própria.",
        "preco": 29.90,
        "raridade": "Lendária"
    },
    {
        "nome": "Emote - Dança do Caos",
        "descricao": "Emote exclusivo para humilhar os adversários.",
        "preco": 9.90,
        "raridade": "Épica"
    },
    {
        "nome": "Pacote de Moedas - 1000 GrokCoins",
        "descricao": "Moedas virtuais para gastar em qualquer jogo da plataforma.",
        "preco": 19.90,
        "raridade": "Comum"
    },
    {
        "nome": "Efeito de Morte - Explosão de Memes",
        "descricao": "Toda vez que você morre, um meme aleatório aparece.",
        "preco": 14.90,
        "raridade": "Rara"
    },
]

# Estado do carrinho
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

st.title("🕹️ Loja GGmax Style")
st.write("Bem-vindo à loja de itens digitais mais duvidosa da internet. Escolha sua skin e gaste seu suado dinheirinho virtual.")

st.sidebar.header("🛒 Carrinho")

def adicionar_ao_carrinho(produto):
    st.session_state.carrinho.append(produto)

def limpar_carrinho():
    st.session_state.carrinho = []

# Listagem de produtos
st.subheader("Itens disponíveis")

for i, p in enumerate(produtos):
    with st.container():
        st.markdown(f"### {p['nome']}")
        st.markdown(f"**Raridade:** {p['raridade']}")
        st.markdown(p["descricao"])
        st.markdown(f"**Preço:** R$ {p['preco']:.2f}")
        if st.button(f"Adicionar ao carrinho ({p['nome']})", key=f"btn_{i}"):
            adicionar_ao_carrinho(p)
            st.success(f"{p['nome']} foi adicionado ao carrinho!")

        st.divider()

# Carrinho na sidebar
total = 0.0
if st.session_state.carrinho:
    for item in st.session_state.carrinho:
        st.sidebar.write(f"- {item['nome']} | R$ {item['preco']:.2f}")
        total += item["preco"]
    st.sidebar.markdown(f"---")
    st.sidebar.markdown(f"**Total:** R$ {total:.2f}")

    if st.sidebar.button("Finalizar compra"):
        st.sidebar.success("Compra finalizada! (Mentira, mas a intenção é o que conta.)")
        limpar_carrinho()
else:
    st.sidebar.write("Seu carrinho está vazio. Triste.")

# Área de destaque / promoções
st.subheader("🔥 Promoções da semana")
st.info("Compre 2 skins e ganhe um emote aleatório (quando você implementar isso de verdade).")

st.subheader("📦 Futuras features")
st.write("- Integração com pagamento via Pix")
st.write("- Sistema de login e inventário de itens")
st.write("- Loot boxes com chance de itens lendários")
