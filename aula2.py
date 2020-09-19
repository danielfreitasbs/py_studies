a = int(input('Entre com o primeiro valor: \n'))
b = int(input('Entre com o segundo valor: \n'))
soma = a + b
sub = a - b
multiply = a * b
div = a / b
resto = a % b

print('soma: {soma}. '
      '\nSubtracao: {sub}. '
      '\nMultiplicação: {mult}. '
      '\nDivisao: {div}. '
      '\nResto: {resto}.'
      .format(soma=soma, sub=sub, mult=multiply, div=div, resto=resto))

# x = '1'
# soma2 = int(x) + 1
# print(soma2)
