"""
ASSUNTO PRINCIPAL DETECTADO: *args e **kwargs em Python

*args e **kwargs permitem criar funções que recebem quantidade variável de argumentos.
- *args → coleta argumentos posicionais em uma tupla.
- **kwargs → coleta argumentos nomeados em um dicionário.

O conteúdo enviado cobre:
- uso de *args para somar valores, iterar e multiplicar,
- uso de **kwargs para imprimir pares chave-valor e montar strings formatadas,
- combinações de *args e **kwargs na mesma função,
- explicações passo a passo de cada exemplo.

Todo o conteúdo foi preservado, organizado e documentado.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL
# ------------------------------------------------------------
# *args e **kwargs servem para criar funções flexíveis em Python:
#
# 1. *args  → argumentos posicionais variáveis (empacotados em uma tupla).
# 2. **kwargs → argumentos nomeados variáveis (empacotados em um dicionário).
#
# Quando usar:
# - quando o número de argumentos é desconhecido,
# - quando a função deve aceitar entradas dinâmicas,
# - quando se quer permitir parametrização flexível.
#
# Notação:
# - * é um operador de desempacotamento.
# - args e kwargs são nomes convencionais; poderiam ter outros nomes.
#
# A função pode receber *args e **kwargs juntos, desde que nessa ordem:
#     def f(*args, **kwargs):
#         ...
#
# Isso garante que Python processe corretamente argumentos posicionais e nomeados.

# ------------------------------------------------------------
# EXEMPLOS — TODOS DO SEU TEXTO
# ------------------------------------------------------------

# EXEMPLO 1 — *args somando vários argumentos
def fun(*args):
    return sum(args)

print(fun(5, 10, 15))  # Saída: 30


# EXEMPLO 2 — **kwargs imprimindo pares chave–valor
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)  
# Saída:
# a 1
# b 2
# c 3


# EXEMPLO 3 — *args iterando sobre argumentos
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Olá', 'Bem-vindo', 'ao', 'GeeksforGeeks')
# Saída:
# Olá
# Bem-vindo
# ao
# GeeksforGeeks


# EXEMPLO 4 — *args multiplicando vários valores
def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

print(multiplicar(2, 3, 4))  # Saída: 24


# EXEMPLO 5 — **kwargs formatando chave: valor
def introduzir(**kwargs):
    detalhes = []
    for k, v in kwargs.items():
        detalhes.append(k + ": " + str(v))
    return ", ".join(detalhes)

print(introduzir(Nome="Alice", Idade=25, Cidade="Nova York"))
# Saída:
# Nome: Alice, Idade: 25, Cidade: Nova York


# EXEMPLO 6 — combinando *args e **kwargs
def student_info(*args, **kwargs):
    print("Assuntos:", args)
    print("Detalhes:", kwargs)

student_info(
    "Matemática",
    "Ciências",
    "Inglês",
    Nome="Alice",
    Idade=20,
    Cidade="Nova York"
)
# Saída:
# Assuntos: ('Matemática', 'Ciências', 'Inglês')
# Detalhes: {'Nome': 'Alice', 'Idade': 20, 'Cidade': 'Nova York'}


# ------------------------------------------------------------
# RESUMO TÉCNICO — TUDO QUE REALMENTE APARECEU NO SEU TEXTO
# ------------------------------------------------------------
# - *args
# - **kwargs
# - argumentos posicionais variáveis
# - argumentos nomeados variáveis
# - tuplas como estrutura de armazenamento de *args
# - dicionários como estrutura de armazenamento de **kwargs
# - funções com quantidade dinâmica de argumentos
# - soma usando *args
# - iteração sobre *args
# - multiplicação usando *args
# - formatação chave:valor via **kwargs
# - kwargs.items()
# - combinação *args + **kwargs
# - criação de funções flexíveis
# - operador de desempacotamento (* e **)
