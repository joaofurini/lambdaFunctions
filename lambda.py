#EXPLICACAO SOBRE FUNCOES ANONIMAS EM PYTHON
#Em python temos dois tipos de funcoes, as normais e as funcoes lambda 
#as funções lambdas nada mais sao do que funcoes anonimas
#a seguir desmontrarei uma simples funcao que soma dois numeros do jeito normal e do jeito lambda 

#SOMAR DOIS NUMEROS COM FUNCAO NORMAL
'''
def somaNum(n1, n2):
	return n1 + n2

print(somaNum(int(input("Digite um numero: ")), int(input("Digite seu outro numero: "))))'''
#Simples né?
#Porem isso pode ser ainda mais reduzido usando funcoes lambda

#Farei a mesma função abaixo usando lambda functions

'''soma_num_lambda = lambda n1, n2: n1+n2
print("A soma dos dois numeros é: {}"\
	.format(soma_num_lambda(int(input("Digite um numero: ")), \
		int(input("Digite outro numero: ")))))'''

#Ok agora vamos ao que aconteceu aqui
#O que esta acontecendo aqui é atribuimos uma função anonima a uma variavel (soma_num_lambda), a funcao recebe n1 e n2 separados por virgula
#e retornamos o valor usando : e escrevendo o algoritmo usado depois dos dois pontos

#Podemos ainda, para simplificar mais ainda, usar lambda functions sem parametros, e pedir os parametros necessarios dentro da propria funcao,
#Da seguinte forma

'''soma = lambda: int(input("Digite um numero: ")) + int(input("Digite outro numero: "))
print("A soma dos numeros e: {}".format(soma()))
'''
#muito simples

#Mas onde usamos isso no mundo real?
#Normalmente lambda functions sao usadas quando precisamos passar uma funcao como parametro
#Como no seguinte exemplo 
#Precisamo de um programa que tira a media de duas notas 
#Primeiro criaremos uma funcao normal que recebe a soma de dois numeros, e o numero para ser divido

def tiraMedia(n1, n2):
	return n1/n2

#Agora na hora de chamar essa funcao, chamaremos passando uma lambda function como parametro
soma = lambda: int(input("Digite um numero: ")) + int(input("Digite outro numero: "))

print(tiraMedia(soma(), 2))

