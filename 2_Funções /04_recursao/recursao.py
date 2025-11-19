"""
ASSUNTO PRINCIPAL DETECTADO: Recursão em Python

A recursão é uma técnica de programação em que uma função chama a si mesma
para resolver problemas dividindo-os em subproblemas menores. Em Python,
recursão é usada em cálculos matemáticos (fatorial, Fibonacci), percursos de
árvores e algoritmos de divisão e conquista.

Este documento cobre:
- funcionamento da recursão,
- caso base e caso recursivo,
- exemplos práticos (fatorial, Fibonacci),
- recursão de cauda vs. não-cauda,
- comparação entre recursão e iteração,
- quando evitar recursão.

Todo o conteúdo enviado foi preservado, separado e documentado.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL (RECURSÃO EM PYTHON)
# ------------------------------------------------------------
# A recursão ocorre quando uma função chama a si mesma direta ou indiretamente.
# Toda função recursiva contém dois elementos fundamentais:
#
# 1. Caso base:
#    - É a condição que encerra as chamadas recursivas.
#    - Evita loops infinitos.
#
# 2. Caso recursivo:
#    - A parte da função que chama a si mesma, geralmente reduzindo o problema.
#
# A recursão funciona bem para problemas naturalmente subdivisíveis:
# - fatorial,
# - sequência de Fibonacci,
# - percursos em árvores,
# - algoritmos de divisão e conquista.
#
# Python mantém um limite de profundidade recursiva. Recursões profundas demais
# podem gerar RecursionError.
#
# Recursão de cauda:
# - A chamada recursiva é a ÚLTIMA operação.
# - Algumas linguagens otimizam (TCO), mas Python NÃO faz otimização de cauda.
#
# Recursão não-cauda:
# - Há trabalho após a chamada recursiva (multiplicações, somas etc.).
# - Não pode ser otimizada.
#
# Comparação recursão x iteração:
# - Recursão tende a ser mais intuitiva para problemas naturalmente recursivos.
# - Iteração é mais eficiente em memória e desempenho na maioria dos casos.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# - Uso de estruturas condicionais (se, senão, outro).
# - Impressão de valores usando print().
# - Demonstração de fatorial e Fibonacci.
# - Diferença entre laços iterativos e chamadas recursivas.
# - Cuidado com estouro de pilha (stack overflow) devido à profundidade recursiva.
# - Conceito de acumulador em recursão de cauda.
# - Exemplos completos com saídas demonstradas.

# ------------------------------------------------------------
# EXEMPLOS — TODOS OS DO CONTEÚDO FORAM MANTIDOS
# ------------------------------------------------------------

# Exemplo 1 — Fatorial Recursivo

def fatorial(n):
    if n == 0:  # Caso base
        return 1
    else:  # Caso recursivo
        return n * fatorial(n - 1)

print(fatorial(5))  # Saída: 120


# Exemplo 2 — Fibonacci Recursivo

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:  # Caso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Saída: 55


# Exemplo 3 — Recursão de cauda (não otimizada em Python)

def tail_fact(n, acc=1):
    # Caso base
    if n == 0:
        return acc
    else:
        # Recursão de cauda: chamada recursiva é a ÚLTIMA operação
        return tail_fact(n - 1, acc * n)

def nontail_fact(n):
    # Caso base
    if n == 1:
        return 1
    else:
        # Recursão NÃO de cauda: há trabalho após a chamada
        return n * nontail_fact(n - 1)

print(tail_fact(5))       # 120
print(nontail_fact(5))    # 120


# ------------------------------------------------------------
# EXPLICAÇÃO LINHA POR LINHA DO CONTEÚDO ENVIADO
# ------------------------------------------------------------

# def fatorial(n):
#     Se n == 0: caso base.
#     return 1: encerra a recursão.
#     Caso recursivo: n * fatorial(n - 1).

# print(fatorial(5)):
#     Chama a função repetidamente até atingir o caso base.

# def fibonacci(n):
#     Casos base: n == 0 → 0; n == 1 → 1.
#     Caso recursivo: soma das duas chamadas anteriores.

# print(fibonacci(10)):
#     Calcula o 10º número da sequência Fibonacci.

# tail_fact(n, acc):
#     Implementa recursão de cauda com acumulador.
#
# nontail_fact(n):
#     Implementa recursão comum com trabalho após a chamada recursiva.

# Comparação recursão vs iteração:
# - Recursão usa chamadas sobre a pilha.
# - Iteração usa laços (for/while).
# - Iteração tende a ser mais eficiente em Python.

# Quando evitar recursão:
# - Se a solução iterativa é simples.
# - Se a profundidade recursiva será muito grande.
# - Se o desempenho é crítico.


