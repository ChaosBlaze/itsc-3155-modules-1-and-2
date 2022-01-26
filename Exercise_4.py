# Group Members: Shekar Balasubramaniam, Ivory Steed, Paul Thottappilly, Hassan Chugtai

from statistics import mean

def Average(list) :
    return mean(list)

list = 11
k = 1

n = int(input("Enter a number: ") )

for i in range(0, n):
    nnums = float(input("Enter number " + str(k) +": "))
    list.append(nnums)
    k = k+1

average = Average(list)
print ("List:", list)
print ("Average:", average)