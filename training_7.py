def func():             # 인수 없고, return 값도 없는 경우
    print('function1)')

def func2(a):           # 인수 있고, return 값이 없는 경우
    print(a)

def func3():           # 인수 없고, return 값이 있는 경우
    return 5+10

def func4(a):           # 인수 있고, return 값도 있는 경우
    total=0
    for value in a:
        total += value
        return total

# 함수 호출
func()
func2(5)
func2((5,10))
func2([1,2,3,4,5])
func2({'one':1, 'two':1, 'three':3})

print(func3())
print(func4((1,2,3,4,5,6,7,8,9,10)))

def gg(t):
    #t=[1,2,3]
    t[1]=60
    return

a=[5,6,7]
gg(a)
print(a)

x=10
y=11
def foo():
    global x
    x = 20
    def bar():
            a=30
            print(a,x,y)
            return

    bar()
    x=40
    bar()
    return

foo()
print(x,y)

def calc_sum(start, end):
    sum = 0
    
    for number in range(start, end+1):
        sum += number

    return sum

print(calc_sum(1,10))

def slice_str(string_list):
    slice_string_list=[]
    for string in string_list:
        slice_string_list.append(string[:3])   
    return slice_string_list

string_list=['Seoul','Busan','Daejeon','Daegu','Jeju']
slice_string=slice_str(string_list)
print(slice_string)
