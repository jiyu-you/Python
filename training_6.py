1. 다음과 같이
 출력하는 프로그램
   ( 10명이내 이름이 'end'이면 결과 출력, 90이상 Excellent 60이하 Fail )

    Hong 50 50 50 150 50.0 Fail
    Kim  90 90 90 270 90.0 Excellent
    Nam  70 70 70 210 70.0
'''
print( ''.center( 80, '=' ) )
print( question_str )
print( ''.center( 80, '=' ) )
print()

MAX = 10
SUBJECT = 3

students = []
count = 0

name = input( '학생 이름 입력 ( "end" : quit ) : ' )
while name != 'end' and count < MAX:
    count = count + 1
    subjects = []
    total = 0
    for x in range( SUBJECT ):
        subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( SUBJECT, x + 1 ) ) )
        while ( subject < 0 or subject > 100 ):
            print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
            subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( SUBJECT, x + 1 ) ) )

        subjects.append( subject )
        total += subject

    average = total / SUBJECT
    
    if average >= 90:
        grade = 'Excellent'
    elif average <= 60:
        grade = 'Fail'
    else:
        grade = ' '

    student = []
    student.append( name )
    student.append( subjects )
    student.append( total )
    student.append( average )
    student.append( grade )

    students.append( student )
    
    name = input( '\n학생 이름 입력 ( "end" : quit ) : ' )

print()
for student in students:
    print( '{0:<10}'.format( student[ 0 ] ), end = '' )
    for subject in student[ 1 ]:
        print( '{0:3}'.format( subject ), end = '' )
    print( '{0:5} {1:6.2f} {2:<10}'.format( student[ 2 ], student[ 3 ], student[ 4 ] ) )

input( '\nPress any key to program stop...' )

l=[[3, 1], [2, 1], [1, 1]]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][0]<l[j][0]:
            l[i][1] += 1 

for value in l:
    print('{0:3}{1:3}'.format(value[0], value[1])) 

2. 1번 문제를 dictioinary를 이용하여 구현한 프로그램
Hong=(['subject1', 'subject2', 'subject3'], [50])
Kim=(['subject1', 'subject2', 'subject3'], [90])
Nam=([subject1', 'subject2', 'subject3', [70])

Hong=['subject1':50]
Hong=['subject2':50]
Hong=['subject3':50]
a={'Hong':['subject1':50]}
b={'Hong':['subject2':50]}
c={'Hong':['subject3':50]}

dic[a,b,c]

