# bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dt = pd.read_csv('data/dados_estudantes.csv', sep = ',')

dt.info()

# traducao das colunas do dataset
traducao_colunas = {
    "StudentID": "ID_Aluno",
    "Age": "Idade",
    "Gender": "Genero",
    "Ethnicity": "Etnia",
    "ParentalEducation": "Escolaridade_Pais",
    "StudyTimeWeekly": "Horas_Estudo_Semanais",
    "Absences": "Faltas",
    "Tutoring": "Aulas_Particulares",
    "ParentalSupport": "Apoio_Pais",
    "Extracurricular": "Atividades_Extracurriculares",
    "Sports": "Esportes",
    "Music": "Musica",
    "Volunteering": "Voluntariado",
    "GPA": "Media_Notas",
    "GradeClass": "Classificacao_Notas"
}

dt = dt.rename(traducao_colunas, axis = 1) # traducao do nome das colunas


pd.options.display.float_format = '{:.1f}'.format # definicao de visualizacao para numeros com uma casa decimal
dt.isnull().sum() # contagem de valores nulos
dt.duplicated().sum() # contagem de linhas duplicadas


# substituicao de valores das colunas
dt["Genero"] = dt.apply(
    lambda row: 'masculino' if row["Genero"] == 0
    else 'feminino',
    axis = 1
)

dt["Etnia"] = dt.apply(
    lambda row: 'caucasiano' if row["Etnia"] == 0
    else 'afrodescendente' if row["Etnia"] == 1
    else 'asiatico' if row["Etnia"] == 2 
    else 'outro',
    axis = 1
)

dt["Escolaridade_Pais"] = dt.apply(
    lambda row: 'nenhuma' if row["Escolaridade_Pais"] == 0
    else 'ensino_medio' if row["Escolaridade_Pais"] == 1
    else 'graduacao_incompleta' if row["Escolaridade_Pais"] == 2
    else 'graduacao_completa' if row["Escolaridade_Pais"] == 3
    else 'pos_graduacao',
    axis = 1
)

dt["Aulas_Particulares"] = dt.apply(
    lambda row: 'nao' if row["Aulas_Particulares"] == 0
    else 'sim',
    axis = 1
)

dt["Apoio_Pais"] = dt.apply(
    lambda row: 'nenhum' if row["Apoio_Pais"] == 0
    else 'baixo' if row["Apoio_Pais"] == 1
    else 'moderado' if row["Apoio_Pais"] == 2
    else 'alto' if row["Apoio_Pais"] == 3
    else 'muito_alto',
    axis = 1
)

dt["Atividades_Extracurriculares"] = dt.apply(
    lambda row: 'nao' if row["Atividades_Extracurriculares"] == 0
    else 'sim',
    axis = 1
)

dt["Esportes"] = dt.apply(
    lambda row: 'nao' if row["Esportes"] == 0
    else 'sim',
    axis = 1
)

dt["Musica"] = dt.apply(
    lambda row: 'nao' if row["Musica"] == 0
    else 'sim',
    axis = 1
)

dt["Voluntariado"] = dt.apply(
    lambda row: 'nao' if row["Voluntariado"] == 0
    else 'sim',
    axis = 1
)

dt["Classificacao_Notas"] = dt.apply(
    lambda row: 'A' if row["Classificacao_Notas"] == 0
    else 'B' if row["Classificacao_Notas"] == 1
    else 'C' if row["Classificacao_Notas"] == 2
    else 'D' if row["Classificacao_Notas"] == 3
    else 'F',
    axis = 1
)

print(dt)


### organizacao de colunas do dataset ###

# adicao das colunas 'esportes', 'musica' e 'voluntariado' em 'atividades extracurriculares'
dt["Atividades_Extracurriculares"] = dt.apply(
    lambda x: 'sim' if x["Atividades_Extracurriculares"] == 'sim' 
    or 'sim' in x[["Esportes", "Musica", "Voluntariado"]].values 
    else 'nao',
    axis = 1
)

# remocao das colunas 'esportes', 'musica' e 'voluntariado'
dt = dt.drop(columns=["Esportes", "Musica", "Voluntariado"])

# renomear coluna 'horas_estudo_semanais' para 'horas_estudo'
dt = dt.rename(columns={'Horas_Estudo_Semanais': 'Horas_Estudo'})

print(dt)

sns.set_context(font_scale = 1.2) # definicao do tamanho padrao da fonte
dt.describe()



## funcoes

# adicao de valores nas barras e colunas dos graficos
def valor_barras(plot, casas_decimais):
    for valor in plot.containers:
        plot.bar_label(valor, fmt=f'%.{casas_decimais}f', label_type='edge')


# geracao de graficos de colunas com uma variavel
def grafico_colunas_1(relacao, paleta):
    grafico = sns.barplot(x = relacao.index, y = relacao.values, hue = relacao.index, palette=paleta)
    return grafico

# geracao de graficos de barras com uma variavel
def grafico_barras_1(relacao, paleta):
    grafico = sns.barplot(y = relacao.index, x = relacao.values, hue = relacao.index, palette=paleta)
    return grafico


# geracao de grafico de colunas com duas variaveis
def grafico_colunas(relacao, coluna_x, tipo_relacao, paleta):
    grafico = sns.barplot(data = relacao, x = coluna_x, y = tipo_relacao, hue = coluna_x, palette=paleta)
    return grafico

# geracao de grafico de barras com duas variaveis
def grafico_barras(relacao, coluna_x, tipo_relacao, paleta):
    grafico = sns.barplot(data = relacao, y = coluna_x, x = tipo_relacao, hue = coluna_x, palette=paleta)
    return grafico


# geracao de grafico de barras agrupadas
def grafico_barras_agrupadas(relacao, coluna_x, coluna_y, tipo_relacao, paleta):
    grafico = sns.barplot(data = relacao, y = coluna_x, x = tipo_relacao, hue = coluna_y, palette=paleta)
    return grafico
    
    
# geracao de grafico de setores com uma variavel
def grafico_setores_1(relacao, paleta):
    plt.pie(relacao, labels = relacao.index, autopct="%1.1f%%", colors = sns.color_palette(paleta))

# geracao de grafico de setores com duas variaveis
def grafico_setores(coluna1_dt, coluna2_dt, valor_dt, paleta):
    dados = dt[dt[coluna1_dt] == valor_dt]
    relacao = dados[coluna2_dt].value_counts()
    grafico_setores_1(relacao, paleta)


# geracao de grafico de dispersao
def grafico_dispersao(dataframe, coluna_x, coluna_y, paleta, cor_linha_tendencia):
    sns.scatterplot(data = dataframe, x = coluna_x, y = coluna_y, color = paleta, markers='o')
    sns.regplot(data = dataframe, x = coluna_x, y = coluna_y, scatter = False, color=cor_linha_tendencia)


## secao 1

# quantidade de estudantes participantes da pesquisa por genero, idade e etnia
contagem_genero = dt['Genero'].value_counts().sort_values(ascending=False)
contagem_idade = dt['Idade'].value_counts()
contagem_etnia = dt['Etnia'].value_counts()

plt.figure(figsize=(22, 7))

# grafico 1
plt.subplot(1,3,1)
plt.title("Quantidade de Estudantes por Gênero")
grafico = grafico_barras_1(contagem_genero, 'flare_r')
valor_barras(grafico, 0)
plt.xlabel('Gênero')
plt.ylabel('Contagem')

# grafico 2
plt.subplot(1,3,2)
plt.title("Quantidade de Estudantes por Idade")
grafico = grafico_colunas_1(contagem_idade, 'flare')
valor_barras(grafico, 0)
plt.xlabel('Idade')
plt.ylabel('Contagem')

# grafico 3
plt.subplot(1,3,3)
plt.title("Quantidade de Estudantes por Etnia")
grafico_setores_1(contagem_etnia, 'magma_r')

plt.tight_layout()
plt.show()



## secao 2
# proporcao escolaridade pais x etnia dos alunos

plt.figure(figsize=(15,15))

# estudantes caucasianos
plt.subplot(2,2,1)
plt.title("Proporção da Escolaridade dos Pais de estudantes Caucasianos")
grafico_setores('Etnia', 'Escolaridade_Pais', 'caucasiano', 'magma_r')

# estudantes afrodescendentes
plt.subplot(2,2,2)
plt.title("Proporção da Escolaridade dos Pais de estudantes Afrodescendentes")
grafico_setores('Etnia', 'Escolaridade_Pais', 'afrodescendente', 'magma_r')

# estudantes asiaticos
plt.subplot(2,2,3)
plt.title("Proporção da Escolaridade dos Pais de estudantes Asiáticos")
grafico_setores('Etnia', 'Escolaridade_Pais', 'asiatico', 'magma_r')

# estudantes outros
plt.subplot(2,2,4)
plt.title("Proporção da Escolaridade dos Pais de estudantes de Outra etnia")
grafico_setores('Etnia', 'Escolaridade_Pais', 'outro', 'magma_r')

plt.tight_layout()
plt.show()



## secao 3
# genero x atividades curriculares

plt.figure(figsize=(20,6))

genero_por_atividades = dt.groupby(['Genero','Atividades_Extracurriculares']).size().reset_index(name = 'Contagem')
genero_por_atividades = genero_por_atividades.sort_values(by='Contagem', ascending=False)

plt.subplot(1,3,1)
plt.title("Relação entre Gênero e realização de Atividades Extracurriculares")
grafico = grafico_barras_agrupadas(genero_por_atividades, 'Genero', 'Atividades_Extracurriculares', 'Contagem', 'flare_r')
valor_barras(grafico, 0)
plt.xlabel("Atividades Extracurriculares")
plt.ylabel("Gênero")

# atividades extracurriculares x quantidade de faltas
atividades_por_faltas = dt.groupby('Atividades_Extracurriculares')['Faltas'].sum().reset_index(name='Total_Faltas')
atividades_por_faltas = atividades_por_faltas.sort_values(by='Total_Faltas', ascending=True)

plt.subplot(1,3,2)
plt.title("Relação entre realização de Atividades Extracurriculares e Total de Faltas de estudantes")
grafico = grafico_colunas(atividades_por_faltas, 'Atividades_Extracurriculares', 'Total_Faltas', 'flare')
valor_barras(grafico, 0)
plt.xlabel("Atividades Extracurriculares")
plt.ylabel("Quantidade de Faltas Totais")

# genero x faltas
genero_por_faltas = dt.groupby('Genero')['Faltas'].sum().reset_index(name = 'Total_Faltas')
genero_por_faltas = genero_por_faltas.sort_values(by='Total_Faltas', ascending=True)

plt.subplot(1,3,3)
plt.title("Relação entre Gênero e Total de Faltas de estudantes")
grafico = grafico_colunas(genero_por_faltas, 'Genero', 'Total_Faltas', 'flare')
valor_barras(grafico, 0)
plt.xlabel("Gênero")
plt.ylabel("Quantidade de Faltas Totais")

plt.tight_layout()
plt.show()



## secao 4
# apoio dos pais x horas de estudo

plt.figure(figsize=(15,6))

apoio_por_horas_estudo = dt.groupby('Apoio_Pais')['Horas_Estudo'].mean().reset_index(name = 'Media_Horas')
apoio_por_horas_estudo = apoio_por_horas_estudo.sort_values(by='Media_Horas', ascending=False)

plt.subplot(1,2,1)
plt.title("Relação entre Apoio do Pais e média de horas de estudo semanal dos estudantes")
grafico = grafico_barras(apoio_por_horas_estudo, 'Apoio_Pais', 'Media_Horas', 'flare_r')
valor_barras(grafico, 1)
plt.xlabel("Média de Horas de Estudo Semanais")
plt.ylabel("Nível de Apoio dos Pais")

# idade x horas de estudo
idade_por_horas_estudo = dt.groupby('Idade')['Horas_Estudo'].mean().reset_index(name='Media_Horas')
idade_por_horas_estudo = idade_por_horas_estudo.sort_values(by='Media_Horas', ascending=True)

plt.subplot(1,2,2)
plt.title("Relação entre Idade e média de horas de estudo semanal dos estudantes")
grafico = grafico_colunas(idade_por_horas_estudo, 'Idade', 'Media_Horas', 'flare')
valor_barras(grafico, 1)
plt.xlabel("Idade")
plt.ylabel("Média de Horas de Estudo Semanal")

plt.tight_layout()
plt.show()



## secao 5
## dados demograficos

plt.figure(figsize=(15,12))

# idade x media de notas
idade_por_notas = dt.groupby('Idade')['Media_Notas'].mean().reset_index(name = 'Media')
idade_por_notas = idade_por_notas.sort_values(by='Media', ascending=True)

plt.subplot(2,2,1)
plt.title("Relação entre Idade dos estudantes e Média de Notas")
grafico = grafico_colunas(idade_por_notas, 'Idade', 'Media', 'flare')
valor_barras(grafico, 2)
plt.xlabel("Idade")
plt.ylabel("Média de Notas")


# genero x media de notas
genero_por_notas = dt.groupby('Genero')['Media_Notas'].mean().reset_index(name = "Media")
genero_por_notas = genero_por_notas.sort_values(by='Media', ascending=True)

plt.subplot(2,2,2)
plt.title("Relação entre Gênero dos estudantes e Média de Notas")
grafico = grafico_colunas(genero_por_notas, 'Genero', 'Media', 'flare')
valor_barras(grafico, 2)
plt.xlabel("Gênero")
plt.ylabel("Média de Notas")

# etnia x media de notas
etnia_por_notas = dt.groupby('Etnia')['Media_Notas'].mean().reset_index(name = 'Media')
etnia_por_notas = etnia_por_notas.sort_values(by='Media', ascending=False)

plt.subplot(2,2,3)
plt.title("Relação entre Etnia dos estudantes e Média de Notas")
grafico = grafico_barras(etnia_por_notas, 'Etnia', 'Media', 'flare_r')
valor_barras(grafico, 2)
plt.xlabel("Média de Notas")
plt.ylabel("Etnia")

# escolaridade dos pais x media de notas
escolaridade_por_notas = dt.groupby('Escolaridade_Pais')['Media_Notas'].mean().reset_index(name = 'Media')
escolaridade_por_notas = escolaridade_por_notas.sort_values(by='Media', ascending=False)

plt.subplot(2,2,4)
plt.title("Relação entre Escolaridade dos Pais dos estudantes e Média de Notas")
grafico = grafico_barras(escolaridade_por_notas, 'Escolaridade_Pais', 'Media', 'flare_r')
valor_barras(grafico, 2)
plt.xlabel("Média de Notas")
plt.ylabel("Nível de Escolaridade dos Pais")

plt.tight_layout()
plt.show()



## secao 6
## dados academicos

plt.figure(figsize=(15,6))

# atividades extracurriculares x media de notas
atividades_por_notas = dt.groupby('Atividades_Extracurriculares')['Media_Notas'].mean().reset_index(name = "Media")
atividades_por_notas = atividades_por_notas.sort_values(by='Media', ascending=True)

plt.subplot(1,2,1)
plt.title("Relação entre realização de Atividades Extracurriculares e Média de Notas")
grafico = grafico_colunas(atividades_por_notas, 'Atividades_Extracurriculares', 'Media', 'flare')
valor_barras(grafico, 2)
plt.xlabel("Realização de Atividades Extracurriculares")
plt.ylabel("Média de Notas")


# aulas particulares x media de notas
aulas_part_por_notas = dt.groupby('Aulas_Particulares')['Media_Notas'].mean().reset_index(name = "Media")
aulas_part_por_notas = aulas_part_por_notas.sort_values(by='Media', ascending=True)

plt.subplot(1,2,2)
plt.title("Relação entre participação de Aulas Particulares e Média de Notas")
grafico = grafico_colunas(aulas_part_por_notas, 'Aulas_Particulares', 'Media', 'flare')
valor_barras(grafico, 2)
plt.xlabel("Participação de Aulas Particulares")
plt.ylabel("Média de Notas")

plt.tight_layout()
plt.show()



## secao 7
## dados comportamentais

plt.figure(figsize=(20,6))

# horas de estudo x media de notas
plt.subplot(1,3,1)
plt.title("Relação entre horas de estudo semanal e Média de Notas")
grafico_dispersao(dt, 'Horas_Estudo', 'Media_Notas', '#d27979', '#872c2c')
plt.xlabel("Quantidade de Horas de Estudo Semanais")
plt.ylabel("Média de Notas")


# quantidade de faltas x media de notas
plt.subplot(1,3,2)
plt.title("Relação entre Quantidade de Faltas e Média de Notas")
grafico_dispersao(dt, 'Faltas', 'Media_Notas', '#d27979', '#872c2c')
plt.xlabel("Quantidade de Faltas")
plt.ylabel("Média de Notas")


# apoio dos pais x media de notas
apoio_por_notas = dt.groupby('Apoio_Pais')['Media_Notas'].mean().reset_index(name = 'Media')
apoio_por_notas = apoio_por_notas.sort_values(by='Media', ascending=False)

plt.subplot(1,3,3)
plt.title("Relação entre o Apoio dos Pais e a Média de Notas")
grafico = grafico_barras(apoio_por_notas, 'Apoio_Pais', 'Media', 'flare_r')
valor_barras(grafico, 2)
plt.xlabel("Média de Notas")
plt.ylabel("Nível de Apoio dos Pais")

plt.tight_layout()
plt.show()



## secao 8
# classificacao x quantidade de notas

plt.figure(figsize=(8,8))

contagem_notas = dt['Classificacao_Notas'].value_counts()

plt.title("Proporção da Classificação das Notas e Quantidade de Notas")
grafico_setores_1(contagem_notas, 'magma_r')

plt.tight_layout
plt.show()