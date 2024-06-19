charactersArranged="qwertyuiopasdfghjkl;zxcvbnm,./"

direction=input()

message=input()
for msg in message:
    postionChar=charactersArranged.find(msg)
    if direction=="R":
        print(charactersArranged[postionChar-1],end="")
    else:
        print(charactersArranged[postionChar+1],end="")