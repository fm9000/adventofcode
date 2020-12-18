import re

with open('input') as f:
    Rawinput = f.read().splitlines()


def Separator(String):
    # What's the Regular Expression to split up the String?
    RegExp = r"(\d*)-(\d*) (.): (.*)"
    Match = re.search(RegExp, String)

    return Match

def Evaluator_1(Match):
    Min = int(Match.group(1))
    Max = int(Match.group(2))
    Char = Match.group(3)
    Passwort = Match.group(4)

    # How often does the Char appear in the passwort?
    Count = Passwort.count(Char)

    # Is the password valid?
    return Min <= Count <= Max


# Counter for Valids Part 1
Valids_1 = 0

for PasswortString in Rawinput:
    Valids_1 += Evaluator_1(Separator(PasswortString))

print(f"Solution for Part 1: {Valids_1}")



#### Part 2
print("\n")

def Evaluator_2(Match):
    Pos_1 = int(Match.group(1))
    Pos_2 = int(Match.group(2))
    Char = Match.group(3)
    Passwort = Match.group(4)

    # Is "Pos_1 XOR Pos_2" equal to Char?
    return (Passwort[Pos_1 - 1] == Char) ^ (Passwort[Pos_2 - 1] == Char)


# Counter for Valids Part 2
Valids_2 = 0

for PasswortString in Rawinput:
    Valids_2 += Evaluator_2(Separator(PasswortString))

print(f"Solution for Part 2: {Valids_2}")