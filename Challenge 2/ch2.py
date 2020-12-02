def validPasswords(policies):
    """
    :type policies = List[List[str], str, str]
    :rtype: int
    """
    # Count the numbeer of valid passwords
    numValid = 0
    # Iterate through all password policies
    for policy in policies:
        # Ensure that the number of desired character is between two constraints
        if(int(policy[0][0]) <= policy[2].count(policy[1]) <= int(policy[0][1])):
            numValid = numValid + 1
    return numValid


def validPasswords2(policies):
    """
    :type policies = List[List[str], str, str]
    :rtype: int
    """
    # Count the number of valid passwords
    numValid = 0
    # Iterate through all of the passwords
    for policy in policies:
        # Split the list into corresponding parts
        password = policy[2]
        positions = (int(policy[0][0]), int(policy[0][1]))
        character = policy[1]
        # Check that either positions have it
        if(password[positions[0]-1] == character or password[positions[1]-1] == character):
            # Make sure both of them don't have it
            if((not (password[positions[0]-1] == character and password[positions[1]-1] == character))):
                numValid = numValid + 1
    return numValid


def readPasswordInput(passwords):
    """
    :type passwords = List[str]
    :rtype: List[List[str], str, str]
    """
    # List to store the parsed strings
    fixed = []
    # Iterate through all policies in the list of policies
    for password in passwords:
        # Split the password policy into each part
        fixedLine = password.split()
        # Get the two number constraints
        fixedLine[0] = fixedLine[0].split("-")
        # Locate the required character
        fixedLine[1] = fixedLine[1][0]
        # Take new line symbol off of the resulting string
        fixedLine[2] = fixedLine[2].strip('\n')
        fixed.append(fixedLine)
    return fixed


file = open("input.txt", "r")
lines = file.readlines()
listPasswordInput = readPasswordInput(lines)
result = validPasswords(listPasswordInput)
print(result)
result2 = validPasswords2(listPasswordInput)
print(result2)
file.close()