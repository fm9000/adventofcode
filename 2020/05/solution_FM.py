with open("input") as f:
    Rawinput = f.read().splitlines()


def SplitString(String):
    '''
    Splitting the string in two parts: Row and column
    '''
    Row = String[:7]
    Col = String[-3:]

    return Row, Col

def CodeToDecimal(String):
    '''
    Convert the string to a decimal int number
    '''

    Replace = { "F" : "0",
                "B" : "1",
                "L" : "0",
                "R" : "1" }

    for Char, Number in Replace.items():
        String = String.replace(Char, Number)
        
    return int(String, 2)

def GetRowCol(String):
    '''
    Convert the string to a tuple of row and column
    '''

    Row, Col = SplitString(String)

    Row = CodeToDecimal(Row)
    Col = CodeToDecimal(Col)
    return Row, Col    

def GetBoardingpassID(Row, Col):
    '''
    Logic to calculate the boarding pass ID
    '''
    return Row * 8 + Col

# A list for all the calculated boarding pass IDs
BP_IDs = []
for BP in Rawinput:
   Row, Col = GetRowCol(BP)
   BP_IDs.append(GetBoardingpassID(Row, Col))

# Task1:
Max_BP = max(BP_IDs)
print("Solution for part 1:")
print(Max_BP)

# Task2:
Min_BP = min(BP_IDs)
set(range(Min_BP,Max_BP)) - set(BP_IDs)
print("Solution for part 2:")