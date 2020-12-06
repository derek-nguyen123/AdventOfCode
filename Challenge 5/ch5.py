def findSeatID(seatCode):
    """
    :type seatCode = str
    :rtype: int
    """
    # Use the two helper function to determine seat id from the string.
    return (parseSeat(seatCode[0:len(seatCode)-3], 0, 127) * 8) + parseSeat(seatCode[len(seatCode)-3:len(seatCode)], 0, 7)


def parseSeat(seatCode, min, max):
    """
    :type seatCode = str
    :type min = int
    :type max = int
    :rtype: int
    """
    # Base case, if on the last character of the string
    if(len(seatCode) == 1):
        # If B or R, take the upper
        if (seatCode[0] == "B" or seatCode[0] == "R"):
            return max
        # Otherwise take lower
        else:
            return min
    # Recursively determine seatID by checking each character and manipulating min/max values
    for character in seatCode:
        if(character == "B" or character == "R"):
            return((parseSeat(seatCode[1:len(seatCode)], (max + min + 1)//2, max)))
        elif(character == "F" or character == "L"):
            return((parseSeat(seatCode[1:len(seatCode)], min, (max + min - 1)//2)))
    return -1


def findMySeat(seatCodes):
    """
    :type seatCodes = str
    :rtype: int
    """
    # Create a set of all seatCodes
    mySet = []
    for seat in seatCodes:
        mySet.append(findSeatID(seat))
    mySet.sort()
    # Find the missing seat code
    for index, seatID in enumerate(mySet):
        if(mySet[index + 1] - seatID == 2):
            return seatID + 1


file = open("input.txt", "r")
lines = file.read().splitlines()
result = 0
for line in lines:
    temp = findSeatID(line)
    if(temp > result):
        result = temp
print(result)
print(findMySeat(lines))
