# Group Members: Shekar Balasubramaniam, Ivory Steed, Paul Thottappilly, Hassan Chugtai

lst1 =[]
evenLst = []

# input gender
while True:
    entry = input("Enter a number or QUIT: ")
    if entry == "QUIT":
        break
    
    lst1.append(int(entry))

for x in lst1:
    if x % 2 == 0:
        evenLst.append(x)

print(evenLst)