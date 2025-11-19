"""
ASSUNTO PRINCIPAL DETECTADO: Decoradores em Python

Resumo geral do assunto.
Os decoradores em Python são uma construção de linguagem poderosa e flexível que permite modificar ou estender o comportamento de funções ou métodos (e até classes) sem alterar seu código-fonte original. Eles promovem o princípio DRY (Don't Repeat Yourself) e a separação de interesses.

Explicação clara e didática.
Um decorador é, essencialmente, uma função que recebe outra função como argumento e retorna uma nova função (geralmente chamada de "wrapper") que adiciona funcionalidades extras ao redor da função original. A sintaxe especial '@nome_do_decorador' é apenas um "açúcar sintático" que simplifica a aplicação dessa lógica.

Contexto sobre o que esse tema significa no Python.
Os decoradores são um dos pilares da programação funcional em Python e dependem fortemente de dois conceitos fundamentais: Funções como Objetos de Primeira Classe (podem ser passadas, retornadas e atribuídas como variáveis) e Funções de Ordem Superior (funções que operam sobre outras funções). Eles são amplamente utilizados em frameworks web (como Flask e Django) para tarefas como roteamento, autenticação e registro de logs.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL (DECORADORES)
# ------------------------------------------------------------
# Um decorador é uma função que recebe outra função (func) como argumento e retorna uma nova função.
# O principal objetivo é modificar ou estender o comportamento da 'func' original.
#
# Sintaxe:
# O uso de `@decorador` antes da definição de uma função 'func' é a forma abreviada (açúcar sintático)
# para a chamada: `func = decorador(func)`.
#
# Usos Comuns:
# - Registro de Logs (log calls)
# - Autenticação (verificar permissões)
# - Memorização/Cache (armazenar resultados de funções custosas)
# - Validação de dados de entrada
#
# Estrutura Básica:
# Um decorador é composto por:
# 1. A função externa (o decorador em si), que recebe a função a ser decorada.
# 2. A função interna (o 'wrapper' ou 'envolvedor'), que contém a lógica extra e chama a função original.
# 3. O retorno da função interna (wrapper) pela função externa.
#
# Lidando com Parâmetros:
# Para que a função 'wrapper' funcione com *qualquer* função decorada (independentemente dos seus argumentos),
# ela deve aceitar argumentos genéricos usando `*args` (argumentos posicionais) e `**kwargs` (argumentos nomeados).
# O resultado da função original deve ser retornado pelo wrapper para manter a funcionalidade.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# Funções como Objetos de Primeira Classe:
# Em Python, funções são tratadas como qualquer outro objeto (como números, strings, listas).
# Isso significa que elas podem ser:
# 1. Atribuídas a variáveis.
# 2. Passadas como argumentos para outras funções.
# 3. Retornadas por outras funções.
# 4. Armazenadas em estruturas de dados (listas, dicionários, etc.).
# Este conceito é *essencial* porque os decoradores dependem dele: um decorador recebe uma função (como argumento) e retorna outra (como resultado).
#
# Funções de Ordem Superior (Higher-Order Functions):
# Uma função é de Ordem Superior se ela aceita uma ou mais funções como argumentos e/ou retorna uma função como resultado.
# Um **Decorador** é um tipo específico de Função de Ordem Superior.
#
# Tipos de Decoradores:
# - Decoradores Funcionais: Envolvem e aprimoram funções. São os mais comuns.
# - Método Decoradores: Usados para métodos dentro de classes; precisam lidar explicitamente com o parâmetro `self`.
# - Decoradores de Classe: Recebem uma classe como argumento e retornam uma classe modificada (por exemplo, adicionando um atributo).
#
# Decoradores Embutidos (@staticmethod, @classmethod, @property):
# - @staticmethod: Para métodos que não precisam de acesso nem à instância (`self`) nem à classe (`cls`). Chamado diretamente na classe.
# - @classmethod: Para métodos que operam na classe e recebem a própria classe (`cls`) como primeiro argumento. Usado para modificar o estado da classe ou criar construtores alternativos.
# - @property: Permite que um método seja acessado como um atributo. É usado para 'getters' e, quando combinado com `@<nome>.setter`, para 'setters', permitindo encapsulamento e validação de atributos.

# ------------------------------------------------------------
# EXEMPLOS
# ------------------------------------------------------------

# Exemplo 1: Decorador simples sem argumentos (Exemplo do conteúdo)
# O decorador 'decorador' recebe uma função, a envolve na 'wrapper' para adicionar
# mensagens antes e depois, e retorna a 'wrapper'.
def decorador(func):
    """
    Decorador simples que adiciona mensagens de início e fim ao redor da execução da função.
    """
    def wrapper():
        print("Antes de chamar a função.")
        func()
        print("Após chamar a função.")
    return wrapper

@decorador  # Abreviação para 'cumprimentar = decorador(cumprimentar)'
def cumprimentar():
    print("Olá, mundo!")

cumprimentar()
# Explicação do exemplo: Ao chamar cumprimentar(), a função 'wrapper' é executada.

# ------------------------------------------------------------

# Exemplo 2: Decorador com argumentos genéricos (*args, **kwargs) (Exemplo do conteúdo)
# Este é o padrão para decoradores que precisam funcionar com funções de qualquer assinatura.
def nome_decorador(func):
    """
    Decorador que suporta argumentos genéricos para a função decorada.
    """
    def wrapper(*args, **kwargs):
        print("Antes da execução")
        # Chama a função original, passando todos os argumentos
        resultado = func(*args, **kwargs)
        print("Após a execução")
        # Retorna o resultado da função original
        return resultado
    return wrapper

@nome_decorador
def adicionar(a, b):
    return a + b

# O wrapper recebe 5 e 3 via *args e retorna o resultado (8)
print(adicionar(5, 3))
# Explicação do exemplo: O decorador adiciona as mensagens de início/fim e o wrapper garante que 5 e 3
# sejam corretamente passados para a função 'adicionar'.

# ------------------------------------------------------------

# Exemplo 3: Uso de @staticmethod (Exemplo do conteúdo)
# Demonstra um método que não requer a instância da classe.
class MathOperations:
    """Classe com uma operação matemática estática."""
    @staticmethod
    def add(x, y):
        """Método estático para somar dois números."""
        return x + y

# Chamado diretamente na classe.
res = MathOperations.add(5, 3)
print(res)
# Explicação do exemplo: O método 'add' funciona de forma independente do estado da classe ou instância.

# ------------------------------------------------------------

# Exemplo 4: Uso de @property e @<nome>.setter (Exemplo do conteúdo)
# Demonstra como acessar um método como se fosse um atributo e como validá-lo.
class Circle:
    """Classe Círculo com raio validado via property."""
    def __init__(self, radius):
        """Inicializa com o raio. O setter é chamado implicitamente aqui."""
        self._radius = radius # Armazena o valor 'privado'

    @property
    def radius(self):
        """Getter para o raio. Acessado como um atributo: c.radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter para o raio com validação."""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("O raio não pode ser negativo")

    @property
    def area(self):
        """Calcula e retorna a área. Acessado como um atributo: c.area"""
        return 3.14159 * (self._radius ** 2)

c = Circle(5)
print(f"Raio inicial: {c.radius}")
print(f"Área inicial: {c.area}")
c.radius = 10 # Chama o método 'setter'
print(f"Nova área: {c.area}")
# Explicação do exemplo: 'c.radius' e 'c.area' são acessados sem parênteses, como atributos,
# mas são métodos controlados internamente pelos decoradores @property e @radius.setter.

# ------------------------------------------------------------
# EXPLICAÇÃO DO MEU CÓDIGO (LINHA POR LINHA)
# ------------------------------------------------------------
# O conteúdo fornecido é uma documentação teórica e vários exemplos.
# A explicação de cada exemplo de código foi detalhada nas seções acima.

# Exemplo Decorador Simples:
# def decorador(func):                     # Define a função decoradora, recebe a função a ser decorada (cumprimentar).
#     def wrapper():                       # Define a função interna (o wrapper).
#         print("Antes de chamar a função.") # Comportamento extra antes.
#         func()                           # Chama a função original.
#         print("Após chamar a função.")   # Comportamento extra depois.
#     return wrapper                       # Retorna a função wrapper.
# @decorador                               # Açúcar sintático: cumprimentar = decorador(cumprimentar).
# def cumprimentar():                      # Define a função original.
#     print("Olá, mundo!")                 #
# cumprimentar()                           # Chama o wrapper retornado, que executa o comportamento extra.

# Exemplo Decorador com Parâmetros (*args, **kwargs):
# def nome_decorador(func):                # Define o decorador.
#     def wrapper(*args, **kwargs):        # O wrapper aceita qualquer argumento (*args, **kwargs).
#         print("Antes da execução")       # Comportamento extra antes.
#         resultado = func(*args, **kwargs) # Chama a função original com os argumentos e armazena o resultado.
#         print("Após a execução")         # Comportamento extra depois.
#         return resultado                 # Retorna o resultado da função original.
#     return wrapper                       # Retorna o wrapper.
# # ... (restante do código segue a lógica do Exemplo 1)

# Exemplo Funções de Primeira Classe:
# # Atribuindo uma função a uma variável:
# say_hi = greet                          # Variável 'say_hi' referencia a função 'greet'.
# print(say_hi("Alice"))                  # Chama a função via nova variável.
# # Passando uma função como argumento:
# def aplicar(f, v):                      # Função 'aplicar' recebe uma função 'f' e um valor 'v'.
#     return f(v)                         # Chama a função 'f' com o valor 'v'.
# res = aplicar(say_hi, "Bob")            # Passa a função 'say_hi' como argumento.
# # Retornando uma função de outra função: (Base para decoradores!)
# def make_mult(f):                       # Função externa recebe um fator 'f'.
#     def mult(x):                        # Função interna ('mult') armazena o fator 'f' (closure).
#         return x * f                    #
#     return mult                         # Retorna a função interna.
# dbl = make_mult(2)                      # 'dbl' armazena a função 'mult' onde 'f' é 2.
# print(dbl(5))                           # Chama a função armazenada.

# Exemplo @classmethod e @staticmethod:
# @staticmethod                           # Decorador que remove a necessidade de self/cls.
# def add(x, y):                          # Método estático.
# @classmethod                            # Decorador que força o primeiro argumento a ser a classe (cls).
# def set_raise_amount(cls, amount):      # Método de classe.
#     cls.raise_amount = amount           # Modifica uma variável da classe (cls.raise_amount).
# Employee.set_raise_amount(1.10)         # Chamado na classe.

# Exemplo @property:
# @property                              # Define o método como um 'getter' de atributo.
# def radius(self):                       # Acessado como c.radius.
# @radius.setter                          # Define o método como um 'setter' de atributo para 'radius'.
# def radius(self, value):                # Acessado como c.radius = <valor>.
#     if value >= 0:                      # Lógica de validação do setter.
#         self._radius = value            #
#     else:                               #
#         raise ValueError("...")         #

# Exemplo Encadeamento:
# @decor1                                 # Decorador mais próximo da função (decor1) é o mais externo (último a ser executado).
# @decor2                                 # Decorador mais longe da função (decor2) é o mais interno (primeiro a ser executado).
# def num(): ...                          # Ordem: num -> decor2 -> decor1
# @decor2
# @decor1
# def num2(): ...                         # Ordem: num2 -> decor1 -> decor2

# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - Decoradores (em Python)
# - Função de ordem superior
# - Funções como objetos de primeira classe
# - Docstrings ("""...""")
# - Comentários (#)
# - Função (def)
# - Argumentos genéricos (*args e **kwargs)
# - Função aninhada (wrapper, inner, mult)
# - Retorno (return)
# - Variáveis (x, y, a, b, res, amount, dbl, c, obj)
# - Tipos de Decoradores (Funcionais, Método, Classe)
# - Decoradores Embutidos
#   - @staticmethod
#   - @classmethod
#   - @property
#   - @<nome>.setter
# - Variáveis de classe (raise_amount)
# - Parâmetro de instância (self)
# - Parâmetro de classe (cls)
# - Classe (class)
# - Método (def dentro de classe)
# - Método construtor (__init__)
# - Módulos implícitos (e.g., functools para lru_cache, Flask/Django para autenticação)
# - Levantamento de exceção (raise ValueError)
# - Operadores (*, +, >=, **)
# - Encadeamento de decoradores
# - Açúcar sintático (@decorator)
# - Encapsulamento (uso de self._radius)

