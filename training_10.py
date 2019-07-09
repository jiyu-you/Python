def inc( a=1, step=1):
    return a + step
    
b=1
b= inc(b)
print(b)
b=inc( b, 10)
print(b)
print(inc())

def area(height, width):
    return height * width

area( 10, 20 ) 
area( width = 20, height = 10 )
area( 20, width = 10 )

def varg( *arg, a):
    print( a, arg2 )

varg( 1 )
varg( 2, 3 )
varg( 2, 3, 4, 5, 6 )





def f2(*arg, **kw)
    print( arg )
    print( kw )

f2( 1, 2, width-10, height-20 )
f2( 3, 4, 5, 6, width = 10, height = 20, depth = 30, dimension= 5 )
f2( 10 )
f2(10, width = 10 )
f2( 10 )
f2( 10, 100, width = 100 )

def h(a, b, c):
    print(a, b, c)

args = (1, 2, 3)
h(*args)

