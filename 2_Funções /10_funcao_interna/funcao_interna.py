"""
ASSUNTO PRINCIPAL DETECTADO: Funções internas (funções aninhadas) em Python

Resumo geral do assunto:
Funções internas são funções definidas dentro de outras funções. Elas permitem encapsulamento,
organização de código, acesso a variáveis externas, criação de closures e implementação de decoradores.

Contexto no Python:
São fundamentais para padrões funcionais, lógica auxiliar protegida, wrappers e comportamentos
persistentes através de closures.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL: FUNÇÕES INTERNAS (ANINHADAS)
# ------------------------------------------------------------
# Uma função interna é definida dentro de outra função.
# Usos principais:
# - Encapsulamento: esconder detalhes internos.
# - Organização: separar lógica auxiliar.
# - Acessar variáveis externas: segue a regra LEGB.
# - Suporte a closures e decoradores.
# Funções internas podem acessar variáveis da função externa.
# Para modificar variáveis externas é necessário usar "nonlocal".

# Closure:
# Quando a função interna armazena valores da função externa mesmo após seu término.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# - LEGB (Local, Enclosing, Global, Built-in)
# - Palavra-chave nonlocal
# - Decoradores e wrappers
# - *args e **kwargs
# - logging e registro de logs
# - Métodos de string como strip()

# ------------------------------------------------------------
# EXEMPLOS
# ------------------------------------------------------------

# Exemplo 1: Função interna simples

def fun1(msg):  # função externa
    def fun2():  # função interna
        print(msg)  # acessa variável do escopo externo
    fun2()

fun1("Olá")  # saída: Olá


# Exemplo 2: Acesso a variáveis locais da função externa

def fun1():
    msg = "Geeks para geeks"
    def fun2():
        print(msg)
    fun2()

fun1()  # saída: Geeks para geeks


# Exemplo 3: Modificação de variável externa usando nonlocal

def fun1():
    a = 45
    def fun2():
        nonlocal a
        a = 54
        print(a)
    fun2()
    print(a)

fun1()  # saída: 54 / 54


# Exemplo 4: Closure

def fun1(a):
    def fun2():
        print(a)
    return fun2

closure_func = fun1("Olá, Closure!")
closure_func()  # saída: Olá, Closure!


# Exemplo 5: Encapsulamento de funções auxiliares

def process_data(data):
    def clean_data():
        return [item.strip() for item in data]
    return clean_data()

print(process_data([" Python ", " Função Interna "]))  # ['Python', 'Função Interna']


# Exemplo 6: Wrapper e registro de logs (decorador simples)
import logging
logging.basicConfig(level=logging.INFO)

def logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executando {func.__name__} com {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 4))  # INFO + 7


# ------------------------------------------------------------
# EXPLICAÇÃO DO CÓDIGO LINHA POR LINHA (GERAL)
# ------------------------------------------------------------
# Cada exemplo demonstra um uso específico de funções internas:
# - Definição dentro de outra função.
# - Acesso ao escopo superior.
# - Uso de nonlocal para modificar variáveis externas.
# - Retorno de função interna criando closure.
# - Uso em decoradores para adicionar comportamento extra.
# - *args e **kwargs permitem flexibilidade.

# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - Funções internas / aninhadas
# - Encapsulamento
# - Organização de código
# - Escopo LEGB
# - nonlocal
# - Closures
# - Decoradores
# - Wrappers
# - logging
# - *args e **kwargs
# - Métodos de string (strip)
