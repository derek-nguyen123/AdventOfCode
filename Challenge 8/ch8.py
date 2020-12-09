def accumulate(operations):
    """
    :type operations = List[str]
    :rtype: int
    """
    # Create a set of checked indices to know if we are looping infinitely
    checked = set()
    # Track results + checked indices
    result = 0
    index = 0
    while index < len(operations):
        line = operations[index].split()
        if(index in checked):
            # break instead of return None for part 1
            return None
        checked.add(index)
        # Parse the command, increasing result and/or index accordingly
        if(line[0] == "nop"):
            index = index + 1
            continue
        elif(line[0] == "acc"):
            result = result + int(line[1])
            index = index + 1
        elif(line[0] == "jmp"):
            index = index + int(line[1])
    return result


def check(operations):
    """
    :type operations = List[str]
    :rtype: int
    """
    for index in range(len(operations)):
        temp = operations[:]
        line = operations[index].split()
        # Replace the line with jmp or nop, see if the accumulate function will terminate
        if(line[0] == "jmp"):
            temp[index] = operations[index].replace("jmp", "nop")
        elif(line[0] == "nop"):
            temp[index] = operations[index].replace("nop", "jmp")
        attempt = accumulate(temp)
        if(attempt):
            return attempt
    return None


file = open("input.txt", "r")
operations = file.read().splitlines()
file.close()
print(accumulate(operations))
print(check(operations))
