import streamlit as st
from utils.calculations import calculate_final_score
from utils.radar_chart import plot_radar_chart

# Define the variables and their options
variables = [
    {"name": "Número de programas de conscientização em uso racional de energia", "options": [
        "0: Nenhum programa em operação.",
        "1: Até 2 programas em operação, atingindo até 100 pessoas.",
        "2: 3-5 programas em operação, atingindo 101-500 pessoas.",
        "3: Mais de 5 programas em operação, atingindo mais de 500 pessoas."
    ]},
    {"name": "Número de programas de gestão de Energy Efficiency", "options": [
        "0: Nenhum programa em operação.",
        "1: Pelo menos um programa, resultando em até 5% de redução no consumo de energia.",
        "2: Pelo menos um programa, resultando em uma redução maior que 5% e menor ou igual a 10% no consumo de energia.",
        "3: Pelo menos um programa com reduções no consumo de energia superiores a 10%."
    ]},
    {"name": "Número de iniciativas de inovação tecnológica em Energy Efficiency", "options": [
        "0: Nenhuma iniciativa.",
        "1: Até 2 iniciativas tecnológicas implementadas.",
        "2: 3-5 iniciativas tecnológicas implementadas.",
        "3: Mais de 5 iniciativas implementadas."
    ]},
    {"name": "Percentual de energia renovável contratada e produzida em instalações portuárias", "options": [
        "0: Nenhum uso de energia renovável.",
        "1: Até 10% da energia utilizada é renovável.",
        "2: Mais de 10% até 50% da energia usada é renovável.",
        "3: Mais de 50% da energia usada é renovável."
    ]},
    {"name": "Percentual de biocombustíveis em cargas elétricas e mecânicas", "options": [
        "0: Nenhum uso de biocombustíveis.",
        "1: Menos de 5% das cargas são operadas com biocombustíveis.",
        "2: 5% a 20% das cargas são operadas com biocombustíveis.",
        "3: Mais de 20% das cargas são operadas com biocombustíveis."
    ]},
    {"name": "Número de iniciativas de inovação tecnológica em energia renovável", "options": [
        "0: Nenhuma iniciativa.",
        "1: Até 2 iniciativas na fase de planejamento ou piloto.",
        "2: 3-5 iniciativas na fase de implementação com resultados preliminares.",
        "3: Mais de 5 iniciativas em plena operação com resultados comprovados."
    ]},
    {"name": "Diversidade de fontes de energia renovável em instalações portuárias", "options": [
        "0: Nenhum uso de fontes renováveis.",
        "1: Uso de 1 tipo diferente de energia renovável.",
        "2: Uso de 2 tipos diferentes de energia renovável.",
        "3: Uso de 3 ou mais tipos diferentes de energia renovável."
    ]},
    {"name": "Quantidade de parcerias para promoção de energia limpa", "options": [
        "0: Nenhuma parceria estabelecida.",
        "1: Até 2 parcerias estabelecidas com foco em energia limpa.",
        "2: 3-5 parcerias estabelecidas com foco em energia limpa.",
        "3: Mais de 5 parcerias estabelecidas com foco em energia limpa."
    ]},
    {"name": "Quantidade de estações de carregamento para veículos elétricos", "options": [
        "0: Nenhuma estação de carregamento disponível.",
        "1: Até 5 estações de carregamento disponíveis.",
        "2: 6-15 estações de carregamento disponíveis.",
        "3: Mais de 15 estações de carregamento disponíveis."
    ]},
    {"name": "Percentual de fornecimento de energia renovável para navios", "options": [
        "0: Nenhum fornecimento de energia renovável para navios.",
        "1: Menos de 10% do fornecimento de energia para navios vem de fontes renováveis.",
        "2: Entre 10% e 30% do fornecimento de energia para navios vem de fontes renováveis.",
        "3: Mais de 30% do fornecimento de energia para navios vem de fontes renováveis."
    ]},
    {"name": "Percentual de abastecimento com GNL", "options": [
        "0: Nenhum abastecimento de GNL.",
        "1: Menos de 5% do fornecimento total de combustível é com GNL.",
        "2: Entre 5% e 20% do fornecimento total de combustível é com GNL.",
        "3: Mais de 20% do fornecimento total de combustível é com GNL."
    ]},
    {"name": "Número de iniciativas de inovação tecnológica em atendimento elétrico e energético para navios", "options": [
        "0: Nenhuma iniciativa.",
        "1: Até 2 iniciativas de inovação tecnológica em fase de planejamento ou piloto.",
        "2: 3-5 iniciativas em fase de implementação ou avaliação de eficácia.",
        "3: Mais de 5 iniciativas em plena operação, com resultados de eficácia comprovados."
    ]},
    {"name": "Quantidade de navios usando energia renovável no porto", "options": [
        "0: Nenhum navio utiliza energia renovável.",
        "1: Até 5% dos navios no porto utilizam energia renovável.",
        "2: 5% a 15% dos navios no porto utilizam energia renovável.",
        "3: Mais de 15% dos navios no porto utilizam energia renovável."
    ]},
    {"name": "Tarifas diferenciadas para navios com desempenho acima dos padrões ambientais", "options": [
        "0: Nenhuma aplicação de tarifas diferenciadas.",
        "1: Até 5% de desconto nas tarifas portuárias.",
        "2: 5% a 15% de desconto nas tarifas portuárias.",
        "3: Mais de 15% de desconto nas tarifas portuárias."
    ]}
]

# Streamlit app title
st.title("Port Energy Efficiency Assessment (ODS 07)")

# Collect scores for each variable
scores = []
for variable in variables:
    option = st.selectbox(variable["name"], options=variable["options"])
    scores.append(int(option[0]))  # Convert the selected option's score (first character) to integer

# Calculate final score
percentage_score = calculate_final_score(scores)
st.write(f"Final Score: {percentage_score:.2f}%")

# Display radar chart
st.subheader("Radar Chart")
st.pyplot(plot_radar_chart(scores))


