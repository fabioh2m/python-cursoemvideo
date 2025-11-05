#usando f-strings abaixo é o mais moderno

# n1 = input ('digite um número:')
# n2 = input ('digite outro número:')
# s = int(n1) +  int(n2)
# print (f'a soma entre {n1} e {n2} é: {s}')

# usando o .format abaixo é o mais tradicional

# n1 = input ('digite um número:')
# n2 = input ('digite outro número:')
# s = int(n1) +  int(n2)
# print ('a soma entre {} e {} é: {}' .format (n1, n2, s))

# n1 = input ('digite um número:')
# n2 = input ('digite outro número:')
# s = int(n1) + int(n2)
# print ('a soma entre os números é: {}' .format (s))

#abaixo código para calcular o imc.


print ('Descubra seu índice de massa corporal-IMC!')
nome = input ('Digite seu nome:')
peso = float (input ('digite seu peso em kg:'))
altura = float (input('digite sua altura em metros:'))
imc = peso / (altura ** 2)
print ('{} Seu índice de massa corporal é:{}' . format (nome, imc))

if imc < 18.5:
    print (f'Cuidado {nome} ! Você está abaixo do peso ideal!') 

if imc >= 18.5 and imc < 25 :
    print (f'Parabéns {nome}! Você está no peso ideal!')

if imc >= 25 and imc < 30:
    print (f'Cuidado {nome} ! Você está com sobrepeso!')    

if imc >= 30 :
    print (f'Atenção {nome} ! Você está com obesidade!')    

