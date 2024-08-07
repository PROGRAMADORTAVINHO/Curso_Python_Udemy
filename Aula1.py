"""
DocString

"""

print(12, 34, sep= "-") # Sep : Separado
print(56, 78, sep= '/')

# Escape -> \
print("João \"Otavio\"")

# A função type mostra o tipo que o Python inferiu ao valor.
print(type('Otávio'))
print(type(0))
print(type(1.1))
print(type(10 == 10))
print(type(False))
print(type(1.1), type(-1), type(0.0))

# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

# Se Sobrar 0 é par, se sobrar é impar

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)

# Contatenação
contatenacao = "João" + " " + "Otavio"
print(contatenacao)

a_dez_vezes = "A" * 10
tres_vezes_joao = 3 * "João"
print(a_dez_vezes)
print(tres_vezes_joao)

# Precedência entre os operadores
"""
    1. (n + n)
    2. **
    3. * / // %
    4. + - 
"""

# Exercicio: Calculo do IMC

nome = "João Otavio"
massa = 91.9
altura = 1.75

imc = massa / altura ** 2

print(f"{nome} tem {altura}m de altura, pesa {massa}KG e seu IMC é {imc:.2f}")

# f-string
# Se for dinheiro ex: 100,050.40 
salario = 100050.40
print(f"{salario:,.2f}")