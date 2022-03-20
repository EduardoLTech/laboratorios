'''
Exercicio
Python

nome = input('Entre com seu nome: ')
idade = input('Qual sua idade? ')
idade = str(idade)
cidade = input('Onde vc mora? ')

print('O ' + nome + ' tem ' + idade + ' anos e mora na cidade de ' + cidade + '.')


ano_nascimento = input('Qual ano de nascimento? ')
ano_nascimento = int(ano_nascimento)
ano_corrente = 2022

print(ano_corrente - ano_nascimento)


fruta = 'Melancia'
#index   01234567
print(fruta[-7])


nome = 'Eduardo'
sobrenome = 'Lopes'
profissao = 'Programador'

texto = f'O {nome} {sobrenome} é um excelente {profissao}'

print(texto.replace(old, new))

# O Eduardo Lopes é um excelente Programador


velocidade =111


if velocidade > 110:
    print('Reduza a velocidade')
elif velocidade < 60:
    print('O cachorro ta mijando na roda')
else:
    print('Velocidade OK')
    


idade = 9

resultado = 'voto permitido' if idade >= 16  else 'voto nao permitido'

print(resultado)




for numero in range(1, 15):
    print(numero)
    
for letra in 'Curso Udemy':
    print(letra)    

 
 
 
compra_confirmada = True
dados_compra = 'Compra efetuada e entrega confirmada'
 
for entrega in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes no seu email')
        break
    else:
        print('Falha na compra')
        break



for numero1 in range(5):
    print('Produto' + str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)



palavra = 'feliz natal'

for espaco in palavra:
    print(f'{espaco.upper()} ', end='')        


valor = 100
dia = 0

while valor > 20:
    dia += 1
    print(f'Valor do produto: {valor} no dia {dia}')
    valor -= 5



def soma_numero():
    num1 = int(input('Entre com primeiro numero: '))
    num2 = int(input('Entre com segundo numero: '))
    result = num1 + num2
    print(f'O resultado da soma é {result}')
    
    
soma_numero()




def boas_vindas(nome, quantidade):
    print(f'Ola {nome}')
    print(f'Temos {str(quantidade)} notebooks.')
    

boas_vindas('duda', 3)
boas_vindas('ellen', 2)    



def calc():
    n1 = 2
    n2 = 3
    result = n1 + n2
    print(result)
    return result
    
y = calc()
print(f'valor {y}')




def soma(*numero):
    resultado = 0
    for num in numero:
        resultado += num
    return resultado
        
y = soma(2,3,5,1)
print(y)                



import math

print(math.factorial(5))



mercado = ['sabonete', 'feijão', 'arroz', 'pipoca', 5, 6, 7, 8]
numeros = [2, 4, 5, 6, 9]


item1, item2, item3, item4, *resto = mercado


print(item1)
print(item4)
print(resto)



valores = [50, 60, 80, 100, 120, 170]
for x in valores:
    print(x)



cores = ['verde', 'amarelo', 'azul', 'branco']
numeros = [10, 20, 30, 40]


junta_lista = zip(cores, numeros)

print(list(junta_lista))    


from array import array


letras = ['a', 'b', 'c', 'd']
numeros_i = [1, 2, 3, 4]
numeros_f = [1.0, 2.0, 3.0, 4.0]


print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [1, 2, 3, 4])
numeros_f = array('f', [1.2, 2.2, 3.2, 4.2])

print(letras)
print(numeros_i)
print(numeros_f)


aluno = {'nome': 'eduardo', 'curso': 'python', 'nota': 9.5}

#aluno['nome'] = 'ellen'
#aluno.update({'nome': 'duda', 'nota': 8})
aluno.update({'endereço': 'Rua 5'})

print(aluno.get('endereço', 'Nao existe'))


def soma(x):
    y = lambda x: x + 3
    return y(x) + 4

print(soma(3))




list1 = [1, 2, 3, 4]

#def multi(x):
#   return x * 2

#print(list(map(multi, list1)))

print(list(map(lambda x: x * 2, list1)))



valores = [10, 19, 22, 45, 67]

def somenteabaixode20(x):
    return x < 20

print(list(filter(somenteabaixode20, valores)))
 


temp = int(input('Entre com a temperatura: '))

if temp < 48:
    print('Precisa assar mais!!')
elif 48 <= temp < 54:
    print('Está selada.')
elif 54 <= temp < 60:
    print('Ao ponto para o mal.')
elif 60 <= temp < 65:
    print('Ao ponto.')
elif 65 <= temp < 71:
    print('Ao ponto para o bem.')                  
else:
    print('Ta bem passado')    




def lata_tinta ():
    largura_parede = int(input('Entre com a largura da parede: '))
    altura_parede = int(input('Entre com a altura da parede: '))
    rendimento_lata = int(input('Entre com o rendimento da lata de tinta: '))
    area = largura_parede * altura_parede
    rend = area / rendimento_lata
    return rend

result = lata_tinta()
print(f'Será necessário {result} latas de tinta.')



funcionarios = {'ana', 'marcos', 'alice', 'pedro', 'sofia', 'bruno', 'melissa'}
turno_dia = {'ana', 'marcos', 'alice', 'melissa'}
turno_noite = {'pedro', 'sofia', 'bruno'}
tem_carro = {'marcos', 'alice', 'bruno', 'melissa'}


carro_noite = tem_carro.intersection(turno_noite)
print(f'Tem carro e trabalha a noite: {carro_noite}')

carro_dia = tem_carro.intersection(turno_dia)
print(f'Tem carro e trabalha de dia: {carro_dia}')

sem_carro = funcionarios.symmetric_difference(tem_carro)
print(f'Funcionario que nao tem carro: {sem_carro}')

'''


altura = float(input(f'Entre com sua altura em cm: '))
peso = float(input(f'Entre com seu peso em Kg: '))


imc = peso / (altura/100) ** 2
  

if imc < 18.5:
    print(f'Seu IMC é de {imc}. Vc está seco.')
elif imc >= 18.5 and imc < 24.9:
    print(f'Seu IMC é de {imc}. Peso normal')
elif imc >= 25.0 and imc < 29.9:
    print(f'Seu IMC é de {imc}. Ta gordo.')
elif imc >= 30.0 and imc < 39.9:
    print(f'Seu IMC é de {imc}. Ta obeso.')
else:
    print(f'Seu IMC é de {imc}. Ta indo pro saco')
            


    






    
         
     
         
 
 
 