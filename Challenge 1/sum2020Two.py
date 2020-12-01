def sum2020Helper(nums, target):
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


def sum2020(nums, target):
    """
    :type nums = List[str]
    :type target = int
    :rtype: int
    """
    # Iterate through the list of input
    for index, num in enumerate(nums):
        # If there are only two numbers left in the list
        if(index == len(nums)-2):
            # There is no solution
            return null
        # Complement is the second integer such that the current num + that num
        complement = target - int(num)
        # Use sum2020Helper to find two numbers in the remainder of the list
        twoSum = sum2020Helper(nums[index+1:len(nums)], complement)
        if(twoSum):
            return int(num) * twoSum


inputFile = open("input.txt", "r")
inputLines = inputFile.read().splitlines()
inputFile.close()
result = sum2020(inputLines, 2020)
print(result)
