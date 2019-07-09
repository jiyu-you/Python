'''
문제 : 10명의 학생 점수를 입력받아 평균 이하의 학생을 출력하는 프로그램

data : 10명 학생 성적 저장 공간 - students : list

algorithm : 1. 10명 학생 성적을 입력 받는다. 
            2. 입력 받은 학생 성적중 평균 이하의 학생 출력한다.

함수 : inputdata() - 10명 학생 성적 입력 함수
       calcaverage() - 평균을 계산하는 함수
       printdata() - 평균 이하의 학생을 출력하는 함수  
'''
def inputdata():
    '''
        1. 10번 반복하면서
            1.1 한번 반복할때 마다 학생 성적 입력
    '''
    students=[]
    for i in range (10):
        student = int(input('학생 성적 입력:'))
        students.append( student )

    return students

def calcaverage( students ):
    '''
        1. 10명의 총점을 계산한다.
        2. 계산된 총점에 대한 평균을 구한다. 
    '''
    total=0
    for student in students:
        total += student
    average = total / 10

    return average

def printdata( students ):
    '''
         1. 10번 반복하면서(학생수 만큼 반복하면서)
            1.1 한번 반복할때 마다 평균 점수 이하이면 학생 정보 출력
    '''
    average = calcaverage( students )
    for student in students:

        if student <= average:
            print( student )

    return


students = inputdata()
printdata( students )

