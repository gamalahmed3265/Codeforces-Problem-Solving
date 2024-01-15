import math

def centerPoints(a,b):
    return (a+b)/2

def diameterCircle(a1,b1,a2,b2):
    return math.sqrt(
        math.pow(a1-a2,2)+math.pow(b1-b2,2)
    )

def circles_intersect(X1, Y1, X2, Y2, X3, Y3, X4, Y4):
    xm1=centerPoints(X1,X2)
    ym1=centerPoints(Y1,Y2)
    xm2=centerPoints(X3,X4)
    ym2=centerPoints(Y3,Y4)
    
    raduis1=(diameterCircle(X1, Y1, X2, Y2))/2
    raduis2=(diameterCircle(X3, Y3, X4, Y4))/2
    
    distance=diameterCircle(xm1,ym1,xm2,ym2)

    return distance <= (raduis1+raduis2)

def main():
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=map(int,input().split())
    print("YES" if circles_intersect(x1,y1,x2,y2,x3,y3,x4,y4) else "NO")

if __name__ =="__main__":
    main()