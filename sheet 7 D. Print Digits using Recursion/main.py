
N=int(input())

def sample(N):
    
    if N==0:
        return
    else:
        t=int(input())
        print(*list(str(t)))

        sample(N-1)

sample(N)