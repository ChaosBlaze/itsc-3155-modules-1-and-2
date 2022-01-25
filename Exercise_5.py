# Group Members: Shekar Balasubramaniam, Ivory Steed, Paul Thottappilly, Hassan Chugtai

def findCommon(ar1, ar2, ar3, n1, n2, n3):

    i, j, k = 0, 0, 0
      
    while (i < n1 and j < n2 and k< n3):
        
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print(ar1[i]),
            i += 1
            j += 1
            k += 1
        
        # when x < y    
        elif ar1[i] < ar2[j]:
            i += 1
            
        # when y < z    
        elif ar2[j] < ar3[k]:
            j += 1
        
        else:
            k += 1

# Driver program to check above function
ar1 = input('Enter elements of a list separated by space ')
ar2 = input('Enter elements of a list separated by space ')
ar3 = input('Enter elements of a list separated by space ')

n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)

print("Common elements are"),
findCommon(ar1, ar2, ar3, n1, n2, n3)
