soma = 0
while True:
    num = int(input("Digite o número desejado: "))
    soma = soma + num
    if num == 0:
        print(soma)
        break