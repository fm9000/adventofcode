import re

with open('input') as f:
    Rawinput = f.read()

# Splitting at the empty line
lines = Rawinput.split("\n\n")

# In each element there is a string that needs parsing


def Parser(InputString):
    # Replacing \n with a whitespace
    Entry = InputString.replace("\n", " ")

    # Splitting at the whitespace
    # Now looks like that
    # ['ecl:gry',
    # 'pid:860033327']
    list_KV = Entry.split(" ")

    # Now there is a list of "key:value" strings
    # Splitting them up again and turn them into a dictionary
    
    PassportDict = {}
    for KeyValue in list_KV:
        Key, Value = KeyValue.split(":")

        PassportDict[Key] = Value

    return PassportDict

# Create a list of all passports
list_Passports = []

for Passport in lines:
    list_Passports.append(Parser(Passport))


def Validity_1(PassportDict):
    '''
    Validity check for the first part
    '''

    # Required fields:
    Required_Fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    # When is the passport valid?
    # When the difference between the set of "Required_Fields"
    # and the passport keys is empty
    result = Required_Fields - set(PassportDict.keys())

    return not bool(result)


# Create a list of all evaluations
Evaluations = [Validity_1(Passport) for Passport in list_Passports]

print("Solution for part 1:")
print(sum(Evaluations))




### Part 2
print("\n")


def HeightCheck(Angabe):
    RegExp = "^(\d*)([i,c][n,m])$"

    Match = re.match(RegExp, Angabe)

    # If there is a matched object, the boolean of Match is true
    if bool(Match):
        Unit = Match.group(2)
        Value = int(Match.group(1))

        if Unit == "cm":
            return 150 <= Value <= 193
        
        elif Unit == "in":
            return 59 <= Value <= 76
        
        else:
            return False

    else:
        return False

def Validity_2(PassportDict):
    # When is a passport valid?
    # When all elements in the Checks list are True
    Checks = []

    # Required fields:
    # Same check as in Validity_1
    Required_Fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    bool_Fields = not bool(Required_Fields - set(PassportDict.keys()))
    Checks.append(bool_Fields)

    # For each field in the passport, use different functions to evaluate their value
    Evaluationrules =  {"byr" : lambda x: 1920 <= int(x) <= 2002,
                        "iyr" : lambda x: 2010 <= int(x) <= 2020,
                        "eyr" : lambda x: 2020 <= int(x) <= 2030,
                        "hgt" : HeightCheck,
                        "hcl" : lambda x: bool(re.match("^[#][0-9a-f]{6}$", x)),
                        "ecl" : lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                        "pid" : lambda x: bool(re.match("^\d{9}$", x)),
                        "cid" : lambda x: True}

    # Check every Key/Value from the passport
    for Key, Value in PassportDict.items():
        # Get the evaluation function from the Evaluationrules dictionary
        Evaluationfunction = Evaluationrules.get(Key)

        # Instanciate that function with the value from the passport
        Result = Evaluationfunction(Value)

        Checks.append(Result)

    return all(Checks)

# Create a list of all evaluations
Evaluations = [Validity_2(Passport) for Passport in list_Passports]

print("Solution for part 2:")
print(sum(Evaluations))