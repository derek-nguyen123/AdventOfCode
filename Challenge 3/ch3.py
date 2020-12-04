def howManyTrees(lines, right, down):
    """
    :type lines = List[str]
    :type right = int
    :type down = int
    :rtype: int
    """
    # Count the total number of trees encountered
    numTrees = 0
    # Track the current index of string to check independent of list index
    stringIndex = 0
    lineLength = len(lines[0])
    for index, line in enumerate(lines):
        # Skip number of necessary lines
        if(index % down != 0):
            continue
        # Check the stringIndex
        if(line[(stringIndex) % lineLength] == '#'):
            numTrees = numTrees + 1
        # if a line was processed, increase string index
        stringIndex = stringIndex + right
    return numTrees


file = open("input.txt", "r")
lines = file.read().splitlines()
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
file.close()
result = 1
for (right, down) in slopes:
    result = result * howManyTrees(lines, right, down)
print(result)
