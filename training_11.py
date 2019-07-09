'''
    1. 10명의 학생 이름, 점수를 입력 받아, 10명의 학생 이름, 점수를 출력하고
    최고점 학생 정보, 최저점 학생 정보, 평균 점수, 점수대 인원수를 출력
    하는 프로그램(함수로 구현)
'''
def inputdata():
    students=[]
    for student in range (3):
        student = str(input('학생 이름 입력:'))
        student = int(input('학생 점수 입력:'))
        students.append( student )

    return students

def calcaverage( students ):
    total=0
    for student in students:
        total += student
    average = total / 3

    return average

def printdata( students ):
    average = calcaverage( students )
    for student in students:
        if student <= average:
            print( student )

    return


def max_min_select(student):
    maximum = max(student)
    minimum = min(student)

    for student in students:
        if student > maximum:
            maximum = student

        if student < minimum:
            minimum = student

    return maximum, minimum

 
students = inputdata()
printdata( students )   
max, min = max_min_select( students )
print( 'max : {0}\tmin : {1}'.format( max, min ) )
    

