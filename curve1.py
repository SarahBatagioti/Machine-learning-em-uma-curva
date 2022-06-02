#importando da biblioteca
import numpy as np

# Os valores "listex" são usados como valores de entrada "listey" os valores de saída.
# Juntos eles constroem os dados de treinamento.
# Estes são valores que resultam de uma função linear e números aleatórios, normalmente distribuídos.

listex = np.linspace(-40,40,20)
# linspace retorna amostras espaçadas uniformemente, calculadas ao longo do intervalo

# parametros:
# (iniciar, parar, número de amostras para gerar)

listey = np.array([0.3*i + np.random.normal(0, 1, 1) for i in listex])
# array cria uma matriz, ou seja, uma estrutura de dados do tipo vetor (estrutura de dados indexada,
# que pode armazenar uma determinada quantidade de valores do mesmo tipo) com duas ou mais dimensões

# parametros:
# ([ tipo mínimo necessário para segurar os objetos na sequência * se verdadeiro (padrão), então o objeto será copiado +
# (média ("centro") da distribuição, desvio padrão (spread ou "largura") da distribuição, forma de saída) repetição])

#for __ in __: definir o loop e iterador (variável que é usada para repetir ao longo da sequência.
# É usado para acessar cada elemento na sequência)
print(listey)

