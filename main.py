#Exercícios Moodle

#Exercício 1
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
mediabimestral= (nota1 + nota2 + nota3 + nota4)/4
mediabimestral= f"{mediabimestral:.2f}"
print('\nNota 1: {}, Nota 2: {}, Nota 3: {}, Nota 4: {} \nMedia Bimestral:{}'.format(nota1, nota2, nota3, nota4, mediabimestral))

#Exercício 2
metros = float(input('Quantos metros são? '))
z = metros * 1000
print('\nA quantidade de metros, ',metros,'equivale a',z,'milímetros' )

#Exercício 3
lado = float(input('Qual a medida do lado do quadrado? '))
area = lado * lado
z = area * 2
print('\nLado: {}, \nÁrea do quadrado: {}, \nDobro da área: {}'.format(lado, area, z))

#Exercício 4
ganho = float(input('Quanto você ganha por hora? '))
horas = float(input('Quantas horas você trabalha no mês?'))
salario = ganho * horas
print('\nCom o ganho de {} reais por hora em 1 mês, sendo trabalhadas {} horas durante o mesmo. \nSeu salário mensal total é de {} reais.'.format(ganho, horas, salario))

#Exercício 5
altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc = peso/(altura*altura)
imc = f"{imc:.2f}"
print('\nCom as informações recebidas sobre o peso de {}kg, e a altura de {}m. \nSeu IMC (índice de massa corporal) é de: {}kg/m².'.format(peso, altura, imc))