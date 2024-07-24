def minFinalGrade(midterm):

    scoretobeCompleted = 60
    finalGrade = ((scoretobeCompleted - (midterm*(0.4)))) / 0.6
    return finalGrade

#Receiving data input from the user
midterm = float(input("Enter midterm grade:"))
print(f"Midterm Grade : {midterm}")

#scoretobeCompleted = float(input("Write the average required to pass:"))
#print(f"Minimum Score is: {scoretobeCompleted}")

finalGrade = minFinalGrade(midterm)
print(f"Minimum final grade required : {finalGrade : .2f}")
        