"""
ASSUNTO PRINCIPAL DETECTADO: Funções em Python

Resumo geral:
Este arquivo documenta detalhadamente o conceito de Funções em Python, incluindo definição,
chamada, argumentos (posicionais, nomeados, padrão, arbitrários), funções aninhadas,
funções anônimas (lambda), comportamento de retorno, passagem por referência/valor e recursão.

Contexto:
Funções são blocos reutilizáveis de código que executam uma tarefa específica.
Elas ajudam a organizar, reutilizar e estruturar programas de forma mais modular.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL (FUNÇÕES EM PYTHON)
# ------------------------------------------------------------
# Uma função em Python é definida com "def" e pode receber parâmetros.
# Executamos uma função chamando seu nome seguido de parênteses.
# Funções ajudam a reaproveitar código e organizar melhor programas.
#
# A declaração básica envolve:
#   - def nome_da_funcao(parâmetros):
#         corpo
#         return opcional
#
# Tipos de argumentos:
#   • Argumentos padrão — possuem valor pré-definido.
#   • Argumentos nomeados (keyword arguments) — ordem não importa.
#   • Argumentos posicionais — ordem importa.
#   • Argumentos arbitrários — *args e **kwargs para quantidades variáveis.
#
# Funções podem:
#   • Conter funções internas (aninhadas).
#   • Ser anônimas (lambda).
#   • Retornar valores (inclusive múltiplos).
#   • Ser recursivas — chamando a si mesmas.
#
# Passagem de argumentos:
#   - Python usa "passagem por referência de objeto".
#   - Objetos mutáveis podem ser alterados dentro da função.
#   - Objetos imutáveis NÃO podem ser modificados internamente.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# - Explicação sobre mutabilidade de objetos (listas, inteiros).
# - Comportamento especial da instrução return.
# - Uso de condição if/else para verificar paridade.
# - Uso de loops para percorrer *args e **kwargs.
# - Noções de escopo em funções internas.
# - Exemplos com mensagens e prints diversos.
# - Menciona-se um arquivo/imagem: uso_de_função_em_javascript_12.webp (conteúdo externo).
# - Diferentes estilos de saída mostrados no texto (“Even/Odd”, “x: 10”, etc.).


# ------------------------------------------------------------
# EXEMPLOS DO CONTEÚDO + EXPLICAÇÕES
# ------------------------------------------------------------

# Exemplo 1 — Definição simples de função
def fun():
    print("Welcome to GFG")  # Exibe uma mensagem simples

fun()  # Chamada da função


# Exemplo 2 — Função que verifica par ou ímpar
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))


# Exemplo 3 — Argumento padrão
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)  # y assume o valor padrão


# Exemplo 4 — Argumentos nomeados
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


# Exemplo 5 — Argumentos posicionais
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")


# Exemplo 6 — Argumentos arbitrários
def myFun_args_kwargs(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun_args_kwargs('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')


# Exemplo 7 — Função interna (aninhada)
def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
    f2()

f1()


# Exemplo 8 — Função anônima (lambda)
def cube(x): 
    return x*x*x  # versão normal

cube_l = lambda x: x*x*x  # versão lambda

print(cube(7))
print(cube_l(7))


# Exemplo 9 — Valor de retorno
def square_value(num):
    """This function returns the square value of the entered number"""
    return num**2

print(square_value(2))
print(square_value(-4))


# Exemplo 10 — Passagem por referência e valor
def myFun_list(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun_list(lst)
print(lst)   # lista modificada


def myFun2(x):
    x = 20  # tentativa de modificar inteiro (imutável)

a = 10
myFun2(a)
print(a)     # não modificado


# Exemplo 11 — Função recursiva (fatorial)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))


# ------------------------------------------------------------
# EXPLICAÇÃO DO CÓDIGO — LINHA POR LINHA (RESUMIDA)
# ------------------------------------------------------------
# - Cada função acima é declarada com "def" seguida de parâmetros.
# - "return" encerra a função e devolve valores.
# - Funções com *args percorrem argumentos não nomeados via loop.
# - Funções com **kwargs percorrem pares chave:valor.
# - Funções internas acessam variáveis do escopo externo.
# - Lambdas criam funções curtas sem nome usando "lambda".
# - Funções recursivas chamam a si mesmas até um caso base.
# - Exemplos com listas mostram mutabilidade.
# - Exemplos com inteiros mostram imutabilidade.
# - Prints exibem resultados para demonstrar conceitos.


# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - def
# - chamada de função
# - parâmetros
# - argumentos padrão
# - argumentos nomeados (keyword)
# - argumentos posicionais
# - *args
# - **kwargs
# - return
# - funções internas / aninhadas
# - lambda (funções anônimas)
# - recursão
# - mutabilidade x imutabilidade
# - passagem por referência de objeto
# - condição if/else
# - operações aritméticas (%, **)
# - impressão com print()
# - exemplos de saída
# - imagem citada: uso_de_função_em_javascript_12.webp
# - listas
# - inteiros
