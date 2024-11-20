""" 
O Python sendo um linguagem de tipagem dinâmica não é incomum ao lidar com dados com o tipo errado
quando um Int está como Float ou então como String se for nescessário teremos que fazer um Type Casting,
converter o tipo do dado.
Para isso é usado funções básicas do python como:
int(dado)
float(dado)
str(dado)
"""
#Ex:
num = int("1") # entre aspas é reconhecido como string, logo precisamos fazer o Type Casting (conversão) para int
num2  = float("1") # convertendo para float
num3 = str(1) # convertendo para string
print(type(num))
print(type(num2))
print(type(num3))