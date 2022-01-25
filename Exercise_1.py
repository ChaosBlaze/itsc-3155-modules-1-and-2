# Group Members: Shekar Balasubramaniam, Ivory Steed, Paul Thottappilly, Hassan Chugtai

def getLetterGrade(score):
    score = round(score)
    grades = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]
    for i in range(len(grades)):
        if score >= grades[i][0]:
            return grades[i][1]