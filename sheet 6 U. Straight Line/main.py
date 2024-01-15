
def straightLine(X1, Y1, X2, Y2, X3, Y3):
    m1=(Y3 - Y2) * (X2 - X1)
    m2=(Y2 - Y1) * (X3 - X2)
    
    return m1==m2
    

def main():
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
   
    print("YES" if straightLine(x1,y1,x2,y2,x3,y3) else "NO")

if __name__ =="__main__":
    main()