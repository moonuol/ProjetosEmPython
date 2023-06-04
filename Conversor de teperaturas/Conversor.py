inicio ='Bem vindo ao Converosr de Temperatura!\nFaça conversão de temperatura para Kelvin (K), Celsius (C) e Fahrenheit (F).\n'
print(f'{inicio.upper()}')          #Tudo em maiúsculo

#entrada do usuário
def entrada():
    print('''Escolha a operação que deseja fazer:
          1. Kelvin (K) para Celsius (C)
          2. Kelvin (k) para Fahrenheit (F)
          3. Celsius(C) para Kelvin (K)
          4. Celsius(C) para Fahrenheit (F)
          5. Fahrenheit (F) para Kelvin (K)
          6. Fahrenheit (F) para Celsius(C)''')
    
    global opcao        #ser acessível em todas as funções
    global temp         # idem
    
    opcao= input('\nQual a operação escolhida? ')
    temp= float(input('\nQual a temperatura? '))            #converte de string para float
    
    resolucao()         #chama a função

#Cálculo das conversões das temperaturas
def calcKC():           #1
    calculo = round(temp - 273)             #round arredonda
    print(f'\nA resposta é: {calculo} ºC')
    adeus()

def calcKF():           #2
    calculo = round( 1.8 * (temp - 373) + 32)
    print(f'\nA resposta é: {calculo} ºF')
    adeus()
    
def calcCK():           #3
    calculo = round(temp + 273)
    print(f'\nA resposta é: {calculo} K')
    adeus()
    
def calcCF():           #4
    calculo = round((temp*1.8) + 32)
    print(f'\nA resposta é: {calculo} ºF')
    adeus()
    
def calcFK():           #5
    calculo = round((temp-32)*(5/9)+273 )
    print(f'\nA resposta é: {calculo} K')
    adeus()
    
def calcFC():           #6
    calculo = round((temp-32)/1.8)
    print(f'\nA resposta é: {calculo} ºC')
    adeus()

#Chamar a função conforme a entrada do usuário
def resolucao():
    if opcao == '1':
        calcKC()
    elif opcao == '2':
        calcKF()
    elif opcao == '3':
        calcCK()
    elif opcao == '4':
        calcCF()
    elif opcao == '5':
        calcFK()
    elif opcao == '6':
        calcFC()
    else:
        invalido()


#Caso haja uma entrada diferente da do esperado       
def invalido(): 
    print('\nEntrada inválida')
    inval = input('\n Para tentar novamente digite S, para sair digite N: ').upper()
    if inval == 'S':
        entrada()
    if inval == 'N':
        adeus()

#Despedida        
def adeus():
    print('\nAté a próxima!')

entrada()