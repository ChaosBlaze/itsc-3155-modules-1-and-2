# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chugtai, Tony Le
# Links below indicate help found online
# https://www.kite.com/python/answers/how-to-print-a-list-without-brackets-in-python#:~:text=Use%20*%20to%20print%20a%20list,set%20sep%20to%20%22%2C%20%22%20.


row_num = int(input("Enter a row num from 1 to 5: "))
col_num = int(input("Enter a col num from 1 to 5: "))

grid = [([0] * 5) for i in range(5)]
grid[row_num - 1][col_num - 1] = 1

for i in grid:
    print(*i, sep = ' ')