nome= input('Qual é o seu nome? ')
idade= eval(input('Qual é a sua idade (informe somente números)? '))
altura= eval(input('Qual é a sua altura (informe somente números e pontos)? '))
peso= eval(input('Qual é o seu peso aproximadamente (informe somente números e pontos)? '))

IMC = peso // altura ** 2

print ( '{} tem {} e possui {} de altura e pesa {} Kg' . format (nome, idade, altura, peso))
print ( 'O IMC de {} é {:.2f}'. format (nome, IMC))

