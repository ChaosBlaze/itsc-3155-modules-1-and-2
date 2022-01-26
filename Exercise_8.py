# Group Members: Shekar Balasubramaniam, Ivory Steed, Paul Thottappilly, Hassan Chugtai


lst = []
newlst = []

for i in range(10):
    nums = int(input('Enter a number: '))
    lst.append(nums)

for x in lst:
    if(lst.count(x) == 1):
        newlst.append(x)

print(newlst)
