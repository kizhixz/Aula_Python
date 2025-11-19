"""
ASSUNTO PRINCIPAL DETECTADO: Entrada e Saída em Python

Resumo geral do assunto:
Este documento apresenta de forma completa o funcionamento das operações de entrada
(input) e saída (print) em Python. Esses recursos permitem a interação entre o usuário 
e o programa, seja solicitando dados, seja exibindo informações formatadas.

Explicação clara e didática:
A função `input()` coleta dados digitados pelo usuário e sempre retorna uma string.
Já a função `print()` exibe textos, variáveis e resultados no console.  
Também são abordados conceitos como conversão de tipos, múltiplas entradas com split(),
impressão de dados, exemplos de tipos básicos e verificação de tipos com type().

Contexto no Python:
Entrada e saída são fundamentais para qualquer aplicação interativa. Python mantém a
simplicidade, utilizando o console como interface padrão para inserir e exibir dados.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL (ENTRADA E SAÍDA)
# ------------------------------------------------------------
# A função input():
# - Pausa o programa até o usuário digitar algo.
# - Sempre retorna o valor inserido como string (`str`).
# - Pode exibir uma mensagem de orientação ao usuário.
# - Permite conversões explícitas usando int(), float(), etc.

# A função print():
# - Exibe informações no console.
# - Aceita múltiplos valores separados por vírgula.
# - Pode imprimir strings, variáveis, expressões e resultados.

# Conversão de tipos:
# - int() converte para inteiro.
# - float() converte para número decimal.
# - Obrigatória quando se deseja trabalhar com números, pois input() retorna string.

# Recebendo múltiplas entradas:
# - input().split() divide a string em valores separados por espaço.
# - Permite atribuição múltipla: x, y = input(...).split()

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# Tipos de dados citados:
# - str, int, float, tuple, list, dict.
# Uso da função type() para verificar tipos.
# Estruturas de dados apenas exemplificadas, sem aprofundamento.
# Valores literais, mensagens de texto e conceitos simples de variáveis foram utilizados.

# ------------------------------------------------------------
# EXEMPLOS (DO CONTEÚDO + COMPLEMENTARES)
# ------------------------------------------------------------

# Exemplo 1: entrada simples e impressão
nome = input("Digite seu nome: ")
print("Olá,", nome)
# Explicação: input coleta o nome como string, print exibe saudação.

# Exemplo 2: entrada simples e saída direta
val = input("Enter your value: ")
print(val)
# Explicação: qualquer entrada é retornada como string.

# Exemplo 3: verificando tipos
num = input("Enter number:")
print(num)
name1 = input("Enter name: ")
print(name1)
print("type of number", type(num))
print("type of name", type(name1))
# Explicação: type() revela que ambas entradas são strings.

# Exemplo 4: conversão para inteiro
num = int(input("Enter a number: "))
print(num, "is of type", type(num))
# Explicação: int() converte a string para número inteiro.

# Exemplo 5: conversão para float
floatNum = float(input("Enter a decimal number: "))
print(floatNum, "is of type", type(floatNum))
# Explicação: float() converte para número decimal.

# Exemplo 6: múltiplas entradas
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)
# Explicação: split() divide a entrada, criando duas strings.

# Exemplo 7: impressão básica
print("Hello, World!")
# Explicação: print imprime literal de string.

# Exemplo 8: impressão múltipla
s = "Alice"
age = 25
city = "New York"
print(s, age, city)
# Explicação: print aceita múltiplos argumentos.

# Exemplo 9: múltiplas entradas (2 e 3 valores)
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

# Exemplo 10: pedir string e imprimir
color = input("What color is rose?: ")
print(color)

# Exemplo 11: pedir número inteiro
n = int(input("How many roses?: "))
print(n)

# Exemplo 12: pedir número decimal
price = float(input("Price of each rose?: "))
print(price)

# Exemplo 13: verificando tipos de várias variáveis
a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for": 2, "Geeks": 3}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# ------------------------------------------------------------
# EXPLICAÇÃO DO CÓDIGO (TODOS OS TRECHOS)
# ------------------------------------------------------------
# - Cada chamada input("mensagem"): exibe texto e aguarda entrada.
# - Atribuição: variável recebe uma string retornada.
# - print(): exibe texto e variáveis.
# - int()/float(): convertem a string em número.
# - split(): divide a entrada por espaços, gerando várias strings.
# - type(): retorna o tipo do valor analisado.
# - Os exemplos finais mostram diferentes tipos básicos de Python.

# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - input()
# - print()
# - Conversão de tipos: int(), float()
# - Múltiplas entradas com split()
# - Saída formatada com print()
# - Variáveis e atribuição
# - Tipos: str, int, float, tuple, list, dict
# - type()
# - Interação com o console
# - Entrada como string por padrão
# - Pausa do programa para entrada
# - Impressão de múltiplos valores
# - Exemplos com texto, números e coleções
