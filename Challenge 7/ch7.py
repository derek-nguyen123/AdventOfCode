def defineBags(rules):
    """
    :type rules = List[str]
    :rtype: dict{str : List[int, str]}
    """
    # Create the empty dictionaries to store rules per bag type
    ruleDict = {}
    for rule in rules:
        # Split the rule into the corresponding bag/rule pair
        (bag, rule) = rule.split(" contain ")
        # Replace any form of bag, or bags to a consistent "bags."
        rule = rule.replace("bag,", "bags.").replace("bag.", "bags.").replace("bags,", "bags.")
        ruleSplit = rule.split(". ")
        # A list to break down the rule side further
        fixedRules = []
        for rule in ruleSplit:
            # Take care of case with no other bags.
            if(rule == "no other bags."):
                fixedRules.append(0)
                fixedRules.append("no other bags")
                continue
            # Take the corresponding number + bag pair to store with bag key
            fixedRules.append(int(rule[0]))
            # Take care of trailing periods
            if rule[len(rule) - 1] == ".":
                fixedRules.append(rule[2:len(rule)-1])
            else:
                fixedRules.append(rule[2:len(rule)])
        # Add bag key pair to dictionary
        ruleDict[bag] = fixedRules
    return ruleDict


def canFit(target, bags, counted = set()):
    """
    :type target = str
    :type bags = dict {str : List[int, str]}
    :type counted = set
    :rtype: int
    """
    # Track number of bags that can hold the target
    result = 0
    for bag in bags:
        # Check if it has been counted already and if it fits the target bag
        if target in bags[bag] and bag not in counted:
            counted.add(bag)
            # Find number of bags that fit the bag that fits the target
            result = result + 1 + canFit(bag, bags, counted)
    return result


def countBags(target, bags):
    """
    :type target = result
    :type bags = dict {str : List[int, str]}
    :rtype: int
    """
    # Track number of bags inside the target
    result = 0
    index = 0
    # Iterate through the bags that the target holds
    while index < len(bags[target]):
        nextBag = bags[target][index+1]
        if(nextBag == "no other bags"):
            return 0
        # Add the number of the bag, then the amount of bags inside those bags * the amount of that bag
        result = result + bags[target][index] + bags[target][index]*countBags(nextBag, bags)
        # Go to the next bag
        index = index + 2
    return result


file = open("input.txt", "r")
lines = file.read().splitlines()
file.close()
bags = defineBags(lines)
print(canFit("shiny gold bags", bags))
print(countBags("shiny gold bags", bags))
