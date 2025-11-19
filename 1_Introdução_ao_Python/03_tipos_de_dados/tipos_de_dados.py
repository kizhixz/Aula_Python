"""
ASSUNTO PRINCIPAL DETECTADO: Tipos de dados em Python

Resumo geral do assunto:
Este documento aborda **todos os tipos de dados integrados do Python**, explicando
suas características, comportamento, exemplos, usos e particularidades.
Em Python, tudo é um objeto — logo, cada tipo de dado é uma classe,
e cada variável é uma instância (objeto) dessas classes.

Contexto:
Os tipos de dados determinam como valores são armazenados, manipulados
e quais operações podem ser realizadas sobre eles. Eles são essenciais para
o funcionamento da linguagem e aparecem em absolutamente qualquer programa Python.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL (Tipos de Dados em Python)
# ------------------------------------------------------------
# Python possui tipos de dados integrados (built-in), divididos em categorias:
#
# NUMÉRICOS:
#   - int: números inteiros, sem limite de tamanho.
#   - float: números reais com ponto flutuante.
#   - complex: números complexos no formato (a + bj).
#
# SEQUÊNCIAS:
#   - str (string): texto representado como sequência imutável de caracteres Unicode.
#   - list: coleção ordenada e mutável.
#   - tuple: coleção ordenada e imutável.
#
# MAPEAMENTO:
#   - dict: pares chave-valor.
#
# BOOLEANOS:
#   - bool: True ou False.
#
# CONJUNTOS:
#   - set: coleção não ordenada sem elementos duplicados.
#   - frozenset: versão imutável de set.
#
# BINÁRIOS:
#   - bytes, bytearray, memoryview.
#
# Cada tipo define:
#   - como o dado é armazenado,
#   - operações permitidas,
#   - comportamento em expressões e funções.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# - Indexação positiva e negativa em sequências.
# - Iteração sobre elementos (ex.: for em listas e sets).
# - Mutabilidade vs. imutabilidade.
# - Erros comuns: NameError ao usar palavras inexistentes ("true", "false").
# - Notação científica em floats.
# - Truthy e falsy (valores avaliados como True ou False).
# - Empacotamento de tuplas (tuple packing).
# - Remoção automática de duplicatas em sets.
# - Acesso de itens por índice (listas, tuplas, strings).
# - Acesso de itens por chave (dicionários).
# - Uso de .get() em dicionários.
# - Diferença entre lista e tupla.
# - Conjuntos não possuem acesso por índice.

# ------------------------------------------------------------
# EXEMPLOS — DO TEXTO E COMPLEMENTARES
# ------------------------------------------------------------

# Exemplos de atribuições mudando o tipo de x
x = 50          # int
x = 60.5        # float
x = "Hello"     # string
x = ["geeks", "for", "geeks"]   # list
x = ("geeks", "for", "geeks")   # tuple

# Exemplos numéricos
a = 5
print(type(a))  # <class 'int'>

b = 5.0
print(type(b))  # <class 'float'>

c = 2 + 4j
print(type(c))  # <class 'complex'>

# String
s = "Bem-vindo ao Mundo dos Geeks"
print(s)
print(type(s))
print(s[1])   # e
print(s[2])   # m
print(s[-1])  # último caractere

# Lista
a = [1, 2, 3]
print(a)

b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

lista = ["Geeks", "Para", "Geeks"]
print(lista[0])
print(lista[2])
print(lista[-1])
print(lista[-3])

# Tuplas
tup1 = ()
tup2 = ("Geeks", "Para")
print(tup2)

tup3 = (1, 2, 3, 4, 5)
print(tup3[0])
print(tup3[-1])
print(tup3[-3])

# Booleanos
print(type(True))
print(type(False))

# Truthy e falsy
if 1:
    print("1 é verdadeiro")

if not 0:
    print("0 é falso")

# Set
s1 = set("GeeksForGeeks")
print(s1)

s2 = set(["Geeks", "Para", "Geeks"])
print(s2)

set1 = set(["Geeks", "For", "Geeks"])
print(set1)

for i in set1:
    print(i, end=" ")

print("Geeks" in set1)

# Dicionário
d = {1: "Geeks", 2: "Para", 3: "Geeks"}
print(d)

d1 = dict({1: "Geeks", 2: "For", 3: "Geeks"})
print(d1)

d2 = {1: "Geeks", "nome": "Para", 3: "Geeks"}
print(d2["nome"])
print(d2.get(3))


# ------------------------------------------------------------
# EXPLICAÇÃO DO CÓDIGO — LINHA POR LINHA
# ------------------------------------------------------------
# Cada trecho acima demonstra a criação, inspeção e manipulação de diferentes tipos.
# As chamadas a type() mostram a classe do objeto criado.
# Os exemplos de string e lista demonstram indexação positiva e negativa.
# Tuplas são mostradas como imutáveis, com acesso por índice.
# Booleanos evidenciam como Python trata valores verdadeiros e falsos.
# Sets demonstram remoção automática de duplicatas e ausência de ordem.
# Dicionários mostram armazenamento em pares chave-valor e recuperação por chave.

# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - int, float, complex
# - str
# - list
# - tuple
# - dict
# - set
# - frozenset (mencionado na teoria padrão)
# - bytes, bytearray, memoryview (mencionados)
# - indexação positiva
# - indexação negativa
# - mutabilidade
# - imutabilidade
# - truthy / falsy
# - NameError
# - notação científica em float
# - iteração com for
# - operador "in"
# - tupla com um único elemento requer vírgula
# - empacotamento de tuplas
# - duplicatas removidas em set
# - .get() em dicionário
# - acesso por chave em dict
# - acesso por índice (str, list, tuple)
