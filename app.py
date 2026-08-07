import streamlit as st
import random

st.title("O que esse borrão parece?")
st.write("Observe a imagem abstrata e diga o que você vê!")

# Lista de 'borrões' (pode ser substituída por URLs de imagens ou formas geométricas)
borroes = ["uma nuvem em formato de coelho", "um monstro com três olhos", "uma ilha perdida"]
imagem_atual = random.choice(borroes)

st.subheader("O que é isso?")
st.image("https://via.placeholder.com/400x200", caption="Forma misteriosa")

palpite = st.text_input("Qual o seu palpite?")

if st.button("Enviar"):
    st.write(f"Você acha que é: {palpite}")
    st.write(f"Outras pessoas disseram que parece: {imagem_atual}")
    st.success("Obrigado por participar da nossa galeria abstrata!")

st.write("---")
st.write("Deseja ver outro borrão ou prefere que eu ajude a gerar uma descrição mais complexa para um novo desafio visual?")
