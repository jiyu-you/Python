'''
1. 두 개의 정수를 입력받아 평균을 반환하는 함수를 작성\
(첫 번째 수가 -1이면 종료)
'''
def calc_average(number1, number2):
    return(number1+number2)/2
'''
2. 입력받은 내용을 리스트에 저장 후 리스트를 전달받아 최대값과 최소값을 반환하는 함수 작성
(-1이 입력될 때 까지 입력 받아 리스트에 저장)
'''
def max_min_select(data_list):
    maximum = sys.float_info.min
    minimum = sys.float_info.max

    for value in data_list:
        if value > maximum:
            maximum = value

        if value < minimum:
            minimum = value

    return maximum, minimum

number1 = int( input( '첫 번째 정수 입력 ( -1 : quit ) : ' ) )
while ( number1 != -1 ):
    number2 = int( input( '두 번째 정수 입력 : ' ) )
    print( '\n{0:5} 과 {1:5}의 평균값은 : {2:7.2f}\n'.format( number1, number2, calc_average( number1, number2 ) ) )
    number1 = int( input( '첫 번째 정수 입력 ( -1 : quit ) : ' ) )

3. 
number_list = []

number = int( input( '\n정수 입력 ( -1 : 입력 종료 ) : ' ) )
while ( number != -1 ):
    number_list.append( number )
    number = int( input( '정수 입력 ( -1 : 입력 종료 ) : ' ) )

input( '\nPress any key to program stop...' )

