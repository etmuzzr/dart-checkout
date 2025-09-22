from board import board
import sys

def get_checkout(score, throws=3, darts=[]):
    #Base cases where a winning throw cannot be made
    if (score < 2 or score > 170) or (throws == 0 and score != 0):
        return []
    
    for location, value in board.items():
        #Not a possible throw since the value on the board is too high
        if value > score:
            continue

        darts.append(location)
        #If the last dart is a double AND there is no remaining score to be made, this is one possible winning throw
        if value == score and location[0] == "D": 
            return darts
        
        #Recursively search for the next possible throw
        res = get_checkout(score - value, throws - 1, darts)
        if res:
            return res
        
        #Backtrack if not a valid solution
        darts.pop()

if __name__ == "__main__":
    score = int(sys.argv[1])
    print(get_checkout(score))
