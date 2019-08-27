lines = []
while True:
    s = input()
    #s = "Hello world Practice makes perfect"
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print (sentence)