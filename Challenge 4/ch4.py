import re

def validPassports(passports):
    """
    :type: passports = List[str]
    :rtype: int
    """
    # Count the number of valid passports encountered
    validPassports = 0
    for passport in passports:
        # Ensure that the passport has all required fields
        hasFields = True
        for field in fields:
            try:
                passport.index(field)
            except:
                # If a field is missing, passport is invalid
                hasFields = False
                break
        # If the passport has all required fields
        if(hasFields):
            # Split the passport into each of its fields
            splitFields = passport.split()
            # Ensure that all fields have valid data
            validFields = True
            # Check every field
            for pair in splitFields:
                if(not validate(pair)):
                    # If a field is found to have invalid data, passport is invalid
                    validFields = False
                    break
            # If the passport has valid data
            if(validFields):
                validPassports = validPassports + 1
    return validPassports


def validate(pair):
    """
    :type pair = str
    :rtype: bool
    """
    # Split the field into the key and value pair
    key, value = pair.split(':')
    # Check the field by its key
    if (key == "byr"):
        return (len(value) == 4) and (1920 <= int(value) <= 2002)
    if (key == "iyr"):
        return (len(value) == 4) and (2010 <= int(value) <= 2020)
    if (key == "eyr"):
        return (len(value) == 4) and (2020 <= int(value) <= 2030)
    if (key == "hgt"):
        if ("cm" in value):
            height = value.split("cm")
            return 150 <= int(height[0]) <= 193
        elif ("in" in value):
            height = value.split("in")
            return 59 <= int(height[0]) <= 76
    if (key == "hcl"):
        return re.fullmatch(r'#[0-9,a-f]{6}', value)
    if (key == "ecl"):
        return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if (key == "pid"):
        return re.fullmatch(r'[0-9]{9}', value)
    if (key == "cid"):
        return True
    return False


fields = {"byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"}
file = open("input.txt", "r")
passports = file.read()
passports = passports.split("\n\n")
file.close()
print(validPassports(passports))