header = list()
with open('header.txt') as openfile:
    for line in openfile:
        words = line.split()
        word = words[1].split(':')[0]
        header.append(word)

print(header)
print(len(header))
