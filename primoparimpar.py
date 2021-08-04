num = int(input('Digite um inteiro: '))

if (num % 2) == 0:
    print("Par")
else:
    print("Ímpar")

mult = 0

for count in range(2,num):
    if (num % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É um nº Primo!")
else:
    print("Tem",mult,"múltiplos acima de 2 e abaixo de",num)
