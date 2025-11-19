"""
ASSUNTO PRINCIPAL DETECTADO: Variáveis em Python

Resumo geral do assunto:
Este documento explica detalhadamente como variáveis funcionam em Python, como são
criadas, nomeadas, manipuladas, convertidas e como se comportam internamente em relação
a referências de objetos.

Explicação clara e didática:
Python utiliza tipagem dinâmica, ou seja, o tipo é inferido automaticamente de acordo
com o valor atribuído. Variáveis são apenas rótulos que referenciam objetos na memória.
Também são apresentadas regras de nomenclatura, uso de palavras-chave, atribuições
múltiplas, conversão de tipos, coleta de lixo, exclusão de variáveis e comportamento de
referências compartilhadas.

Contexto no Python:
Por ser uma linguagem dinâmica e orientada a objetos, todos os valores em Python são
objetos, e variáveis apenas apontam para esses objetos. Esse modelo simplifica a escrita
de código, permite flexibilidade e torna operações como troca de variáveis
extremamente diretas.
"""

# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL (VARIÁVEIS EM PYTHON)
# ------------------------------------------------------------
# O que é uma variável:
# - Uma variável é um nome que referencia um valor armazenado na memória.
# - Python NÃO exige declaração de tipo; ele é inferido automaticamente.
# - Ex.: x = 5 → x referencia o objeto inteiro 5.

# Tipagem dinâmico-inferida:
# - Python pode alterar o tipo da variável conforme o valor atribuído.
#   Ex.: x = 10 → inteiro / x = "texto" → string.

# Regras de nomenclatura:
# - Podem conter letras, números e underline.
# - Não podem começar com número.
# - São case-sensitive: nome != Nome.
# - Não podem usar palavras-chave (if, for, class, etc.)

# Referências de objetos:
# - Variáveis não armazenam valores; armazenam referências para objetos.
# - Várias variáveis podem apontar para o mesmo objeto.
# - Atribuição posterior faz a variável apontar para um novo objeto.

# Atribuições múltiplas:
# - Python permite atribuições em cadeia: a = b = c = 100
# - Atribuições múltiplas com diferentes valores: x, y, z = 1, 2.5, "Python"

# Conversão de tipos (casting):
# - int(), float(), str()
# - Converte valores entre tipos quando compatíveis.

# Exclusão de variáveis:
# - del x remove a variável do namespace.
# - Acessar após o del gera NameError.

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# Palavras-chave:
# - São palavras reservadas da linguagem, como if, else, for, return, class, etc.
# - Não podem ser usadas como variáveis.
# - Estão disponíveis pelo módulo keyword (keyword.kwlist).

# Categorias de palavras-chave mencionadas:
# - Valores: True, False, None
# - Operadores: and, or, not, is, in
# - Controle de fluxo: if, else, elif, for, while, break, continue, pass, try, except...
# - Funções/classe: def, return, class, lambda, yield
# - Assíncrono: async, await
# - Escopo: global, nonlocal
# - Gerenciamento de contexto: with, as
# - Importação: import, from

# Estruturas de dados citadas:
# - list, dict, tuple, bool, str, int, float.

# ------------------------------------------------------------
# EXEMPLOS (DO CONTEÚDO + COMPLEMENTARES)
# ------------------------------------------------------------

# Exemplo básico de variáveis:
x = 5
name = "Samantha"
print(x)
print(name)

# Exemplo: obtendo lista de palavras-chave
import keyword
print("The list of keywords are : ")
print(keyword.kwlist)

# Exemplo de erro ao usar palavra-chave como variável (ilustrativo; não executável):
# for = 10
# print(for)
# → SyntaxError

# Atribuição de mesmo valor:
a = b = c = 100
print(a, b, c)

# Atribuição múltipla com valores diferentes:
x, y, z = 1, 2.5, "Python"
print(x, y, z)

# Conversão de tipos:
s = "10"
n = int(s)
cnt = 5
f = float(cnt)
age = 25
s2 = str(age)

print(n)
print(f)
print(s2)

# Verificação de tipos:
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {"key": "value"}
bool_var = True

print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(d))
print(type(bool_var))

# Referências de objeto:
x = 5
y = x  # y referencia o mesmo objeto que x
x = "Geeks"  # x agora referencia outro objeto

# Exclusão de variável:
x2 = 10
print(x2)
del x2
# print(x2) → NameError

# Troca de variáveis:
a, b = 5, 10
a, b = b, a
print(a, b)

# Contar caracteres:
word = "Python"
length = len(word)
print("Length of the word:", length)

# ------------------------------------------------------------
# EXPLICAÇÃO DO MEU CÓDIGO (LINHA POR LINHA RESUMIDA)
# ------------------------------------------------------------
# - x = 5 / name = "Samantha": criação e atribuição de variáveis.
# - print(x), print(name): exibição dos valores.
# - import keyword: importa módulo para acessar lista de palavras-chave.
# - keyword.kwlist: retorna lista de palavras reservadas.
# - a = b = c = 100: atribuição encadeada.
# - x, y, z = ...: atribuição múltipla.
# - int(), float(), str(): conversão de tipos.
# - type(): obtém o tipo do objeto.
# - y = x: referência compartilhada.
# - del x: remove variável.
# - a, b = b, a: troca de valores sem variável temporária.
# - len(word): obtém tamanho de string.

# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - Variáveis e tipagem dinâmica
# - Regras de nomenclatura
# - Atribuição simples, múltipla e encadeada
# - Palavras-chave e módulo keyword
# - Categorias de palavras-chave
# - Diferença entre variáveis e palavras-chave
# - Conversão de tipos: int(), float(), str()
# - Função type()
# - Exclusão com del
# - Referência compartilhada de objetos
# - Troca de variáveis
# - len() para medir tamanho
# - Estruturas: list, dict, tuple
# - Exemplos práticos diversos
