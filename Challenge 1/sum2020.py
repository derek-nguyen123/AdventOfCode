def sum2020(nums, target):
    """
    :type nums = List[str]
    :type target = int
    :rtype: int
    """
    checked = set()
    for index, num in enumerate(nums):
        complement = target - int(num)
        if(complement in checked):
            return (int(num) * complement)
        else:
            checked.add(int(num))

inputFile = open("input.txt", "r")
inputLines = inputFile.read().splitlines()
result = sum2020(inputLines, 2020)
print(result)
