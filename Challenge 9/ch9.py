def isSum(lines):
    '''
    :type lines = List[str]
    :rtype: int
    '''
    for index in range(25, len(lines)):
        target = lines[index]
        # Create a set from the "preamble" for which we will twoSum
        pool = set(lines[index-25:index])
        hasPair = False
        # If the current target has a twoSum in the preamble, return nothing
        for num in pool:
            complement = target - num
            if (complement in pool):
                hasPair = True
                break
        if(not hasPair):
            return target


def partialSum(goal, lines):
    '''
    :type goal = int
    :type lines = List[str]
    :rtype: int
    '''
    # Create a list of partial sums to find the partial sum that is the goal
    partSum = [0]
    accumulation = 0
    for line in lines:
        accumulation += int(line)
        partSum.append(accumulation)
    # Iterate through the list of partial sums
    for index in range(len(partSum)):
        index2 = index + 2
        while 0 <= index2 < len(partSum) and partSum[index2] - partSum[index] <= goal:
            # If the difference in partial sums at two indexes meets our goal
            if(partSum[index2] - partSum[index] == goal):
                # The partial sum to meet the goal is between those two indexes
                return(max(lines[index:index2]) + min(lines[index:index2]))
            index2 += 1
    return -1


file = open("input.txt", "r")
lines = file.read().splitlines()
lines = [int(l) for l in lines]
file.close()
goal = isSum(lines)
print(goal)
print(partialSum(goal, lines))