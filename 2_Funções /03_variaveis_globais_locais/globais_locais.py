"""
ASSUNTO PRINCIPAL DETECTADO: Variáveis globais e locais em Python

Este arquivo documenta detalhadamente o comportamento de variáveis globais e locais
em Python, incluindo como são acessadas, como a palavra-chave `global` afeta o escopo
e como funções tratam variáveis com o mesmo nome em escopos distintos.

O conteúdo explica:
- como acessar variáveis globais dentro e fora de funções,
- como variáveis locais podem ocultar variáveis globais,
- o erro gerado ao tentar modificar globais sem usar `global`,
- como modificar corretamente valores globais,
- comparação clara entre variáveis globais e locais.

Todo o conteúdo enviado foi preservado e documentado.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL (VARIÁVEIS GLOBAIS E LOCAIS)
# ------------------------------------------------------------
# - Uma variável global é declarada fora de funções.
# - Uma variável local é declarada dentro de uma função.
# - Variáveis globais podem ser acessadas dentro de funções, desde que não sejam modificadas.
# - Se uma variável local tem o mesmo nome de uma variável global, a variável local SOMBRA a global.
# - Para modificar uma variável global dentro de uma função, é obrigatório usar a palavra-chave `global`.
# - Se tentar modificar uma variável global sem usar `global`, ocorre um UnboundLocalError.
# - O Python procura variáveis primeiro no escopo local; se não encontrar, procura no escopo global.
# - Uma variável global permanece acessível por todo o programa; uma variável local vive apenas enquanto a função executa.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# - Uso da palavra-chave `global`.
# - UnboundLocalError gerado ao tentar modificar uma variável assumida como local.
# - Comparação tabular entre variável global e variável local:
#       * definição,
#       * vida útil,
#       * compartilhamento,
#       * escopo,
#       * parâmetros,
#       * armazenamento,
#       * impacto das alterações.
# - Demonstração de sombreamento de nome (shadowing).
# - Impressões usando print(), pois apareceram nos exemplos.
# - Múltiplos exemplos de funções simples (display, fun, f, g, h).

# ------------------------------------------------------------
# EXEMPLOS (INCLUINDO OS DO CONTEÚDO + EXEMPLOS MANTIDOS FIEIS)
# ------------------------------------------------------------

# Exemplo 1 – Acessando variável global dentro e fora da função
msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)

# Exemplo 2 – Variável local escondendo variável global
def fun():
    s = "Me too."
    print(s)

s = "I love Geeksforgeeks"
fun()
print(s)

# Exemplo 3 – Tentativa de modificar global sem usar global → erro
# Este código gera UnboundLocalError
# def fun():
#     s += ' GFG'   # Python assumes s is local before assignment
#     print(s)
#
# s = "I love GeeksforGeeks"
# fun()

# Exemplo 4 – Modificando variável global corretamente
s = "Python is great!"

def fun():
    global s
    s += " GFG"
    print(s)
    s = "Look for GeeksforGeeks Python Section"
    print(s)

fun()
print(s)

# Exemplo 5 – Global vs Local com mesmo nome
a = 1  # Global variable

def f():
    print("f():", a)

def g():
    a = 2  # Local shadows global
    print("g():", a)

def h():
    global a
    a = 3
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)

# ------------------------------------------------------------
# EXPLICAÇÃO LINHA POR LINHA DO CÓDIGO DO USUÁRIO
# ------------------------------------------------------------

# msg = "Python is awesome!"
#   Cria uma variável global chamada msg.

# def display():
#     print("Inside function:", msg)
#   Função que acessa msg (global) e a imprime.

# display()
#   Chama a função e imprime o valor global.

# print("Outside function:", msg)
#   Imprime novamente a variável global.

# def fun():
#     s = "Me too."
#     print(s)
#   Dentro desta função, s é local e oculta s global.

# s = "I love Geeksforgeeks"
#   Variável global s criada.

# fun()
#   Usa s local.

# print(s)
#   Imprime s global, não alterada.

# O exemplo sem global gera erro porque Python interpreta s como local
# e tenta modificá-la antes de atribuir valor local → UnboundLocalError.

# No exemplo com global:
# global s
#   Diz ao Python para usar a variável global.
#
# s += " GFG"
#   Modifica a variável global.
#
# s = "Look for GeeksforGeeks Python Section"
#   Reatribui totalmente a variável global.

# No exemplo com f(), g(), h():
# - f() apenas lê a variável global a.
# - g() cria uma variável local a e oculta a global.
# - h() usa global a e modifica a global.


