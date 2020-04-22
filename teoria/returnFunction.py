############ Declaração de retorno em Python ############

# return => retorna o resultado da execução chamada de uma função
# não pode ser usada fora da função!

# sintaxe:
            # def fun()
            # afirmacao
            # .
            # .
            # .
            # retorna [resultado]

#######################################################################################################

# Faça um programa em Python para demostrar uma declaração de retorno

def add(a, b):
    #retorna a soma de a e b:
    return a + b

def is_true(a):

    # retorna boleano de a:
    return bool(a)

# chama função:
res = add(2, 3)

res = add(2, 3)
print("O resultado da função de adição é: {}".format(res))

res = is_true(2 < 5)
print("\nO resultado da função is_true é {}".format(res))

#####################################################################################################

# Faça um programa em Python que retorne vários valores de um método usando classes:

class Teste:
    def __init__(self):
        self.str = "Hello, world! ;)"
        self.x = 19

# retorna um objeto da classe teste
def fun():
    return Teste()

# testar o método acima:

t = fun()
print(t.str)
print(t.x)


#####################################################################################################

# Exemplo utilizando tuplas:
# => sequencia de itens separados por vírgula. Pode ser criado com ou sem ()
# => são imutáveis - importante!

def fun():
    str = "Hello, World! ;)"
    x = 8
    return (str, x);

str, x = fun()
print(str)
print(x)

#####################################################################################################

# Exemplo utilizando listas:
# listas são como uma matriz que podem são escritas entre [],
# porém podem conter itens de outros tipos, diferentemente de uma matriz;

# Faça um programa em Python que retorne vários valores de um método usando listas:

def fun():
    str = "Hello, world! ;)"
    x = 1908
    return [str, x]
list = fun()
print(list)

#####################################################################################################

# Exemplo utilizando dicionário:

def fun():
    d = dict();
    d['str'] = "Hello, World! ;)"
    d['x'] = 1908
    return d

# para testar:
d = fun()
print(d)

#####################################################################################################
# Exemplo de função retornando de outra função

# Faça um programa para ilustrar funções que pode, retornar de uma outra função

def create_adder(x):
    def adder(y):
        return x + y

    return adder

add_15 = create_adder(15)

print("\nO resultado é:", add_15(10))

#retornando de função diferente
def outer(x):
    return x * 10

def minha_funcao():

    #retornando de diferente função
    return outer

#armazena a função em resultado
resultado = minha_funcao()

print("\nO resultado é:", resultado(10))
