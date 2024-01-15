
def parallelLine(X1, Y1, X2, Y2, X3, Y3, X4, Y4):
    m1=(Y2-Y1)*(X4-X3)
    m2=(Y4-Y3)*(X2-X1)
    
    return m1==m2
    

def main():
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=map(int,input().split())
    print("YES" if parallelLine(x1,y1,x2,y2,x3,y3,x4,y4) else "NO")

if __name__ =="__main__":
    main()