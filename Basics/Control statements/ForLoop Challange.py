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