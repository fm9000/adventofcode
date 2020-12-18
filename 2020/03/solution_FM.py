import numpy as np

with open('input') as f:
    Rawinput = f.read().splitlines()

# The strings have to be translated
Translation = {"." : 0,
               "#" : 1}


def AsciiToInt(String, Translationdict):
    '''
    Function to convert the ".##.#..#"-string into a list of integers
    '''

    list_Result = []
    
    # list(String) turns the input string into a list
    # This works as strings are iterable
    for Entry in list(String):
        Translation = Translationdict.get(Entry, np.nan)
        list_Result.append(Translation)

    return list_Result


# list_Array will be the list where the whole input gets stored
list_Array = []

for line in Rawinput:

    # Translate to integer
    int_row = AsciiToInt(String=line, Translationdict=Translation)
    
    # Appending this row to the list_Array
    list_Array.append(int_row)



# Converting into a numpy array
input_array = np.array(list_Array)

# What's the slope of our movement?
# (X-direction, Y-direction)
Slope = (3,1)




def Treecounter(Slope, Array):
    '''Given a slope and an array, count the occurences of trees
    '''

    # How many rows in total do we have?
    Rows = Array.shape[0]

    # Create a list of all the coordinates we have to check
    X_Coords = list(range(0,9999,Slope[0])) # Sloppy to set the upper limit to 9999
    Y_Coords = list(range(0,Rows,Slope[1]))

    # Those coordinates will be zipped.
    # As the Y-Coords are exhausted earlier than X_Coords,
    # the upper 999 limit doesn't matter
    Coordinates = list(zip(X_Coords, Y_Coords))

    # Counting the number of trees
    Treecounter = 0

    for X, Y in Coordinates:
        # What's the value at the given coordinate? Use wrapping!
        Value = np.take(Array[Y,:], indices=X, axis=0, mode="wrap")
        Treecounter += Value

    return Treecounter



print("Solution for part 1:")
print(Treecounter(Slope=Slope, Array=input_array))


### Part 2
print("\n")

# We have several slopes now
Slopes = [(1,1),
          (3,1),
          (5,1),
          (7,1),
          (1,2)
          ]


Results = []
for Slope in Slopes:
    Results.append(Treecounter(Slope=Slope, Array=input_array))

print("Solution for part 2:")
# Multiplication of all the results
print(np.prod(Results))