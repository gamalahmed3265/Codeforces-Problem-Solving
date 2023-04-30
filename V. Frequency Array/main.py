def vFrequencyArray(n:int ,m:int ,a:list):
  counts = {}
  for i in range(1, m + 1):
    counts[i] = 0

  for i in range(n):
    counts[a[i]] += 1

  for number, count in counts.items():
    print(count)

def main():
  n, m= list(map(int, input().split()))
  arr=list(map(int, input().split()))
  
  vFrequencyArray(n,m,arr)

if __name__ == "__main__":
  main()