from board import board
import sys

def get_checkout(score, throws=3, darts=[]):
    if (score < 2 or score > 170) or (throws == 0 and score != 0):
        return []
    
    for location, value in board.items():
        if value > score:
            continue

        darts.append(location)
        if value == score and location[0] == "D":
            return darts
        
        res = get_checkout(score - value, throws - 1, darts)
        if res:
            return res
        
        darts.pop()

if __name__ == "__main__":
    score = int(sys.argv[1])
    print(get_checkout(score))
