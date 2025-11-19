"""
ASSUNTO PRINCIPAL DETECTADO: Declaração `pass` em Python

Resumo geral do assunto.
A instrução `pass` em Python é um marcador de posição (no-op) que não executa qualquer ação.
Serve para manter a sintaxe válida em blocos que ainda não têm implementação (funções, classes,
condicionais, loops, métodos). É útil durante o desenvolvimento para esboçar a estrutura do código
sem definir a lógica imediatamente.

Explicação clara e didática.
- Quando o interpretador encontra `pass`, ele simplesmente continua a execução na próxima linha.
- `pass` é preferível a deixar um bloco vazio porque blocos vazios causariam erro de indentação/sintaxe.
- Use `pass` para prototipar: criar assinaturas de função, classes e ramos condicionais antes de
  escrever a lógica final.

Contexto sobre o que esse tema significa no Python.
- Faz parte das construções sintáticas que permitem criar esqueleto de código (scaffolding).
- Ajuda na leitura e manutenção do código, permitindo que a estrutura e a intenção sejam claras,
  mesmo que a implementação venha depois.
"""
# ------------------------------------------------------------
# TEORIA — ASSUNTO PRINCIPAL
# ------------------------------------------------------------
# A instrução `pass`
# - É uma operação nula (no-op): não realiza nenhuma operação.
# - Sintaxe: simplesmente escreva `pass` no corpo do bloco.
#
# Onde é usada:
# - Funções vazias: permite declarar uma função sem implementar sua lógica.
# - Métodos de classe vazios: permite definir a assinatura do método.
# - Classes vazias: cria classes atuando como marcadores até implementar atributos/métodos.
# - Blocos condicionais (if/elif/else): mantém o bloco sintaticamente válido.
# - Loops (for/while): permite deixar uma iteração sem ação específica.
#
# Por que usar `pass`:
# - Evita erros de sintaxe quando um bloco precisa existir mas ainda não contém lógica.
# - Facilita desenvolvimento incremental e TDD (escrever a estrutura antes dos testes/implementação).
#
# Comportamento em tempo de execução:
# - `pass` não altera estado nem retorna valor; é simplesmente ignorado durante a execução.
#
# Observações:
# - `pass` não é um placeholder para "fazer depois" no sentido de lançar exceção;
#   para indicar claramente que falta implementação você pode usar `raise NotImplementedError()`
#   (isso interrompe a execução, ao contrário de `pass` que continua silenciosamente).

# ------------------------------------------------------------
# TEORIA — CONTEÚDO RELACIONADO PRESENTE NO TEXTO
# ------------------------------------------------------------
# - Exemplos mostrados: uso em função, if/else, loops, classes, métodos vazios.
# - Menciona-se saída esperada para o exemplo do loop (0,1,2,4).
# - O texto inclui uma versão mal formatada (ex.: "passar", "passe", "imprimir") que aparenta ser
#   tradução/erro de OCR; todos os exemplos válidos estarão corrigidos abaixo, e comentaremos
#   onde o texto original continha tokens incorretos.
# - File/Imagem citada: uso_de_função_em_javascript_12.webp (apenas menção).
# - Termos relacionados: escopo, instância de classe, construtor (__init__), atributo, método.
#
# Observação sobre a fidelidade ao conteúdo original:
# - O arquivo inclui todos os conceitos e exemplos citados no texto (função vazia, condicional com pass,
#   loop com pass, classe vazia, método com pass, explicações). Corrigimos a sintaxe para Python válido,
#   mas mantivemos menção a erros de formatação originais no comentário acima.

# ------------------------------------------------------------
# EXEMPLOS (CÓDIGO FUNCIONAL) E EXPLICAÇÕES
# ------------------------------------------------------------

# Exemplo A — Função vazia usando pass
def fun():
    # Função definida, sem lógica por enquanto — `pass` mantém a função válida.
    pass

fun()  # Chama a função; nada acontece e o programa continua normalmente.


# Exemplo B — Condicional com pass
x = 10

if x > 5:
    # Espaço reservado: quando x > 5 não executamos ação por enquanto
    pass
else:
    print("x é 5 ou menos")

# Explicação:
# - Se x > 5: o interpretador executa `pass` (não faz nada) e segue em frente.
# - Caso contrário, executa o bloco else e imprime a mensagem.


# Exemplo C — Loop com pass (mostrando saída esperada no texto)
for i in range(5):
    if i == 3:
        # Não faça nada quando i for 3
        pass
    else:
        print(i)

# Saída esperada:
# 0
# 1
# 2
# 4
# Explicação: quando i == 3 o pass impede qualquer ação; nos demais valores o número é impresso.


# Exemplo D — Classe vazia com pass
class EmptyClass:
    # Classe válida mesmo sem atributos ou métodos por causa de `pass`
    pass

# Exemplo E — Classe com método placeholder
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        # Método definido, mas sem implementação ainda.
        pass

# Criando uma instância da classe
p = Pessoa("Emily", 30)
# p.cumprimentar() pode ser chamado, mas não fará nada até implementarmos o método.


# ------------------------------------------------------------
# EXPLICAÇÃO DO CÓDIGO — LINHA POR LINHA (RESUMIDA)
# ------------------------------------------------------------
# def fun():            -> declara a função `fun`.
#     pass              -> instr. de placeholder; a função é válida mas não faz nada.
# fun()                 -> chama a função; nenhuma saída gerada.
#
# x = 10                -> atribuição simples.
# if x > 5:             -> condição; avalia expressão booleana.
#     pass              -> bloco 'if' syntaticamente válido, sem ação.
# else:                 -> bloco alternativo.
#     print(...)        -> executa se a condição for False.
#
# for i in range(5):    -> loop que itera 0..4.
#     if i == 3:        -> verifica valor de i.
#         pass          -> não executa ação para i == 3.
#     else:
#         print(i)      -> imprime i nos outros casos.
#
# class EmptyClass:     -> declaração de classe vazia.
#     pass              -> evita SyntaxError; classe existe sem membros.
#
# class Pessoa:         -> classe com construtor e método placeholder.
#     def __init__(...):
#         self.nome...  -> inicializa atributos de instância.
#     def cumprimentar(self):
#         pass          -> método declarado sem lógica por enquanto.
#
# Observação: `pass` não modifica variáveis nem estados; é apenas um marcador sintático.

# ------------------------------------------------------------
# BOAS PRÁTICAS & ANOTAÇÕES
# ------------------------------------------------------------
# - Use `pass` para esqueleto de código e prototipagem. Para indicar implementação pendente com
#   falha explícita em tempo de execução, prefira `raise NotImplementedError()` em métodos que
#   realmente deveriam falhar quando usados antes da implementação.
# - Evite deixar `pass` em produção sem intenção clara — deixe comentários explicando o porquê,
#   por exemplo: `# TODO: implementar validação aqui`.
# - `pass` é útil em exemplos educacionais, testes e ao estruturar módulos complexos por etapas.

# ------------------------------------------------------------
# RESUMO TÉCNICO (TUDO QUE APARECEU NO TEXTO)
# ------------------------------------------------------------
# - pass (instrução)
# - marcador de posição (placeholder)
# - funções vazias
# - classes vazias
# - métodos vazios
# - condicionais (if / else)
# - loops (for)
# - range()
# - exemplos de saída (0,1,2,4)
# - instância de classe (p = Pessoa(...))
# - __init__ (construtor)
# - atributo de instância (self.nome, self.idade)
# - Notação sobre uso em desenvolvimento incremental / scaffolding
# - imagem mencionada: uso_de_função_em_javascript_12.webp
# - observação sobre alternativamente usar `raise NotImplementedError()`
# - recomendação de comentários TODO junto com pass

# ------------------------------------------------------------
# NOTAS SOBRE TRECHO ORIGINAL COM ERROS DE FORMATAÇÃO
# ------------------------------------------------------------
# O texto original continha tokens/termos possivelmente resultantes de tradução automática ou OCR,
# por exemplo: "passar", "passe", "imprimir" em vez de "pass", "print".
# - Neste arquivo corrigimos os exemplos para Python válido, mas mantivemos menção a esses erros
#   nos comentários para fidelidade ao conteúdo original.

# ------------------------------------------------------------
# EXEMPLOS ADICIONAIS ÚTEIS (VARIAÇÕES E CONTRASTES)
# ------------------------------------------------------------

# Exemplo F — Usando pass em estrutura de exceção (try/except)
try:
    # código que pode lançar exceção
    x = 1 / 1
except ZeroDivisionError:
    # por ora não lidamos com a exceção
    pass

# Exemplo G — Quando usar raise NotImplementedError em vez de pass
class BaseProcessor:
    def process(self, data):
        # Indica que subclasses devem implementar este método.
        raise NotImplementedError("Subclasses devem implementar process()")

# Exemplo H — Exemplo com TODO comentado
def futura_funcao():
    # TODO: implementar logging e validação
    pass

# ------------------------------------------------------------
# FIM DO ARQUIVO
# ------------------------------------------------------------
