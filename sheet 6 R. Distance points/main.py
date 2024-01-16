import math
def distance (x1,y1,x2,y2):
    return math.sqrt(
        math.pow(x2-x1,2)+
        math.pow(y2-y1,2)
    )

def distancePoints(x1,y1,x2,y2):
    
    print(distance(x1,y1,x2,y2))
    

def main():
    x1,y1,x2,y2=map(int,input().split())
    
    distancePoints(x1,y1,x2,y2)

if __name__ =="__main__":
    main()