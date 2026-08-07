import streamlit as st
import random
import time

# Times mockados
teams = [
    {'id': 1, 'nome': 'XV de Python', 'ataque': 72, 'defesa': 68, 'meio': 70},
    {'id': 2, 'nome': 'Streamlit FC', 'ataque': 69, 'defesa': 66, 'meio': 71},
    {'id': 3, 'nome': 'Data United', 'ataque': 65, 'defesa': 70, 'meio': 67},
    {'id': 4, 'nome': 'AI Warriors', 'ataque': 75, 'defesa': 60, 'meio': 72},
]

def calcular_forca(time):
    return time['ataque'] * 0.4 + time['meio'] * 0.35 + time['defesa'] * 0.25

def simular_partida(casa, fora):
    gols_casa = 0
    gols_fora = 0
    eventos = []

    forca_casa = calcular_forca(casa)
    forca_fora = calcular_forca(fora)

    for minuto in range(1, 91):
        caos = random.random()

        chance_casa = min(max((forca_casa + 8) / 2200 + caos * 0.01, 0.01), 0.12)
        chance_fora = min(max(forca_fora / 2200 + (1 - caos) * 0.008, 0.01), 0.11)

        if random.random() < chance_casa:
            gols_casa += 1
            eventos.append(f"GOL DO {casa['nome'].upper()} aos {minuto} minutos!")

        if random.random() < chance_fora:
            gols_fora += 1
            eventos.append(f"GOL DO {fora['nome'].upper()} aos {minuto} minutos!")

        if random.random() < 0.018:
            eventos.append(f"Cartão amarelo aos {minuto} minutos. Entrada criminosa, porém futebolística.")

        if random.random() < 0.008:
            eventos.append(f"Lesão aos {minuto} minutos. A coxa foi de arrasta.")

    return gols_casa, gols_fora, eventos

st.title('Brasfoot Classic - Simulador de Partidas')

st.sidebar.header('Escolha os times')
nomes_times = [t['nome'] for t in teams]

time_casa_nome = st.sidebar.selectbox('Time da casa', nomes_times, index=0)
time_fora_nome = st.sidebar.selectbox('Time visitante', nomes_times, index=1)

time_casa = next(t for t in teams if t['nome'] == time_casa_nome)
time_fora = next(t for t in teams if t['nome'] == time_fora_nome)

if st.button('Simular partida'):
    placar_texto = st.empty()
    eventos_container = st.container()

    gols_casa, gols_fora = 0, 0
    eventos = []

    for minuto in range(1, 91):
        caos = random.random()

        chance_casa = min(max((calcular_forca(time_casa) + 8) / 2200 + caos * 0.01, 0.01), 0.12)
        chance_fora = min(max(calcular_forca(time_fora) / 2200 + (1 - caos) * 0.008, 0.01), 0.11)

        if random.random() < chance_casa:
            gols_casa += 1
            eventos.append(f"GOL DO {time_casa_nome.upper()} aos {minuto} minutos!")

        if random.random() < chance_fora:
            gols_fora += 1
            eventos.append(f"GOL DO {time_fora_nome.upper()} aos {minuto} minutos!")

        if random.random() < 0.018:
            eventos.append(f"Cartão amarelo aos {minuto} minutos. Entrada criminosa, porém futebolística.")

        if random.random() < 0.008:
            eventos.append(f"Lesão aos {minuto} minutos. A coxa foi de arrasta.")

        placar_texto.markdown(f"## {time_casa_nome} {gols_casa} x {gols_fora} {time_fora_nome}")
        eventos_container.empty()
        with eventos_container:
            for ev in eventos:
                st.write(f"- {ev}")

        time.sleep(0.05)  # velocidade da simulação

    st.success("Fim de jogo! Se prepare para o próximo caos.")
