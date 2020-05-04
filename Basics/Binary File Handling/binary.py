with open('binary', mode='bw') as binFile: #'bw' is for binary write mode
    for i in range(17):
        binFile.write(bytes([i])) # bytes method converts the iterable/int into bytes

with open('binary', mode='br') as binFile: # 'br' is for bytes read
    for b in binFile:
        print(b)
 
#______________________writing integers to a binary file_________________________#

a = 65534       # FF FF
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open('binary2', mode='bw') as binFile:
    binFile.write(a.to_bytes(2, 'big')) # '2' for number of bytes
    binFile.write(b.to_bytes(2, 'big')) # 'big' for big endian ordering
    binFile.write(c.to_bytes(4, 'big')) # .to_byte() converts the passed int to binary
    binFile.write(x.to_bytes(4, 'big'))
    binFile.write(x.to_bytes(4, 'little'))

with open('binary2', mode='br') as binFile:
    e = int.from_bytes(binFile.read(2), 'big')
    print(e)
    f = int.from_bytes(binFile.read(2), 'big')
    print(f)
    g = int.from_bytes(binFile.read(4), 'big')
    print(g)
    h = int.from_bytes(binFile.read(4), 'big')
    print(h)
    i = int.from_bytes(binFile.read(4), 'big') # here the line stored in little ndian is read in big endian format
    print(i)