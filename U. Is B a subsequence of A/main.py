def uIsBaSubsequenceOfA(a:list,b:list):
  i=0
  j=0
  while i < len(a) and j < len(b):
      if a[i] == b[j]:
        j += 1
      i += 1

  return j == len(b)

def main():
  sizeArr, sizeSubseq= list(map(int, input().split()))
  arr=list(map(int, input().split()))
  arrSubseq=list(map(int, input().split()))
  
  if uIsBaSubsequenceOfA(arr,arrSubseq)==True:
    print("YES")
  else:
    print("NO")
  
if __name__ == "__main__":
  main()
def main():
  sizeArr, sizeSubseq= list(map(int, input().split()))
  arr=list(map(int, input().split()))
  arrSubseq=list(map(int, input().split()))
  
  if uIsBaSubsequenceOfA(arr,arrSubseq)==True:
    print("YES")
  else:
    print("NO")
  
if __name__ == "__main__":
  main()