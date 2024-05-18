def count_suitable_rooms():
  """Counts the number of rooms with free space for George and Alex.

  Returns:
      The number of suitable rooms.
  """
  n = int(input())  # Read number of rooms
  suitable_rooms = []

  for i in range(n):
    pi, qi = map(int, input().split())  # Read people and capacity for each room
    if qi - pi >= 2:
      suitable_rooms.append(i + 1)  # Append room number (starting from 1)

  return len(suitable_rooms)

# Example usage
result = count_suitable_rooms()
print(result)

####################################### 

# other way



n=int(input())

result=0
for i in range(n):
    nP,c=map(int,input().split()) # number of people , capacity
    if (c-nP)>=2:
        print(result)
        result+=1

print(result)