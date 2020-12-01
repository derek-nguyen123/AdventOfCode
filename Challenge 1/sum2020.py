def sum2020(nums, target):
    """
    :type nums = List[str]
    :type target = int
    :rtype: int
    """
    # Create a set to store any values we looked at already
    checked = set()
    for index, num in enumerate(nums):
        # Complement is the required number to reach the target
        complement = target - int(num)
        # See if we have already found the complement in the list
        if(complement in checked):
            # If we have, return the product of the two numbers
            return (int(num) * complement)
        # Otherwise, add the current number to the checked numbers
        else:
            checked.add(int(num))

inputFile = open("input.txt", "r")
inputLines = inputFile.read().splitlines()
inputFile.close()
result = sum2020(inputLines, 2020)
print(result)
