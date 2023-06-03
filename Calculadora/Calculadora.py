
print('Bem vindo a Calculadora!\n Faça operações usando dois números.')

def calculadora():

    primeiro_nuemero = int(input('Digite o primeiro número: '))
    operador = input('''Qual a operação você deseja fazer?
    + para adição
    - para subtração
    / para divisão
    * para multiplicação:
    -> ''')
    segundo_numero = int(input('Digite o segundo número: '))


    if operador == '+':
        add= int(primeiro_nuemero + segundo_numero)
        print('{} + {} = {}' .format(primeiro_nuemero, segundo_numero, add))

    elif operador == '-':
        sub= int(primeiro_nuemero - segundo_numero)
        print('{} - {} = {}'.format(primeiro_nuemero, segundo_numero, sub))

    elif operador == '/':
        div= int(primeiro_nuemero / segundo_numero)
        print('{} / {} = {}'.format(primeiro_nuemero, segundo_numero, div))

    elif operador == '*':
        mul= int(primeiro_nuemero * segundo_numero)
        print('{} * {} = {}'.format(primeiro_nuemero, segundo_numero, mul))
    
    else:
        print('O operador inserido não foi válido 😓, tente novamente.')

    novamente()

def novamente():
    calc_nov = input('''
Você deseja efetuar uma nova operação?
Digite S para sim e N para não.
''')

    if calc_nov.upper() == 'S':
        calculadora()
    elif calc_nov.upper() == 'N':
        print('Até mais 👋.')
    else:
        novamente()

calculadora()