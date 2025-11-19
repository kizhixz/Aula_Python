"""
ASSUNTO PRINCIPAL DETECTADO: Uso de 'self' em métodos de classes Python

Resumo geral do assunto.
Este arquivo explica por que Python utiliza 'self' como primeiro argumento de métodos
em classes, como ele funciona internamente, por que é explícito e quais benefícios
isso traz para a orientação a objetos.

Contexto sobre o que esse tema significa no Python.
No Python, métodos de instância recebem automaticamente o objeto como primeiro
argumento. A convenção é chamar esse argumento de 'self'. Isso permite acessar e 
manipular atributos e métodos da instância de forma explícita e clara.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL
# ------------------------------------------------------------
# Em Python, o primeiro parâmetro de qualquer método de instância é 'self'.
# Ele representa a própria instância do objeto usada na chamada do método.
#
# 'self' NÃO é palavra-chave; é apenas convenção.
#
# Por que Python usa 'self':
# - Clareza: segue "explícito é melhor que implícito".
# - Consistência: todos os métodos usam esse padrão.
# - Flexibilidade: qualquer nome poderia ser usado, mas 'self' é o padrão universal.
#
# Python não torna essa referência implícita como outras linguagens — isso aumenta
# a legibilidade e evita confusões durante herança ou múltiplas instâncias.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# O texto original inclui:
# - Criação de classes (Carro, gfg, Círculo)
# - Uso de __init__ para inicialização
# - Atribuição de atributos de instância (self.atributo = valor)
# - Chamadas de métodos (obj.metodo())
# - Uso de print()
# - Retorno de tupla
# - Cálculo matemático na classe Círculo (área = πr²)
#
# Esses assuntos não são o tópico principal, mas aparecem no conteúdo e são
# documentados aqui separadamente.

# ------------------------------------------------------------
# EXEMPLOS (inclui seus exemplos + exemplos novos)
# ------------------------------------------------------------

# Exemplo 1: Classe Carro com uso de self
class Carro:
    def __init__(self, brand, model):
        self.brand = brand       # Define o atributo da instância
        self.model = model       # Define o atributo da instância

    def exibir(self):
        return self.brand, self.model  # Retorna atributos da instância

# Criando instância
carro1 = Carro("Toyota", "Corolla")

# Exibindo
print(carro1.exibir())
# Explicação: Python passa carro1 automaticamente como 'self'.


# Exemplo 2: Classe gfg
class gfg:
    def __init__(self, topic):
        self._topic = topic  # Armazena o valor na instância

    def topic(self):
        print("Tópico:", self._topic)

ins = gfg("Python")
ins.topic()
# Explicação: ins é fornecido automaticamente como self no tópico()


# Exemplo 3: Classe Círculo
class Circulo:
    def __init__(self, r):
        self.r = r

    def area(self):
        a = 3.14 * self.r ** 2
        return a

ins = Circulo(5)
print("Área do círculo:", ins.area())
# Explicação: self.r garante que o raio pertence à instância correta.


# ------------------------------------------------------------
# EXPLICAÇÃO DO MEU CÓDIGO (LINHA POR LINHA)
# ------------------------------------------------------------
# class Carro:                -> Define uma nova classe chamada Carro.
# def __init__(...):          -> Método construtor, recebe self, brand e model.
# self.brand = brand          -> Atributo brand é armazenado na instância.
# self.model = model          -> Atributo model é armazenado na instância.
# def exibir(self):           -> Método que usa self para acessar atributos.
# return self.brand, self.model -> Retorna tupla com valores da instância.
# carro1 = Carro(...)         -> Cria instância; Python envia carro1 como self.
# print(carro1.exibir())      -> Chama método exibir e imprime resultado.
#
# class gfg:                  -> Classe para exemplo de tópico armazenado.
# self._topic = topic         -> Armazena valor na instância.
# def topic(self):            -> Método imprime o atributo da instância.
# ins = gfg("Python")         -> Cria objeto.
# ins.topic()                 -> Python injeta ins como self.
#
# class Circulo:              -> Classe para cálculo de área.
# self.r = r                  -> Armazena o raio.
# a = 3.14 * self.r ** 2      -> Cálculo da área usando atributo da instância.
# return a                    -> Retorna área específica da instância.
# ins.area()                  -> Autoenvio de self para acessar r correto.


# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - self como parâmetro explícito
# - convenção de nomenclatura 'self'
# - clareza e legibilidade explícita do Python
# - método __init__
# - atributos de instância
# - classes Carro, gfg, Circulo
# - métodos de instância
# - retorno de tupla
# - print()
# - cálculo matemático (área = πr²)
# - acesso a atributos via self
# - comportamento automático de passagem de instância
# - criação de objetos
# - chamada de métodos obj.método()

