import streamlit as st
import random
import time
from collections import defaultdict

# ============================================================
# DADOS DOS TIMES (completos, todas as séries e estaduais)
# ============================================================

teams_serie_a = [
    {"id": 1, "nome": "Flamengo", "sigla": "FLA", "ataque": 88, "defesa": 82, "meio": 85, "serie": "A", "estado": "RJ"},
    {"id": 2, "nome": "Palmeiras", "sigla": "PAL", "ataque": 86, "defesa": 84, "meio": 83, "serie": "A", "estado": "SP"},
    {"id": 3, "nome": "Santos", "sigla": "SAN", "ataque": 78, "defesa": 74, "meio": 76, "serie": "A", "estado": "SP"},
    {"id": 4, "nome": "São Paulo", "sigla": "SAO", "ataque": 80, "defesa": 78, "meio": 79, "serie": "A", "estado": "SP"},
    {"id": 5, "nome": "Corinthians", "sigla": "COR", "ataque": 79, "defesa": 77, "meio": 78, "serie": "A", "estado": "SP"},
    {"id": 6, "nome": "Grêmio", "sigla": "GRE", "ataque": 77, "defesa": 75, "meio": 76, "serie": "A", "estado": "RS"},
    {"id": 7, "nome": "Internacional", "sigla": "INT", "ataque": 78, "defesa": 76, "meio": 77, "serie": "A", "estado": "RS"},
    {"id": 8, "nome": "Cruzeiro", "sigla": "CRU", "ataque": 76, "defesa": 74, "meio": 75, "serie": "A", "estado": "MG"},
    {"id": 9, "nome": "Atlético-MG", "sigla": "CAM", "ataque": 81, "defesa": 79, "meio": 80, "serie": "A", "estado": "MG"},
    {"id": 10, "nome": "Botafogo", "sigla": "BOT", "ataque": 75, "defesa": 73, "meio": 74, "serie": "A", "estado": "RJ"},
    {"id": 11, "nome": "Fluminense", "sigla": "FLU", "ataque": 76, "defesa": 74, "meio": 75, "serie": "A", "estado": "RJ"},
    {"id": 12, "nome": "Vasco", "sigla": "VAS", "ataque": 72, "defesa": 70, "meio": 71, "serie": "A", "estado": "RJ"},
    {"id": 13, "nome": "Bahia", "sigla": "BAH", "ataque": 73, "defesa": 71, "meio": 72, "serie": "A", "estado": "BA"},
    {"id": 14, "nome": "Athletico-PR", "sigla": "CAP", "ataque": 77, "defesa": 75, "meio": 76, "serie": "A", "estado": "PR"},
    {"id": 15, "nome": "Fortaleza", "sigla": "FOR", "ataque": 74, "defesa": 72, "meio": 73, "serie": "A", "estado": "CE"},
    {"id": 16, "nome": "Ceará", "sigla": "CEA", "ataque": 71, "defesa": 69, "meio": 70, "serie": "A", "estado": "CE"},
    {"id": 17, "nome": "Goiás", "sigla": "GOI", "ataque": 69, "defesa": 67, "meio": 68, "serie": "A", "estado": "GO"},
    {"id": 18, "nome": "Cuiabá", "sigla": "CUI", "ataque": 68, "defesa": 66, "meio": 67, "serie": "A", "estado": "MT"},
    {"id": 19, "nome": "Juventude", "sigla": "JUV", "ataque": 67, "defesa": 65, "meio": 66, "serie": "A", "estado": "RS"},
    {"id": 20, "nome": "Vitória", "sigla": "VIT", "ataque": 70, "defesa": 68, "meio": 69, "serie": "A", "estado": "BA"},
]

teams_serie_b = [
    {"id": 21, "nome": "Sport", "sigla": "SPO", "ataque": 72, "defesa": 70, "meio": 71, "serie": "B", "estado": "PE"},
    {"id": 22, "nome": "Náutico", "sigla": "NAU", "ataque": 68, "defesa": 66, "meio": 67, "serie": "B", "estado": "PE"},
    {"id": 23, "nome": "Santa Cruz", "sigla": "STA", "ataque": 66, "defesa": 64, "meio": 65, "serie": "B", "estado": "PE"},
    {"id": 24, "nome": "América-MG", "sigla": "AME", "ataque": 70, "defesa": 68, "meio": 69, "serie": "B", "estado": "MG"},
    {"id": 25, "nome": "Avaí", "sigla": "AVA", "ataque": 67, "defesa": 65, "meio": 66, "serie": "B", "estado": "SC"},
    {"id": 26, "nome": "Chapecoense", "sigla": "CHA", "ataque": 65, "defesa": 63, "meio": 64, "serie": "B", "estado": "SC"},
    {"id": 27, "nome": "Brusque", "sigla": "BRU", "ataque": 63, "defesa": 61, "meio": 62, "serie": "B", "estado": "SC"},
    {"id": 28, "nome": "Criciúma", "sigla": "CRI", "ataque": 69, "defesa": 67, "meio": 68, "serie": "B", "estado": "SC"},
    {"id": 29, "nome": "Ponte Preta", "sigla": "PON", "ataque": 66, "defesa": 64, "meio": 65, "serie": "B", "estado": "SP"},
    {"id": 30, "nome": "Guarani", "sigla": "GUA", "ataque": 64, "defesa": 62, "meio": 63, "serie": "B", "estado": "SP"},
    {"id": 31, "nome": "Mirassol", "sigla": "MIR", "ataque": 65, "defesa": 63, "meio": 64, "serie": "B", "estado": "SP"},
    {"id": 32, "nome": "Novorizontino", "sigla": "NOV", "ataque": 64, "defesa": 62, "meio": 63, "serie": "B", "estado": "SP"},
    {"id": 33, "nome": "Ituano", "sigla": "ITU", "ataque": 63, "defesa": 61, "meio": 62, "serie": "B", "estado": "SP"},
    {"id": 34, "nome": "Sampaio Corrêa", "sigla": "SAM", "ataque": 62, "defesa": 60, "meio": 61, "serie": "B", "estado": "MA"},
    {"id": 35, "nome": "Londrina", "sigla": "LON", "ataque": 61, "defesa": 59, "meio": 60, "serie": "B", "estado": "PR"},
    {"id": 36, "nome": "Operário-PR", "sigla": "OPE", "ataque": 62, "defesa": 60, "meio": 61, "serie": "B", "estado": "PR"},
    {"id": 37, "nome": "Tombense", "sigla": "TOM", "ataque": 60, "defesa": 58, "meio": 59, "serie": "B", "estado": "MG"},
    {"id": 38, "nome": "CRB", "sigla": "CRB", "ataque": 61, "defesa": 59, "meio": 60, "serie": "B", "estado": "AL"},
    {"id": 39, "nome": "CSA", "sigla": "CSA", "ataque": 60, "defesa": 58, "meio": 59, "serie": "B", "estado": "AL"},
    {"id": 40, "nome": "Botafogo-PB", "sigla": "BOT", "ataque": 59, "defesa": 57, "meio": 58, "serie": "B", "estado": "PB"},
]

teams_serie_c = [
    {"id": 41, "nome": "Remo", "sigla": "REM", "ataque": 65, "defesa": 63, "meio": 64, "serie": "C", "estado": "PA"},
    {"id": 42, "nome": "Paysandu", "sigla": "PAY", "ataque": 64, "defesa": 62, "meio": 63, "serie": "C", "estado": "PA"},
    {"id": 43, "nome": "Volta Redonda", "sigla": "VOL", "ataque": 63, "defesa": 61, "meio": 62, "serie": "C", "estado": "RJ"},
    {"id": 44, "nome": "Figueirense", "sigla": "FIG", "ataque": 62, "defesa": 60, "meio": 61, "serie": "C", "estado": "SC"},
    {"id": 45, "nome": "ABC", "sigla": "ABC", "ataque": 61, "defesa": 59, "meio": 60, "serie": "C", "estado": "RN"},
    {"id": 46, "nome": "América-RN", "sigla": "AME", "ataque": 60, "defesa": 58, "meio": 59, "serie": "C", "estado": "RN"},
    {"id": 47, "nome": "Confiança", "sigla": "CON", "ataque": 59, "defesa": 57, "meio": 58, "serie": "C", "estado": "SE"},
    {"id": 48, "nome": "Brasil de Pelotas", "sigla": "BRA", "ataque": 58, "defesa": 56, "meio": 57, "serie": "C", "estado": "RS"},
    {"id": 49, "nome": "Ypiranga-RS", "sigla": "YPI", "ataque": 58, "defesa": 56, "meio": 57, "serie": "C", "estado": "RS"},
    {"id": 50, "nome": "São José-RS", "sigla": "SJO", "ataque": 57, "defesa": 55, "meio": 56, "serie": "C", "estado": "RS"},
    {"id": 51, "nome": "Aparecidense", "sigla": "APA", "ataque": 56, "defesa": 54, "meio": 55, "serie": "C", "estado": "GO"},
    {"id": 52, "nome": "Atlético-CE", "sigla": "ACE", "ataque": 55, "defesa": 53, "meio": 54, "serie": "C", "estado": "CE"},
    {"id": 53, "nome": "Ferroviário", "sigla": "FER", "ataque": 56, "defesa": 54, "meio": 55, "serie": "C", "estado": "CE"},
    {"id": 54, "nome": "Floresta", "sigla": "FLO", "ataque": 55, "defesa": 53, "meio": 54, "serie": "C", "estado": "CE"},
    {"id": 55, "nome": "Manaus", "sigla": "MAN", "ataque": 54, "defesa": 52, "meio": 53, "serie": "C", "estado": "AM"},
    {"id": 56, "nome": "Nacional-AM", "sigla": "NAC", "ataque": 53, "defesa": 51, "meio": 52, "serie": "C", "estado": "AM"},
    {"id": 57, "nome": "Altos", "sigla": "ALT", "ataque": 54, "defesa": 52, "meio": 53, "serie": "C", "estado": "PI"},
    {"id": 58, "nome": "River-PI", "sigla": "RIV", "ataque": 53, "defesa": 51, "meio": 52, "serie": "C", "estado": "PI"},
    {"id": 59, "nome": "Caxias", "sigla": "CAX", "ataque": 58, "defesa": 56, "meio": 57, "serie": "C", "estado": "RS"},
    {"id": 60, "nome": "Vitória-ES", "sigla": "VIT", "ataque": 52, "defesa": 50, "meio": 51, "serie": "C", "estado": "ES"},
]

teams_serie_d = [
    {"id": 61, "nome": "Sergipe", "sigla": "SER", "ataque": 52, "defesa": 50, "meio": 51, "serie": "D", "estado": "SE"},
    {"id": 62, "nome": "Lagarto", "sigla": "LAG", "ataque": 51, "defesa": 49, "meio": 50, "serie": "D", "estado": "SE"},
    {"id": 63, "nome": "ASA", "sigla": "ASA", "ataque": 50, "defesa": 48, "meio": 49, "serie": "D", "estado": "AL"},
    {"id": 64, "nome": "Coruripe", "sigla": "COR", "ataque": 49, "defesa": 47, "meio": 48, "serie": "D", "estado": "AL"},
    {"id": 65, "nome": "Santa Cruz-RN", "sigla": "SCR", "ataque": 48, "defesa": 46, "meio": 47, "serie": "D", "estado": "RN"},
    {"id": 66, "nome": "Potiguar", "sigla": "POT", "ataque": 47, "defesa": 45, "meio": 46, "serie": "D", "estado": "RN"},
    {"id": 67, "nome": "Moto Club", "sigla": "MOT", "ataque": 48, "defesa": 46, "meio": 47, "serie": "D", "estado": "MA"},
    {"id": 68, "nome": "Imperatriz", "sigla": "IMP", "ataque": 47, "defesa": 45, "meio": 46, "serie": "D", "estado": "MA"},
    {"id": 69, "nome": "Treze", "sigla": "TRE", "ataque": 49, "defesa": 47, "meio": 48, "serie": "D", "estado": "PB"},
    {"id": 70, "nome": "Campinense", "sigla": "CAM", "ataque": 48, "defesa": 46, "meio": 47, "serie": "D", "estado": "PB"},
    {"id": 71, "nome": "Retrô", "sigla": "RET", "ataque": 50, "defesa": 48, "meio": 49, "serie": "D", "estado": "PE"},
    {"id": 72, "nome": "Afogados", "sigla": "AFO", "ataque": 49, "defesa": 47, "meio": 48, "serie": "D", "estado": "PE"},
    {"id": 73, "nome": "Jacobinense", "sigla": "JAC", "ataque": 46, "defesa": 44, "meio": 45, "serie": "D", "estado": "BA"},
    {"id": 74, "nome": "Bahia de Feira", "sigla": "BAH", "ataque": 47, "defesa": 45, "meio": 46, "serie": "D", "estado": "BA"},
    {"id": 75, "nome": "Uberlândia", "sigla": "UBE", "ataque": 48, "defesa": 46, "meio": 47, "serie": "D", "estado": "MG"},
    {"id": 76, "nome": "Patrocinense", "sigla": "PAT", "ataque": 47, "defesa": 45, "meio": 46, "serie": "D", "estado": "MG"},
    {"id": 77, "nome": "Real Noroeste", "sigla": "REA", "ataque": 46, "defesa": 44, "meio": 45, "serie": "D", "estado": "ES"},
    {"id": 78, "nome": "Rio Branco-ES", "sigla": "RIO", "ataque": 45, "defesa": 43, "meio": 44, "serie": "D", "estado": "ES"},
    {"id": 79, "nome": "Portuguesa-RJ", "sigla": "POR", "ataque": 47, "defesa": 45, "meio": 46, "serie": "D", "estado": "RJ"},
    {"id": 80, "nome": "Olaria", "sigla": "OLA", "ataque": 46, "defesa": 44, "meio": 45, "serie": "D", "estado": "RJ"},
]

# Times estaduais (mais clubes regionais)
teams_estaduais = [
    # Paulistão
    {"id": 81, "nome": "Palmeiras", "sigla": "PAL", "ataque": 86, "defesa": 84, "meio": 83, "serie": "EST", "estado": "SP"},
    {"id": 82, "nome": "Corinthians", "sigla": "COR", "ataque": 79, "defesa": 77, "meio": 78, "serie": "EST", "estado": "SP"},
    {"id": 83, "nome": "São Paulo", "sigla": "SAO", "ataque": 80, "defesa": 78, "meio": 79, "serie": "EST", "estado": "SP"},
    {"id": 84, "nome": "Santos", "sigla": "SAN", "ataque": 78, "defesa": 74, "meio": 76, "serie": "EST", "estado": "SP"},
    {"id": 85, "nome": "RB Bragantino", "sigla": "RBB", "ataque": 74, "defesa": 72, "meio": 73, "serie": "EST", "estado": "SP"},
    {"id": 86, "nome": "Guarani", "sigla": "GUA", "ataque": 64, "defesa": 62, "meio": 63, "serie": "EST", "estado": "SP"},
    {"id": 87, "nome": "Ponte Preta", "sigla": "PON", "ataque": 66, "defesa": 64, "meio": 65, "serie": "EST", "estado": "SP"},
    {"id": 88, "nome": "Mirassol", "sigla": "MIR", "ataque": 65, "defesa": 63, "meio": 64, "serie": "EST", "estado": "SP"},
    # Cariocão
    {"id": 89, "nome": "Flamengo", "sigla": "FLA", "ataque": 88, "defesa": 82, "meio": 85, "serie": "EST", "estado": "RJ"},
    {"id": 90, "nome": "Fluminense", "sigla": "FLU", "ataque": 76, "defesa": 74, "meio": 75, "serie": "EST", "estado": "RJ"},
    {"id": 91, "nome": "Botafogo", "sigla": "BOT", "ataque": 75, "defesa": 73, "meio": 74, "serie": "EST", "estado": "RJ"},
    {"id": 92, "nome": "Vasco", "sigla": "VAS", "ataque": 72, "defesa": 70, "meio": 71, "serie": "EST", "estado": "RJ"},
    {"id": 93, "nome": "Volta Redonda", "sigla": "VOL", "ataque": 63, "defesa": 61, "meio": 62, "serie": "EST", "estado": "RJ"},
    {"id": 94, "nome": "Portuguesa-RJ", "sigla": "POR", "ataque": 47, "defesa": 45, "meio": 46, "serie": "EST", "estado": "RJ"},
    # Mineirão
    {"id": 95, "nome": "Atlético-MG", "sigla": "CAM", "ataque": 81, "defesa": 79, "meio": 80, "serie": "EST", "estado": "MG"},
    {"id": 96, "nome": "Cruzeiro", "sigla": "CRU", "ataque": 76, "defesa": 74, "meio": 75, "serie": "EST", "estado": "MG"},
    {"id": 97, "nome": "América-MG", "sigla": "AME", "ataque": 70, "defesa": 68, "meio": 69, "serie": "EST", "estado": "MG"},
    {"id": 98, "nome": "Tombense", "sigla": "TOM", "ataque": 60, "defesa": 58, "meio": 59, "serie": "EST", "estado": "MG"},
    # Gauchão
    {"id": 99, "nome": "Grêmio", "sigla": "GRE", "ataque": 77, "defesa": 75, "meio": 76, "serie": "EST", "estado": "RS"},
    {"id": 100, "nome": "Internacional", "sigla": "INT", "ataque": 78, "defesa": 76, "meio": 77, "serie": "EST", "estado": "RS"},
    {"id": 101, "nome": "Juventude", "sigla": "JUV", "ataque": 67, "defesa": 65, "meio": 66, "serie": "EST", "estado": "RS"},
    {"id": 102, "nome": "Caxias", "sigla": "CAX", "ataque": 58, "defesa": 56, "meio": 57, "serie": "EST", "estado": "RS"},
    # Baianão
    {"id": 103, "nome": "Bahia", "sigla": "BAH", "ataque": 73, "defesa": 71, "meio": 72, "serie": "EST", "estado": "BA"},
    {"id": 104, "nome": "Vitória", "sigla": "VIT", "ataque": 70, "defesa": 68, "meio": 69, "serie": "EST", "estado": "BA"},
    {"id": 105, "nome": "Jacobinense", "sigla": "JAC", "ataque": 46, "defesa": 44, "meio": 45, "serie": "EST", "estado": "BA"},
    # Cearense
    {"id": 106, "nome": "Fortaleza", "sigla": "FOR", "ataque": 74, "defesa": 72, "meio": 73, "serie": "EST", "estado": "CE"},
    {"id": 107, "nome": "Ceará", "sigla": "CEA", "ataque": 71, "defesa": 69, "meio": 70, "serie": "EST", "estado": "CE"},
    {"id": 108, "nome": "Ferroviário", "sigla": "FER", "ataque": 56, "defesa": 54, "meio": 55, "serie": "EST", "estado": "CE"},
    # Paranaense
    {"id": 109, "nome": "Athletico-PR", "sigla": "CAP", "ataque": 77, "defesa": 75, "meio": 76, "serie": "EST", "estado": "PR"},
    {"id": 110, "nome": "Londrina", "sigla": "LON", "ataque": 61, "defesa": 59, "meio": 60, "serie": "EST", "estado": "PR"},
    {"id": 111, "nome": "Operário-PR", "sigla": "OPE", "ataque": 62, "defesa": 60, "meio": 61, "serie": "EST", "estado": "PR"},
    # Goianão
    {"id": 112, "nome": "Goiás", "sigla": "GOI", "ataque": 69, "defesa": 67, "meio": 68, "serie": "EST", "estado": "GO"},
    {"id": 113, "nome": "Aparecidense", "sigla": "APA", "ataque": 56, "defesa": 54, "meio": 55, "serie": "EST", "estado": "GO"},
    # Catarinense
    {"id": 114, "nome": "Avaí", "sigla": "AVA", "ataque": 67, "defesa": 65, "meio": 66, "serie": "EST", "estado": "SC"},
    {"id": 115, "nome": "Chapecoense", "sigla": "CHA", "ataque": 65, "defesa": 63, "meio": 64, "serie": "EST", "estado": "SC"},
    {"id": 116, "nome": "Criciúma", "sigla": "CRI", "ataque": 69, "defesa": 67, "meio": 68, "serie": "EST", "estado": "SC"},
    # Pernambucano
    {"id": 117, "nome": "Sport", "sigla": "SPO", "ataque": 72, "defesa": 70, "meio": 71, "serie": "EST", "estado": "PE"},
    {"id": 118, "nome": "Náutico", "sigla": "NAU", "ataque": 68, "defesa": 66, "meio": 67, "serie": "EST", "estado": "PE"},
    {"id": 119, "nome": "Santa Cruz", "sigla": "STA", "ataque": 66, "defesa": 64, "meio": 65, "serie": "EST", "estado": "PE"},
    # Matogrossense
    {"id": 120, "nome": "Cuiabá", "sigla": "CUI", "ataque": 68, "defesa": 66, "meio": 67, "serie": "EST", "estado": "MT"},
]

# Junta todos os times
all_teams = teams_serie_a + teams_serie_b + teams_serie_c + teams_serie_d + teams_estaduais

# ============================================================
# FUNÇÕES DE SIMULAÇÃO
# ============================================================

def calcular_forca(time):
    return time['ataque'] * 0.4 + time['meio'] * 0.35 + time['defesa'] * 0.25

def simular_partida(time_casa, time_fora):
    gols_casa = 0
    gols_fora = 0
    eventos = []

    forca_casa = calcular_forca(time_casa)
    forca_fora = calcular_forca(time_fora)

    for minuto in range(1, 91):
        caos = random.random()
        chance_casa = min(max((forca_casa + 8) / 2200 + caos * 0.01, 0.01), 0.12)
        chance_fora = min(max(forca_fora / 2200 + (1 - caos) * 0.008, 0.01), 0.11)

        if random.random() < chance_casa:
            gols_casa += 1
            eventos.append(f"GOL DO {time_casa['nome'].upper()} aos {minuto} min!")
        if random.random() < chance_fora:
            gols_fora += 1
            eventos.append(f"GOL DO {time_fora['nome'].upper()} aos {minuto} min!")
        if random.random() < 0.018:
            eventos.append(f"Cartão amarelo aos {minuto} min")
        if random.random() < 0.008:
            eventos.append(f"Lesão aos {minuto} min")

    return gols_casa, gols_fora, eventos

# ============================================================
# INTERFACE STREAMLIT
# ============================================================

st.set_page_config(page_title="Brasfoot Brasileirão", layout="wide")
st.title("⚽ Brasfoot Brasileirão Completo")
st.markdown("Brasileirão Série A, B, C, D + Estaduais")

# Inicializar estado da sessão
if 'tabelas' not in st.session_state:
    st.session_state.tabelas = {}
    for time in all_teams:
        chave = f"{time['serie']}_{time['estado']}" if time['serie'] == 'EST' else time['serie']
        if chave not in st.session_state.tabelas:
            st.session_state.tabelas[chave] = {}
        if time['nome'] not in st.session_state.tabelas[chave]:
            st.session_state.tabelas[chave][time['nome']] = {'P': 0, 'J': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}

if 'partidas_realizadas' not in st.session_state:
    st.session_state.partidas_realizadas = 0

# Sidebar - seleção de competição
competicao = st.sidebar.selectbox(
    "Selecione a competição",
    ["Brasileirão Série A", "Brasileirão Série B", "Brasileirão Série C", "Brasileirão Série D", "Estaduais"]
)

# Mapear competição para times e chave
if competicao == "Brasileirão Série A":
    times_comp = teams_serie_a
    chave = "A"
elif competicao ==
