def sum2020Helper(nums, target):
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

def sum2020(nums, target):
    for index, num in enumerate(nums):
        if(index == len(nums)-2):
            return null
        twoSum = sum2020Helper(nums[index+1:len(nums)], target - int(num))
        if(twoSum):
            return int(num) * twoSum
            
    
inputFile = open("input.txt", "r")
inputLines = inputFile.read().splitlines()
inputFile.close()
result = sum2020(inputLines, 2020)
print(result)
