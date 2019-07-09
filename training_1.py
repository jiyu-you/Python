'''
    inputprint.py

'''
number1 = int(input( '첫 번째 정수를 입력하시오 : ' ))
number2 = int(input( '두 번째 정수를 입력하시오 : ' ))

result_add = number1 + number2
result_sub = number2 - number1
result_mul = number1 * number2
result_div = number2 / number1
result_div2 = number2 // number1
result_mod = number2 % number1

print( '{0:2} + {1:2} = {2:2}'.format( number1, number2, result_add))
print( '{0:2} - {1:2} = {2:2}'.format( number2, number1, result_sub))
print( '{0:2} * {1:2} = {2:2}'.format( number1, number2, result_mul))
print( '{0:2} / {1:2} = {2:.2f}'.format( number2, number1, result_div))
print( '{0:2} // {1:2} = {2:2}'.format( number2, number1, result_div2))
print( '{0:2} % {1:2} = {2:2}'.format( number2, number1, result_mod))




