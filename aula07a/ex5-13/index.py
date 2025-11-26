#Exercício 5) faça um program que leia um número inteiro e mostre na tela o seu sucessor e antecessor.

# abaico código usando .format

# n1= int(input('digite um número:'))
# print ('O valor digitado foi: {} \n seu sucessor é: {} \n seu antecessor é: {}'. format(n1, n1+1, n1-1))

 #abaixo código usando f-strings

# n1 = int(input('digit um número:'))
# print (f'o número digitado foi: {n1}\n o sucessor é: {n1+1} \n o antecessor é: {n1-1}')


# fazendo do modo abaixo, se precisar usar o antecessor e sucessor, fica melhor para usar as variáveis correspondentes individualmente.
# n1= int(input('digite um número:'))
# a = n1-1
# s = n1+1
# print ('O valor digitado foi: {} \n seu sucessor é: {} \n seu antecessor é: {}'. format(n1, a, s))


# Exercício 6) crie um algoritmo que leia um número e mostre o seu dobro, típlo e raiz quadrada.

# n1 = int(input('digite uma número:'))
# x2 = n1*2
# x3 = n1*3
# rq = n1 ** 0.5

# print ('o número digitado foi: {} \n seu dobro é;{} \n seu tiplo é:{}\n sua raiz quadrada é:{}'.format(n1, x2, x3, rq))

#posso fazer direto também

# n1 = int(input('digite uma número:'))
# print('o número digitado foi:{} \n seu dobro é:{} \n seu triplo é:{} \n sua raiz quadrada é:{:.2f}' .format (n1, n1*2, n1*3, n1**(1/2)))


# Exercício 7) desenvolva um programa que leia as duas notas de uma aluno, calcule e mostre a sua média.

# n1 = float(input('digite a 1a. nota:'))
# n2 = float(input('digite a 2a. nota:'))
# m = (n1+n2) /2
# # print('1a. nota é:{} \n 2a. nota é:{} \n a média é:{}' .format(n1, n2, m))
# print(f'a 1a. nota é: {n1} \n a 2a. nota é: {n2} \n a nédia é: {m}')
#abaixo acrescentei if else como condição
# if m >= 6:
#     print('PARABÉNS! você está APROVADO!')
# else:
#     print('ATENÇÃO! você está em RECUPERAÇÃO! dedique-se mais aos estudos!')

# Exercício 8) escreva um programa que leia um valor em mt, e o exiba em cm e mm

#no caso abaixo converti o valor de cm e mm para int para o resultado ficar inteiro com um visual mais limpo

# n1 = float(input('digite um valor em metros:'))
# cm = int(n1 * 100)
# mm = int(n1 * 1000)
# print ('valor em metros:{}mt. \n valor em cm:{}cm. \n valor em mm:{}mm. '.format (n1, cm, mm))

 #Exercício 9) faça um  programa que leia um número inteiro qualquer e moastre na tela a sua tabuada.

# n1 = int(input('digite um número de 1 a 10 e te mostro a tabuada dele:'))
# t = n1*1, n1*2, n1*3, n1*4, n1*5, n1*6, n1*7, n1*8, n1*9, n1*10
# print ('o número digitado foi:{} \n sua tabuada é:{}' .format (n1, t))

# n = int(input('digite um número de 1 a 10 e veja sua tabuada:'))
# print('{}x1={} \n {}x2={} \n {}x3={} \n {}x4={} \n {}x5={} \n {}x6={} \n {}x7={} \n {}x8={} \n {}x9={} \n {}x10={}' .format(n, n*1, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))

#abaixo usei :2 na segunda mascara{:2} para o resultado do print ficar alinhado.
# num = int(input('digite um número e veja sua tabuada:'))
# print('x' * 13)
# print('{} x {:2} = {}'.format(num, 1, num*1))
# print('{} x {:2} = {}'.format(num, 2, num*2))
# print('{} x {:2} = {}'.format(num, 3, num*3))
# print('{} x {:2} = {}'.format(num, 4, num*4))
# print('{} x {:2} = {}'.format(num, 5, num*5))
# print('{} x {:2} = {}'.format(num, 6, num*6))
# print('{} x {:2} = {}'.format(num, 7, num*7))
# print('{} x {:2} = {}'.format(num, 8, num*8))
# print('{} x {:2} = {}'.format(num, 9, num*9))
# print('{} x {:2} = {}'.format(num, 10, num*10))
# print('x' * 13)




# exercício 10) escreva um programa que leia quanto a pessoa tem na carteira e mostre quantos dólares ela pode comprar. considere que o dólar vale r$5.20

#abaixo adcionei (:.2f)na mascara {}de dólares para limitar o resultado a duas casas decimais.
# v1 = int(input('digite quanto você tem em r$:'))
# d = float(5.20)
# print('Você possui r${} com esse valor você pode comprar {:.2f} dólares.' .format (v1, v1/d))

#exercício 11) faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la , sabendo que  cada litro de tinta, pinta uma área de 2 mt2.

# L = float(input('digite a largura da parede em metros:'))
# A = float(input('digite a altrura da parede em metros:'))
# area = L*A 
# QT = area/2
# print('Sua parede tem:{} mt2 de largura \n {} mt2 de altura. formando uma área de {} mt2 \n  vão ser necessários {} litros de tinta para pintá-la.' .format (L, A, area, QT))


#exercício 12) faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

# p1 = float(input('digite o valor do produto:r$'))
# vcd = p1 * 0.05
# print ('O valor desse produto é: r${} \n com 5% de desconto vai para r${}' .format (p1, p1-vcd))

#outra forma de fazer(com f.string)
# preço = float(input('digite o valor do produto:r$'))
# np = preço - (preço * 5 / 100)
# print (f'O valor do produto é:r${preço} \n com desconto de 5% você vai pagar:r${np:.2f}')


#exercício 13) faça u algortítimo que leia o salário do funcionário e mostre seu novo salário com 15% de almento.

# salario = float(input('digite seu salário atual:r$'))
# sca = salario + (salario * 15 / 100) 
# print ('Esse é seu salário atual:r${} \n Esse é seu salário com almento de 15%:r${:.2f}' .format (salario, sca))

# s1 = float(input('digite seu salário atual:r$'))
# sa = s1 * 0.15
# print(f'O seu salário de :r${s1} com 15% de almento vai para :r$ {s1+sa}')

#exercício 14) escreva um programa que converta uma temperatura degitada em °C para °F.

# tc = float(input('Digite a temperatura em °C para ver a conversão em °F:°C'))
# tf = tc*9/5 +32
# print ('A temperatura digitada em °C é:°C{} \n Aqui está a temperatura convertida em °F:°F{}' .format (tc, tf))


#exercício 15) escreva um algorítimo que pergunte a quantidade de Km percorrido por um carro aluado e a quantidade de dias pelos quais foi alugado. calcule o preço a pagar. sabendo que o carro custa r$60 por dia e r$0.15 por Km rodado.

# print ('***CALCULE O VALOR A PAGAR PELO ALUGUEL DO CARRO***')

#abaixo usando .format
# al = float(input('O carro está alugado por quantos dias?:'))
# km = float(input('Rodou quantos kilômetros com o carro?:'))
# print ('O aluguel do carro fica em :r${} \n o Preço por km rodado fica em :r${} \n Total dos serviços :r${}' .format (al*60, km*0.15, (al*60) + (km*0.15)))

#abaixo usando f.string
# al = float(input('Ficou com o carro por quantos dias?:'))
# km = float(input('Rodou por quantos kilômetros?:'))
# print (f'O valor por {al} dias de aluguel do automóvel fica em:r${al*60} \n O valor por {km}km rodados fica em:r${km*0.15} \n O Total a pagar pelo aluguel do altomóvel é:r${(al*60) + (km*0.15)} ')