#set tem relação com as teorias do conjunto em matemática

#regras básicas:
# set só pode receber uma váriavel como argumento
#por isso o melhor jeito de trabalhar com set é utilizando listas, pois uma lista pode ser uma variável


################################## Exemplo set 01 ##################################

a = {1,2,3,4,5} #forma simplificada
b = {3,4,5,6}

print a.union(b)
set([1,2,3,4,5,6]) #forma antiga

l1 = [1,2,3]
l2 = [2,4,3]

print set(l1).intersection(l2)


################################## Exemplo set 02 ##################################
cores = set(["Amarelo", "Azul", "Rosa", "Roxo", 1,2,3.5,4,5, ("casa", "carro") ["flor amarela", 1,2,3]])
# uma lista poder conter: strings, números inteiros, flutuantes, tuplas e até outra lista dentro dela
#set = mutável

cores.add(("olar", "how are you?"))



#frozeset = imutável; assim como uma tupla, não pode ser alterada
frutas = (["morango", "abacaxi", "uva"])
#frutas. add("pera") => impossível alterar, vai aparecer mensagem de erro ao executar o comando

################################## Outras funções utilizadas com set ##################################

carros = "olar mundo!"
carros.clear() #limpa conteúdo

carros = {"Fusca", "Tipo", "Fiat 146", "Belina", "Corcel"}
copia_carros = carros.copy() #cria lista cópia

carros.clear()
#copia_carros não será alterada!


x = {"Estou", "sem", "criatividade", "!"}
y = {"Estou", "sem", "criatividade", "hoje", "rs"}
z = {"Estou", "estudando", "agora", ".", "Como está você?"}
# type x => mostra o tipo de dado de uma variável

x.difference(y) # => mostra apenas as diferenças de y e x
# set(["!", "hoje", "rs"])

x.difference(y).difference(z) # => mostra apenas as diferenças entre y, x e z
# set(["!", "hoje", "rs", "estdando", "agora", ".", "Como está você?"])

#outra forma: operação de subtração:
# x - y
# set(["!", "hoje", "rs"])

# x - y - z
# set(["!", "hoje", "rs", "estdando", "agora", ".", "Como está você?"])

#difference.update => faz uma comparação e o que for igual entre os dois é removido do primeiro
# x = x - y => faz mesma coisa que o comando acima


#discard => ermove um elemento de uma variável set
set(["abc", "casa", "carro", "rua"])
x.discard("abc") # se pedirmos para remover algo que não existe, nenhum erro é gerado
#set(["casa", "carro", "rua"])


x.remove("cores") # => faz a mesma coisa que o remove, porém se pedirmos para algo que não existe, um erro é gerado.

set{[a,b,c,d,e]} # => economiza tempo porque não há ordem de elementos
set("a", "b", "c", "d", "e") # => quando printa, sai desordenado