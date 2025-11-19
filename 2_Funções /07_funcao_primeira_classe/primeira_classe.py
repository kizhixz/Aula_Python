"""
ASSUNTO PRINCIPAL DETECTADO: Funções de primeira classe em Python

Resumo geral do assunto.
Este arquivo apresenta o conceito de funções de primeira classe em Python, mostrando
como funções podem ser tratadas como objetos comuns: atribuídas a variáveis, passadas
como argumentos, retornadas de outras funções e armazenadas em estruturas de dados.

Contexto sobre o que esse tema significa no Python.
Em Python, funções são objetos como qualquer outro. Isso permite criar código modular,
flexível e altamente reutilizável, possibilitando padrões como funções de ordem superior,
fábricas de funções e composição funcional.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL
# ------------------------------------------------------------
# Funções de primeira classe são funções tratadas como valores.
# Em Python, isso significa que funções podem:
# - Ser atribuídas a variáveis.
# - Ser passadas como argumentos para outras funções.
# - Ser retornadas de funções.
# - Ser armazenadas em listas, dicionários ou outras estruturas.
#
# Isso permite criar funções de ordem superior (funções que recebem ou retornam funções),
# aplicar padrões funcionais e escrever código mais limpo e reutilizável.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# O conteúdo também inclui:
# - Uso de print()
# - Funções internas (funções definidas dentro de outras)
# - Dicionários como armazenamento de funções
# - Retorno de strings formatadas (f-strings)
# - Operações matemáticas simples (adição e subtração)
#
# Esses itens não são o tema principal, mas aparecem no texto e são explicados aqui.

# ------------------------------------------------------------
# EXEMPLOS (inclui seus exemplos + exemplos novos)
# ------------------------------------------------------------

# 1. Atribuição de funções a variáveis
def msg(name):
    return f"Hello, {name}!"

# Assigning function to a variable
f = msg

print(f("Emma"))  # Exemplo funcionando
# Explicação: a variável f agora referencia a função msg.


# 2. Passando funções como argumentos
def fun1(fun2, name):
    return fun2(name)

print(fun1(msg, "Alex"))
# Explicação: fun1 recebe outra função como argumento e a executa.


# 3. Retornando funções
def fun1_return(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2

func = fun1_return("Hello, World!")
print(func())
# Explicação: fun1_return retorna a função fun2, que usa a variável msg.


# 4. Armazenando funções em estruturas de dados
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

d = {
    "add": add,
    "subtract": subtract
}

print(d["add"](5, 3))
print(d["subtract"](5, 3))
# Explicação: funções armazenadas em dicionário e chamadas por chave.


# ------------------------------------------------------------
# EXPLICAÇÃO DO MEU CÓDIGO (LINHA POR LINHA)
# ------------------------------------------------------------
# def msg(name):                 -> Define uma função que recebe um nome e retorna uma saudação.
# f = msg                        -> Atribui a função msg à variável f.
# print(f("Emma"))               -> Chama msg usando f como referência.
#
# def fun1(fun2, name):          -> Função que recebe outra função e um nome.
# return fun2(name)              -> Executa a função recebida.
# print(fun1(msg, "Alex"))       -> Passa msg como argumento.
#
# def fun1_return(msg):          -> Função que cria outra função interna.
# def fun2():                    -> Função interna que usa msg.
# return fun2                    -> Retorna a função interna.
# func = fun1_return("Hello")    -> Armazena a função retornada.
# print(func())                  -> Executa a função interna.
#
# def add(x, y), def subtract:   -> Funções matemáticas.
# d = {"add": add, ...}          -> Dicionário armazenando funções.
# d["add"](5, 3)                 -> Executa a função usando a chave do dicionário.


# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - Funções de primeira classe
# - Atribuição de funções a variáveis
# - Passar funções como argumentos
# - Retornar funções
# - Funções internas
# - Funções de ordem superior
# - Armazenamento de funções em dicionários
# - Uso de f-strings
# - print()
# - Operações matemáticas simples (adição, subtração)
