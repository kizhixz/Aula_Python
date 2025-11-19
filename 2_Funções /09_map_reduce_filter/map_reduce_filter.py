"""
ASSUNTO PRINCIPAL DETECTADO: Função map() em Python

Resumo geral do assunto.
A função map() aplica uma função a cada elemento de um ou mais iteráveis, retornando um iterador.
É usada para transformações uniformes, criando código conciso, eficiente e funcional.

Contexto no Python:
map() é uma função de ordem superior, muito útil para processamento em lote de dados,
substituindo loops explícitos em diversos casos.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL: FUNÇÃO map()
# ------------------------------------------------------------
# A função map() aplica uma função a cada elemento de um iterável.
# Retorna um objeto do tipo map, que é um iterador.
# Pode receber um ou mais iteráveis.
# Pode utilizar funções definidas, métodos internos (como str.upper)
# ou funções lambda.
# Frequentemente é convertida em lista com list(map(...)).

# Sintaxe:
#   map(funcao, iteravel1, iteravel2, ...)
# - funcao: função que recebe os elementos dos iteráveis.
# - iteráveis: listas, tuplas, sets, etc.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# - Função int() usada para conversão de strings para inteiros.
# - Funções personalizadas (double()).
# - Funções lambda.
# - Métodos de string como str.upper e str.strip.
# - Operação de indexação (s[0]).
# - Conversão de temperatura Celsius → Fahrenheit.

# ------------------------------------------------------------
# EXEMPLOS
# ------------------------------------------------------------

# Exemplo 1: Convertendo lista de strings para inteiros
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))  # [1, 2, 3, 4]
# Explicação: int() é aplicado a cada string da lista.


# Exemplo 2: map() com função personalizada
def double(val):
    return val * 2

a = [1, 2, 3, 4]
res = list(map(double, a))
print(res)  # [2, 4, 6, 8]
# Explicação: a função double() é aplicada a cada número.


# Exemplo 3: map() com lambda
res = list(map(lambda x: x ** 2, a))
print(res)  # [1, 4, 9, 16]
# Explicação: eleva cada valor ao quadrado.


# Exemplo 4: map() com múltiplos iteráveis
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))  # [5, 7, 9]
# Explicação: soma elementos correspondentes.


# Exemplo 5: Converter strings para maiúsculas
frutas = ['maçã', 'banana', 'cereja']
res = map(str.upper, frutas)
print(list(res))  # ['MAÇÃ', 'BANANA', 'CEREJA']
# Explicação: aplica upper() em cada string.


# Exemplo 6: Extrair o primeiro caractere de cada string
palavras = ['maçã', 'banana', 'cereja']
res = map(lambda s: s[0], palavras)
print(list(res))  # ['m', 'b', 'c']
# Explicação: pega s[0] de cada item.


# Exemplo 7: Remover espaços em branco
s = [' olá ', ' mundo ', ' python ']
res = map(str.strip, s)
print(list(res))  # ['olá', 'mundo', 'python']
# Explicação: strip remove espaços extras.


# Exemplo 8: Converter Celsius para Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))  # [32.0, 68.0, 98.6, 212.0]
# Explicação: aplica fórmula de conversão.


# ------------------------------------------------------------
# EXPLICAÇÃO DO CÓDIGO LINHA POR LINHA (GERAL)
# ------------------------------------------------------------
# Cada bloco cria uma lista/iterável → aplica map() → converte com list() → imprime.
# Quando funções personalizadas são usadas, elas são definidas antes do map().
# Em uso com vários iteráveis, map() itera até o menor deles.
# Métodos como str.upper e str.strip são passados diretamente sem parênteses.


# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - Função map()
# - Iteradores
# - list()
# - int()
# - Funções personalizadas (double)
# - lambda
# - str.upper
# - str.strip
# - Indexação s[0]
# - Operações matemáticas (x**2, soma, fórmula Fahrenheit)
# - Múltiplos iteráveis no map()
# - Conversões de tipo
