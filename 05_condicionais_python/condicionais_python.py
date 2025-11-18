"""
ASSUNTO PRINCIPAL DETECTADO: Instruções Condicionais em Python

Resumo geral do assunto:
Este conteúdo aborda as instruções condicionais em Python, usadas para controlar o fluxo de execução
de acordo com diferentes condições. São apresentadas formas simples e avançadas de decisões,
incluindo if, if abreviado, if-else, if-elif-else, condicionais aninhadas, expressões (ou operadores)
ternárias e o recurso match-case introduzido em versões recentes do Python.

Contexto no Python:
Python utiliza blocos de código baseados em indentação, o que torna as estruturas condicionais
claras e legíveis. As instruções condicionais permitem que programas tomem decisões dinâmicas com base
em valores, expressões e comparações.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL (INSTRUÇÕES CONDICIONAIS)
# ------------------------------------------------------------
# Instruções condicionais permitem executar diferentes blocos de código dependendo do valor
# de uma condição booleana (True ou False).
#
# Principais formas:
# - if: executa um bloco se a condição for verdadeira.
# - if (abreviado): versão compacta em uma única linha.
# - if-else: executa um bloco para verdadeiro e outro para falso.
# - if-elif-else: permite múltiplas condições encadeadas.
# - if aninhado: um if dentro de outro.
# - Expressão condicional (operador ternário): forma compacta de if-else em uma linha.
# - match-case: estrutura de decisão que compara padrões (similar ao switch-case de outras linguagens).
#
# Python usa indentação obrigatória; cada novo bloco deve ser identado corretamente.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# - Operadores de comparação (>=, <=, ==, !=, <, >) aparecem para criar condições.
# - Tipos booleanos (True, False) usados nas decisões.
# - Impressão com print() para demonstrar resultados.
# - F-strings foram usadas em um dos exemplos: f"Result: {res}"
# - Atribuição de valores a variáveis (age, marks, res etc.)
# - Estruturas de controle match-case foram citadas como versão Python de switch-case.
# - Conceito de "operador ternário": expressão condicional em uma linha.
#
# Esses itens são secundários, pois são ferramentas utilizadas dentro das condicionais.

# ------------------------------------------------------------
# EXEMPLOS (baseados no conteúdo enviado + complementos didáticos)
# ------------------------------------------------------------

# Exemplo 1: if simples
age = 20
if age >= 18:
    print("Eligible to vote.")  # Executa porque 20 >= 18

# Exemplo 2: if abreviado
age = 19
if age > 18: print("Eligible to Vote.")  # Executa em uma linha

# Exemplo 3: if-else
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

# Exemplo 4: if-else abreviado (operador ternário)
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")

# Exemplo 5: elif
age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# Exemplo 6: if aninhado
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# Exemplo 7: expressão condicional (ternária)
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

# Exemplo 8: match-case
number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")

# ------------------------------------------------------------
# EXPLICAÇÃO DO MEU CÓDIGO (LINHA POR LINHA)
# ------------------------------------------------------------
# age = 20 → cria variável com idade.
# if age >= 18: → verifica se a idade é maior ou igual a 18.
# print("Eligible to vote.") → imprime se a condição for verdadeira.
#
# if age > 18: print("Eligible to Vote.") → verifica e imprime em uma linha.
#
# age = 10 → variável age recebe 10.
# if age <= 12: → verifica condição.
# print("Travel for free.") → executa se verdadeiro.
# else: print("Pay for ticket.") → executa caso contrário.
#
# marks = 45 → nota do aluno.
# res = "Pass" if marks >= 40 else "Fail" → operador ternário.
# print(f"Result: {res}") → usa f-string para imprimir.
#
# A estrutura if-elif-else testa várias condições em sequência.
#
# No if aninhado, a segunda condição só é testada se a primeira for verdadeira.
#
# O match-case compara padrões, permitindo verificar diferentes valores para "number".

# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - Instruções condicionais
# - if
# - if abreviado
# - if-else
# - if-else abreviado
# - elif
# - if aninhado
# - Operador ternário (expressão condicional)
# - match-case
# - Operadores de comparação (>=, <=, >, <, ==, !=)
# - Booleanos (True, False)
# - Atribuição de variáveis
# - print()
# - f-strings
# - Estrutura de tomada de decisão baseada em padrões

