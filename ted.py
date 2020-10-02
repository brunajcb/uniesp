#### Função ####

def calculoMedias (num1, num2, num3, carac):
    if carac == "a" or carac == "A":
        return((num1 + num2 + num3)/3)
    elif carac == "P" or carac == "p":
        return ((num1*5) + (num2*3) + (num3*2)) / 10
    elif carac == "H" or carac == "h":
        return((3 / ((1/num1) + (1/num2) + (1/num3))))

#### Laço de decisão ####

pergunta = input('Deseja realizar um cálculo de média? Digite: Sim ou Não: ')

while pergunta == "sim" or pergunta == "Sim" or pergunta == "SIM":
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))

    print('\nA seguir informe qual tipo de cálculo você quer realizar...\n')
    print('Para média aritimética insira: A \nPara média ponderada insira: P \nPara média harmônica insira: H\n')

    carac = input('Insira um tipo de média para realizar o cálculo: ')

    print("O cálculo da média escolhida é: ", calculoMedias(num1, num2, num3, carac))

    pergunta = input('Deseja realizar outro cálculo de média? Digite: Sim ou Não: ')





