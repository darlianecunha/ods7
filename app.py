import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the variables
variables = [
    "Número de programas de conscientização em uso racional de energia",
    "Número de programas de gestão de Energy Efficiency",
    "Número de iniciativas de inovação tecnológica em Energy Efficiency",
    "Percentual de energia renovável contratada e produzida em instalações portuárias",
    "Percentual de biocombustíveis em cargas elétricas e mecânicas",
    "Número de iniciativas de inovação tecnológica em energia renovável",
    "Diversidade de fontes de energia renovável em instalações portuárias",
    "Quantidade de parcerias para promoção de energia limpa",
    "Quantidade de estações de carregamento para veículos elétricos",
    "Percentual de fornecimento de energia renovável para navios",
    "Percentual de abastecimento com GNL",
    "Número de iniciativas de inovação tecnológica em atendimento elétrico e energético para navios",
    "Quantidade de navios usando energia renovável no porto",
    "Tarifas diferenciadas para navios com desempenho acima dos padrões ambientais"
]

# Streamlit app title
st.title("Port Energy Efficiency Assessment (ODS 07)")

# Collect scores for each variable
scores = []
for variable in variables:
    score = st.slider(variable, 0, 3, 0)
    scores.append(score)

# Calculate final score as a percentage
total_score = sum(scores)
max_score = len(variables) * 3  # maximum score if all variables scored 3
percentage_score = (total_score / max_score) * 100
st.write(f"Final Score: {percentage_score:.2f}%")

# Radar chart function
def plot_radar_chart(scores):
    categories = [f"7.{i+1}" for i in range(len(scores))]
    values = scores + scores[:1]  # Repeat the first value to close the circle
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='teal', alpha=0.25)
    ax.plot(angles, values, color='teal', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    return fig

# Display radar chart
st.subheader("Radar Chart")
st.pyplot(plot_radar_chart(scores))
