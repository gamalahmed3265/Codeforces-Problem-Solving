def wMirrorArray(n:int ,m:int ,a:list):
  for i in range(n):
      for res in a[i][::-1]:
        print(res,end=" ")
      print()

def main():
  arr=[]
  n, m= list(map(int, input().split()))
  for i in range(n):
    arr.append(list(map(int, input().split())))
  
  wMirrorArray(n,m,arr)
if __name__ == "__main__":
  main()