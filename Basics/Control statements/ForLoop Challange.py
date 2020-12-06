"""Write a program that takes an I.P. adress entered on a keyboard and
prints out the number of segments it contains, and the length of each segment.
    Example of valid inputs:
        127.0.0.1
        10.12344.456.111
    Example of invalid inputs:
        10.10t.10.10
        123.4567.459.789."""

#_________________My Solution_____________________#
# iP = input("Enter a valid IP address")
# strNumbers = ""
# for i in range(len(iP)):
#     if iP[i] not in '0123456789':
#         continue
#     strNumbers += iP[i]
#     print(len(strNumbers))
# intNumbers = int(strNumbers)
# print(intNumbers)

#_________________Tim's Solution___________________#
ipAddress = input("Enter an IP address: ")

segment = 1
segLenth = 0
char = ""

for char in ipAddress:
    if char == ".":
        print("segment {} contains {} charecters".format(segment, segLenth))
        segment += 1
        segLenth = 0
    else:
        segLenth +=1