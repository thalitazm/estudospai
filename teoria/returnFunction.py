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

###############################################################
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
print("\n O resultado da função is_true é {}".format(res))