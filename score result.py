score = float(input("Enter your score: "))
if score < 0 or score > 100 :
    print ("invalid")
elif score == 100 :
    print ("perfect score")
elif score <= 99.75 and score >= 80 :
    print ("very good")
elif score < 80 and score >= 60 :
    print ("good")
else :
    print ("You failed")        