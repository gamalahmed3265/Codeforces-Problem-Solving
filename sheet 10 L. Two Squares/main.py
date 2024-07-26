import math
def main():
    l_s1_s2=[int(i) for i in input().split()]
    for i in range(int(input())):
        area=int(input())
        lq=math.sqrt(area)
        dif=l_s1_s2[0]-lq
        t=dif/abs(l_s1_s2[1]-l_s1_s2[2])
        print(math.sqrt(2)*t)

main()        



###################### way 2

import math
# Read input values
L ,S1 ,S2 =list(map(float,input().split()))
numQ=int(input())
for _ in range(numQ):
    q = float(input())
    time = math.sqrt(2) * (L - math.sqrt(q)) / abs(S2 - S1)
    print(f"{time:.6f}") 
