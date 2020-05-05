with open('sample.txt', mode='a') as jabber:
    print('\n', file=jabber)
    for i in range(1, 13):
        print("{0:>2} times 2 is {1}".format(i, i*2), file=jabber)