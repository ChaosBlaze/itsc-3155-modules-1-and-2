# Group Members: Shekar Balasubramaniam, Ivory Steed, Paul Thottappilly, Hassan Chugtai

def perfectSquares(l, r):
 
    # For every element from the range
    for i in range(l, r + 1):
 
        # If current element is
        # a perfect square
        if (i**(.5) == int(i**(.5))):
            print(i, end=" ")
 
# Driver code
l = input('Enter an integer ')
r = input('Enter an integer ')