"""
ASSUNTO PRINCIPAL DETECTADO: Funções lambda em Python

Resumo geral do assunto.
Este arquivo apresenta o uso de funções lambda em Python, destacando como elas funcionam,
suas limitações, seus casos de uso mais comuns e como comparar lambda com funções criadas
com `def`.

Contexto sobre o que esse tema significa no Python.
Funções lambda são funções anônimas, curtas e de expressão única, úteis para situações
onde uma função rápida é suficiente — especialmente quando usadas com map(), filter(),
reduce() ou compreensões. Elas fazem parte do paradigma funcional disponível em Python.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL
# ------------------------------------------------------------
# Funções lambda:
# - São funções pequenas e anônimas.
# - Possuem apenas uma expressão.
# - São úteis para operações rápidas e temporárias.
#
# Sintaxe:
#   lambda argumentos: expressão
#
# Características:
# - Não podem conter múltiplas instruções.
# - Não suportam docstrings.
# - Geralmente usadas como função inline em transformações ou filtragens.
#
# Casos apresentados no conteúdo:
# 1. Compreensão de lista + lambda
# 2. Lambda retornando múltiplos valores (tupla)
# 3. Uso com filter()
# 4. Uso com map()
# 5. Uso com reduce()
# 6. Comparação lambda vs def

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# O texto também inclui:
# - List comprehensions
# - Uso de listas
# - Uso de tuplas como retorno
# - Módulo functools
# - Comparação entre def e lambda
# - Operações matemáticas simples (adição, multiplicação, produto total)
# - Tabelas comparativas conceituais
# - print()
#
# Esses temas não são o foco principal, mas aparecem no conteúdo e são documentados aqui.

# ------------------------------------------------------------
# EXEMPLOS (inclui seus exemplos + exemplos novos)
# ------------------------------------------------------------

# 1. Lambda dentro de compreensão de lista
li = [1, 2, 3, 4]
result = [lambda x: x * 10 for _ in li]     # lista de funções
# Para aplicar corretamente:
processed = [x * 10 for x in li]

print(10)
print(20)
print(30)
print(40)
# Explicação: cada elemento foi multiplicado por 10.


# 2. Lambda retornando múltiplos resultados
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)
# Explicação: retorna tupla contendo soma e produto.


# 3. Usando lambda com filter()
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))
# Explicação: mantém apenas os números pares.


# 4. Usando lambda com map()
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))
# Explicação: duplica cada número.


# 5. Usando lambda com reduce()
from functools import reduce
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)
# Explicação: calcula o produto de todos os elementos.


# 6. Comparação entre lambda e def
sq = lambda x: x ** 2
print(sq(3))

def sqdef(x):
    return x ** 2

print(sqdef(3))
# Explicação: ambos retornam o quadrado do número.

# ------------------------------------------------------------
# EXPLICAÇÃO DO MEU CÓDIGO (LINHA POR LINHA)
# ------------------------------------------------------------
# li = [1,2,3,4]                    -> Lista base.
# processed = [...]                 -> Aplica multiplicação por 10.
# print(...)                        -> Exibe saídas de exemplo.
#
# calc = lambda x,y: (...)          -> Lambda que retorna tupla (soma, produto).
# res = calc(3,4)                   -> Executa a função lambda.
#
# even = filter(lambda..., n)       -> Filtra apenas números pares.
# list(even)                        -> Converte o filtro em lista.
#
# b = map(lambda..., a)             -> Aplica transformação em cada item.
#
# reduce(lambda..., a)              -> Aplica redução multiplicativa.
#
# sq = lambda x: x**2               -> Quadrado via lambda.
# def sqdef(x): return x**2         -> Quadrado via função normal.
#
# Ambos exibem o mesmo resultado.


# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - lambda
# - sintaxe lambda
# - funções anônimas
# - limitações (uma expressão, sem docstring)
# - compreensão de listas
# - retorno de tuplas
# - filter()
# - map()
# - reduce()
# - módulo functools
# - operações matemáticas com lambda
# - comparação lambda vs def
# - uso de listas
# - uso de print()
