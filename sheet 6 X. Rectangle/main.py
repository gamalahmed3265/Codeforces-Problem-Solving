
def point_belongs_to_rectangle(x1,y1,x2,y2,x3,y3,x4,y4,x,y):
    maxX=max(x1,x2,x3,x4)
    minX=min(x1,x2,x3,x4)
    maxY=max(y1,y2,y3,y4)
    minY=min(y1,y2,y3,y4)
    
    return maxX>=x>=minX and maxY>=y>=minY

def main():
    x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
    n=int(input())
    
    for _ in range(n):
        x,y =map(int,input().split())            
        if point_belongs_to_rectangle(x1,y1,x2,y2,x3,y3,x4,y4,x,y):
            print("YES")
        else:
            print("NO")


if __name__ =="__main__":
    main()