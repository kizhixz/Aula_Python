"""
ASSUNTO PRINCIPAL DETECTADO: Laços em Python (for, while e laços aninhados)

Resumo geral do assunto:
Este conteúdo apresenta todos os fundamentos essenciais sobre laços de repetição em Python.
Mostra como usar for, while, loops aninhados e instruções de controle de fluxo (break, continue, pass).
Inclui exemplos iterando sequências, strings, dicionários, sets, índices e loops infinitos.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL (LAÇOS DE REPETIÇÃO EM PYTHON)
# ------------------------------------------------------------
# Em Python, laços são usados para executar blocos de código repetidamente.
#
# Tipos principais:
# - for: itera sobre sequências (listas, tuplas, strings, ranges, dicionários, sets).
# - while: repete enquanto uma condição for verdadeira.
# - laços aninhados: loops dentro de loops.
#
# Instruções de controle:
# - continue: pula a iteração atual.
# - break: encerra o loop.
# - pass: placeholder para um bloco vazio.
#
# Python é altamente legível graças ao uso de indentação para definir blocos.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO QUE APARECE NO TEXTO
# ------------------------------------------------------------
# - range()
# - len()
# - Iteração sobre listas, tuplas, strings, dicionários e sets
# - Iteração baseada em índices
# - Laços infinitos com while True
# - print() com end=' ' para impressão na mesma linha
# - Import para compatibilidade de print no Python 2 (from __future__ import print_function)
# - Variáveis contadoras e incremento manual (cnt = cnt + 1)

# ------------------------------------------------------------
# EXEMPLOS (baseados no texto enviado)
# ------------------------------------------------------------

# Exemplo 1: for com range()
n = 4
for i in range(0, n):
    print(i)  # 0 → 3

# Exemplo 2: iterando sobre diferentes tipos de sequências
li = ["geeks", "for", "geeks"]
for x in li:
    print(x)

tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)

s = "abc"
for x in s:
    print(x)

d = dict({'x': 123, 'y': 354})
for x in d:
    print("%s  %d" % (x, d[x]))

set1 = {10, 30, 20}
for x in set1:
    print(x)

# Exemplo 3: iterando usando índices
li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])

# Exemplo 4: while simples
cnt = 0
while cnt < 3:
    cnt = cnt + 1
    print("Hello Geek")

# Exemplo 5: laço infinito (não executar na prática!)
# while True:
#     print("Hello Geek")   # loop infinito

# Exemplo 6: laços aninhados
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

# Exemplo 7: continue
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

# Exemplo 8: break
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
print('Current Letter :', letter)

# Exemplo 9: pass
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

# ------------------------------------------------------------
# EXPLICAÇÃO DO MEU CÓDIGO — LINHA A LINHA (RESUMO)
# ------------------------------------------------------------
# - for i in range(0, n):         → cria uma sequência de 0 a n-1 e itera sobre ela.
# - for x in li:                  → percorre uma lista, elemento por elemento.
# - for x in s:                   → percorre caracteres de uma string.
# - for x in d:                   → percorre chaves de um dicionário.
# - for index in range(len(li)):  → iteração baseada em índices.
#
# While:
# - while cnt < 3:                → repete enquanto a condição for verdadeira.
# - cnt = cnt + 1                 → necessário para evitar loop infinito.
#
# Laços aninhados:
# - for j in range(i):            → repete i vezes dentro do loop externo.
#
# continue:
# - pula a iteração atual quando a condição é verdadeira.
#
# break:
# - interrompe o loop imediatamente.
#
# pass:
# - não faz nada; placeholder para código futuro.
#

# ------------------------------------------------------------
# RESUMO TÉCNICO — TUDO QUE APARECEU NO TEXTO
# ------------------------------------------------------------
# - for
# - range()
# - iterar listas
# - iterar tuplas
# - iterar strings
# - iterar dicionários
# - iterar sets
# - len()
# - for por índice
# - while
# - while True (loop infinito)
# - incremento manual
# - laços aninhados
# - print() com end=
# - continue
# - break
# - pass
# - conceito de que loops podem conter loops de qualquer tipo

