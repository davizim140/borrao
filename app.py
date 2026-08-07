import streamlit as st
import random

# -----------------------------
# Dados iniciais (mock)
# -----------------------------
LIGAS = ["Série A", "Série B", "Série C", "Série D"]
ESTADUAIS = ["Paulista", "Carioca", "Mineiro", "Gaúcho"]

TIMES_BASE = [
    {"nome": "Flamengo", "liga": "Série A", "estado": "Carioca"},
    {"nome": "Palmeiras", "liga": "Série A", "estado": "Paulista"},
    {"nome": "Corinthians", "liga": "Série A", "estado": "Paulista"},
    {"nome": "Vasco", "liga": "Série B", "estado": "Carioca"},
    {"nome": "Cruzeiro", "liga": "Série B", "estado": "Mineiro"},
    {"nome": "Grêmio", "liga": "Série A", "estado": "Gaúcho"},
]

JOGADORES_BASE = [
    {"nome": "Jogador 1", "pos": "ATA", "overall": 78, "salario": 300_000},
    {"nome": "Jogador 2", "pos": "MEI", "overall": 75, "salario": 250_000},
    {"nome": "Jogador 3", "pos": "ZAG", "overall": 72, "salario": 200_000},
    {"nome": "Jogador 4", "pos": "LAT", "overall": 70, "salario": 180_000},
    {"nome": "Jogador 5", "pos": "GOL", "overall": 74, "salario": 220_000},
]

# -----------------------------
# Estado da aplicação
# -----------------------------
if "clube" not in st.session_state:
    st.session_state.clube = None

if "financas" not in st.session_state:
    st.session_state.financas = {
        "caixa": 50_000_000,
        "receita_tv": 5_000_000,
        "receita_bilheteria": 1_000_000,
        "patrocinios": 3_000_000,
        "despesa_salarios": 0,
        "despesa_outros": 1_000_000,
    }

if "elenco" not in st.session_state:
    st.session_state.elenco = []

if "historico_partidas" not in st.session_state:
    st.session_state.historico_partidas = []

# -----------------------------
# Funções de lógica
# -----------------------------
def inicializar_clube(nome_clube):
    clube = next((t for t in TIMES_BASE if t["nome"] == nome_clube), None)
    if not clube:
        return

    st.session_state.clube = clube
    # Clona jogadores base pro elenco
    elenco = []
    for j in JOGADORES_BASE:
        jogador = j.copy()
        jogador["clube"] = clube["nome"]
        elenco.append(jogador)
    st.session_state.elenco = elenco

    # Calcula despesa de salários
    total_salarios = sum(j["salario"] for j in elenco)
    st.session_state.financas["despesa_salarios"] = total_salarios


def simular_partida(adversario_nome: str):
    if not st.session_state.clube:
        st.warning("Escolha um clube primeiro.")
        return

    clube = st.session_state.clube["nome"]
    overall_clube = sum(j["overall"] for j in st.session_state.elenco) / len(st.session_state.elenco)
    overall_adv = random.randint(65, 80)

    fator_random = random.uniform(-5, 5)
    score_clube = max(0, int((overall_clube + fator_random) // 10))
    score_adv = max(0, int((overall_adv - fator_random) // 10))

    resultado = "Empate"
    if score_clube > score_adv:
        resultado = "Vitória"
        st.session_state.financas["caixa"] += 500_000
        st.session_state.financas["receita_bilheteria"] += 200_000
    elif score_clube < score_adv:
        resultado = "Derrota"
        st.session_state.financas["caixa"] -= 200_000

    partida = {
        "mandante": clube,
        "visitante": adversario_nome,
        "gols_mandante": score_clube,
        "gols_visitante": score_adv,
        "resultado": resultado,
    }
    st.session_state.historico_partidas.append(partida)


def resumo_financeiro_mensal():
    f = st.session_state.financas
    receita_total = f["receita_tv"] + f["receita_bilheteria"] + f["patrocinios"]
    despesa_total = f["despesa_salarios"] + f["despesa_outros"]
    saldo = receita_total - despesa_total
    return receita_total, despesa_total, saldo


# -----------------------------
# Layout principal
# -----------------------------
st.set_page_config(page_title="Manager BR", layout="wide")

st.title("⚽ Manager BR - Protótipo")
st.caption("Estilo Brassfoot/Footsim, com economia avançada em construção.")

# Seleção de clube
st.sidebar.header("Configuração inicial")
clube_escolhido = st.sidebar.selectbox(
    "Escolha seu clube:",
    [t["nome"] for t in TIMES_BASE],
)

if st.sidebar.button("Iniciar com esse clube"):
    inicializar_clube(clube_escolhido)
    st.sidebar.success(f"Clube {clube_escolhido} carregado!")

# Tabs principais
tab_dashboard, tab_elenco, tab_financas, tab_partidas = st.tabs(
    ["📊 Dashboard", "👥 Elenco", "💰 Finanças", "🏟️ Partidas"]
)

# -----------------------------
# Dashboard
# -----------------------------
with tab_dashboard:
    st.subheader("Visão geral do clube")

    if not st.session_state.clube:
        st.info("Escolha um clube na barra lateral para começar.")
    else:
        clube = st.session_state.clube
        st.markdown(f"### {clube['nome']}")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Liga", clube["liga"])
            st.metric("Estado", clube["estado"])

        receita_total, despesa_total, saldo = resumo_financeiro_mensal()
        with col2:
            st.metric("Receita mensal", f"R$ {receita_total:,.0f}")
            st.metric("Despesas mensais", f"R$ {despesa_total:,.0f}")

        with col3:
            st.metric("Saldo projetado", f"R$ {saldo:,.0f}")
            st.metric("Caixa atual", f"R$ {st.session_state.financas['caixa']:,.0f}")

        st.markdown("#### Últimas partidas")
        if st.session_state.historico_partidas:
            st.table(st.session_state.historico_partidas[-5:])
        else:
            st.write("Nenhuma partida simulada ainda.")

# -----------------------------
# Elenco
# -----------------------------
with tab_elenco:
    st.subheader("Elenco do clube")

    if not st.session_state.elenco:
        st.info("Elenco ainda não carregado. Inicie um clube na barra lateral.")
    else:
        st.table(st.session_state.elenco)

# -----------------------------
# Finanças
# -----------------------------
with tab_financas:
    st.subheader("Gestão financeira")

    f = st.session_state.financas

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Receitas")
        st.write(f"TV: R$ {f['receita_tv']:,.0f}")
        st.write(f"Bilheteria: R$ {f['receita_bilheteria']:,.0f}")
        st.write(f"Patrocínios: R$ {f['patrocinios']:,.0f}")

    with col2:
        st.markdown("### Despesas")
        st.write(f"Salários: R$ {f['despesa_salarios']:,.0f}")
        st.write(f"Outros: R$ {f['despesa_outros']:,.0f}")

    receita_total, despesa_total, saldo = resumo_financeiro_mensal()
    st.markdown("---")
    st.metric("Saldo mensal projetado", f"R$ {saldo:,.0f}")

    st.markdown("### Ajustes rápidos")
    novo_patrocinio = st.slider("Ajustar patrocínios (R$)", 1_000_000, 10_000_000, int(f["patrocinios"]))
    if st.button("Aplicar novo patrocínio"):
        st.session_state.financas["patrocinios"] = novo_patrocinio
        st.success("Patrocínio atualizado.")

# -----------------------------
# Partidas
# -----------------------------
with tab_partidas:
    st.subheader("Simulação de partidas")

    if not st.session_state.clube:
        st.info("Escolha um clube primeiro.")
    else:
        adversarios = [t["nome"] for t in TIMES_BASE if t["nome"] != st.session_state.clube["nome"]]
        adversario = st.selectbox("Escolha o adversário:", adversarios)

        if st.button("Simular partida"):
            simular_partida(adversario)
            st.success("Partida simulada! Veja o resultado no histórico abaixo.")

        if st.session_state.historico_partidas:
            st.markdown("### Histórico de partidas")
            st.table(st.session_state.historico_partidas)
        else:
            st.write("Nenhuma partida simulada ainda.")
