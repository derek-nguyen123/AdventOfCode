def countYes(groups):
    """
    :type groups = [str]
    :rtype: (int, int)
    """
    # Start counting for parts 1 and 2 of question
    part1, part2 = 0, 0
    # Check every set of applications
    for group in groups:
        # Find all distinct letters in the set of applications
        letters = set(''.join(group.split('\n')))
        part1 += len(letters)
        # For every letter, check if they exist in the rest of applications per group
        for letter in letters:
            # Check each person
            for person in group.split('\n'):
                # If one person is missing the letter, don't increase
                if (letter not in person) and (person != ''):
                    break
            else:
                part2 += 1
    return(part1, part2)

file = open("input.txt", "r")
groups = file.read()
groups = groups.split("\n\n")
print(countYes(groups))