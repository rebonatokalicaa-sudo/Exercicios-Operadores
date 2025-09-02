print("Resultados das contas:")
print("17/4 =", 17/4)
print("17//4 =", 17//4)
print("17%4 =", 17%4)
print("2**5 =", 2**5)
print("---------------------------")

# EX 2
n = int(input("Digite um número: "))

if n % 3 == 0 and n % 5 == 0:
    print("É múltiplo de 3 e 5")
else:
    print("Não é múltiplo de 3 e 5")
print("---------------------------")

# EX 3
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if (a > b and a < c) or (a > c and a < b):
    print("O primeiro número está entre os outros dois")
else:
    print("O primeiro número NÃO está entre os outros dois")
print("---------------------------")

# EX 4
while True:
    x = float(input("Digite um número: "))

    if x < 0.999999 or x > 1.000001:
        print("Ainda não está próximo de 1.0, tente de novo")
    else:
        print("Número está próximo de 1.0")
        break
print("---------------------------")

# EX 5
soma = 0
for i in range(1, 51):
    if i % 2 == 0:
        soma += i
print("Soma dos pares de 1 a 50:", soma)
