# Dissecando uma variável

a = input ('Digite algo:')
print ('o tipo primitivo desse valor é:', type (a))
print ('só tem espaços?', a.isspace())
print ('é um número?', a.isnumeric())
print ('é alfabético?', a.isalpha())
print ('é alfanumérico?', a.isalnum())
print ('está em maiúsculas?', a.isupper())
print ('está em minúsculas?', a.islower())
print ('está capitalizada?', a.istitle())
