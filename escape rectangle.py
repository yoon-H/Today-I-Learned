x,y,w,h = input().split( )
x=int(x)
y=int(y)
w=int(w)
h=int(h)

hor = ( x if x<w-x else w-x)
ver =(y if y<h-y else h-y)

num = (hor if hor<ver else ver)

print(num)
