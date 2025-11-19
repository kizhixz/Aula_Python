"""
ASSUNTO PRINCIPAL DETECTADO: Operadores em Python

Resumo geral do assunto:
Operadores em Python são símbolos especiais usados para realizar operações sobre valores
e variáveis. Eles permitem que o programa execute cálculos, comparações, combine condições,
manipule bits, verifique identidade e pertinência, atribua valores e até escreva decisões
condicionais em uma única linha (operador ternário).

Contexto:
No Python, operadores são fundamentais para qualquer lógica de programação. Muitos deles
funcionam sobre tipos específicos (como números ou sequências), enquanto outros podem ser
usados genericamente em diversos contextos. Eles seguem regras de precedência e
associatividade, que determinam a ordem de avaliação dentro de expressões complexas.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL (OPERADORES EM PYTHON)
# ------------------------------------------------------------
# Operadores são símbolos que instruem Python a realizar uma operação.
# Os operandos são os valores sobre os quais esses operadores atuam.
#
# TIPOS DE OPERADORES ABORDADOS NO CONTEÚDO:
# 1. Operadores aritméticos
#    +, -, *, /, //, %, **
#
# 2. Operadores de comparação
#    >, <, ==, !=, >=, <=
#
# 3. Operadores lógicos
#    and, or, not
#
# 4. Operadores bit a bit
#    &, |, ~, ^, >>, <<
#
# 5. Operadores de atribuição
#    =, +=, -=, *=, <<=, etc.
#
# 6. Operadores de identidade
#    is, is not
#
# 7. Operadores de pertinência
#    in, not in
#
# 8. Operador ternário (condicional simples)
#    <valor_se_verdadeiro> if <condicao> else <valor_se_falso>
#
# 9. Precedência e associatividade de operadores
#    Determinam a ordem em que operações são avaliadas.
#
# Esses elementos constituem o núcleo da lógica computacional em Python.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# - Uso de variáveis como operandos.
# - Sequências (listas) aparecem no contexto dos operadores "in" e "not in".
# - Contextos booleanos True/False aparecem quando os operadores retornam valores lógicos.
# - Estruturas condicionais (if/else) aparecem em exemplos sobre precedência.
# - A distinção entre Python 2.x e Python 3.x foi citada na explicação da divisão.

# ------------------------------------------------------------
# EXEMPLOS (COM BASE NO CONTEÚDO + EXPLICAÇÕES)
# ------------------------------------------------------------

# ---------- Operadores Aritméticos ----------
a = 15
b = 4

print("Adição:", a + b)         # soma os dois valores
print("Subtração:", a - b)      # subtrai b de a
print("Multiplicação:", a * b)  # multiplica a por b
print("Divisão:", a / b)        # divisão sempre retorna float em Python 3.x
print("Divisão do andar:", a // b)  # divisão inteira (descarta parte decimal)
print("Módulo:", a % b)         # resto da divisão
print("Exponenciação:", a ** b) # a elevado à potência b

# ---------- Operadores de Comparação ----------
a = 13
b = 33
print(a > b)   # maior que
print(a < b)   # menor que
print(a == b)  # igual
print(a != b)  # diferente
print(a >= b)  # maior ou igual
print(a <= b)  # menor ou igual

# ---------- Operadores Lógicos ----------
a = True
b = False
print(a and b)   # só True se ambos forem True
print(a or b)    # True se qualquer um for True
print(not a)     # inverte o valor booleano

# ---------- Operadores Bit a Bit ----------
a = 10
b = 4
print(a & b)     # AND bit a bit
print(a | b)     # OR bit a bit
print(~a)        # NOT bit a bit (complemento)
print(a ^ b)     # XOR bit a bit
print(a >> 2)    # desloca bits para a direita
print(a << 2)    # desloca bits para a esquerda

# ---------- Operadores de Atribuição ----------
a = 10
b = a       # atribuição simples
print(b)

b += a      # b = b + a
print(b)

b -= a      # b = b - a
print(b)

b *= a      # b = b * a
print(b)

b <<= a     # deslocamento binário com atribuição
print(b)

# ---------- Operadores de Identidade ----------
a = 10
b = 20
c = a
print(a is not b)  # verifica se NÃO ocupam a mesma área de memória
print(a is c)      # verifica se são o mesmo objeto

# ---------- Operadores de Pertinência ----------
x = 24
y = 20
lista = [10, 20, 30, 40, 50]

if x not in lista:
    print("x NÃO está presente na lista fornecida")
else:
    print("x está presente na lista fornecida")

if y in lista:
    print("y está presente na lista fornecida")
else:
    print("y NÃO está presente na lista fornecida")

# ---------- Operador Ternário ----------
a, b = 10, 20
minimo = a if a < b else b
print(minimo)

# ---------- Precedência ----------
expr = 10 + 20 * 30         # multiplicação ocorre antes da adição
print(expr)

nome = "Alex"
idade = 0
if nome == "Alex" or nome == "John" and idade >= 2:
    print("Olá! Bem-vindo(a).")
else:
    print("Adeus!!")

# ---------- Associatividade ----------
print(100 / 10 * 10)     # avaliado da esquerda para direita
print(5 - 2 + 3)         # associatividade esquerda
print(5 - (2 + 3))       # uso de parênteses altera a ordem
print(2 ** 3 ** 2)       # exponenciação é associativa à direita

# ------------------------------------------------------------
# EXPLICAÇÃO DO MEU CÓDIGO (LINHA POR LINHA)
# ------------------------------------------------------------
# Cada bloco acima reproduz e demonstra o comportamento dos operadores segundo os exemplos enviados.
# Todas as linhas seguem exatamente o propósito original:
# - demostrar resultados
# - exibir valores
# - testar condições
# - verificar identidade
# - testar pertinência
# - mostrar regras de precedência
#
# Nada foi alterado conceitualmente — apenas organizado e comentado.

# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - Operadores aritméticos (+, -, *, /, //, %, **)
# - Operadores de comparação (> < == != >= <=)
# - Operadores lógicos (and, or, not)
# - Operadores bit a bit (& | ~ ^ >> <<)
# - Operadores de atribuição (= += -= *= <<=)
# - Operadores de identidade (is, is not)
# - Operadores de pertinência (in, not in)
# - Operador ternário (x if condição else y)
# - Precedência de operadores
# - Associatividade
# - Uso de variáveis como operandos
# - Avaliação booleana
# - Uso de listas em testes de pertinência
# - Estruturas condicionais (if/else)
# - Diferença entre divisão no Python 2.x e 3.x
