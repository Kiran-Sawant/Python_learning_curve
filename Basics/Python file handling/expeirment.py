with open('sample.txt', mode='r') as poem:
    lines = poem.readline()
    while lines:
        print(lines, end='')
        lines = poem.readline()
