# Group Members: Shekar Balasubramaniam, Ivory Steed, Paul Thottappilly, Hassan Chugtai
# Links below indicate help found online
# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

user_string = input("Enter a string: ")
user_string = str(user_string)

def split(user_string):
    return list(user_string)
user_string = (split(user_string))

n = 3
split_list = [user_string[i * n:(i +1) * n] for i in range ((len(user_string) + n - 1) // n)]
print(split_list)