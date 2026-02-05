score_1 = float(input("Enter your first score: "))
score_2 = float(input("Enter your second score: "))
if score_1 > 20 or score_1 < 0 and score_2 > 20 or score_2 < 0 :
    print ("invalid, please try again")
elif score_1 >= 18 and score_1 <= 19.75 and score_2 >= 18 and score_2 <= 19.75 :
    print ("you passed")
elif score_1 < 18 or score_2 < 18 :
    print ("you failed")
elif score_1 == 20 and score_2 == 20 :
    print ("You passed with perfect score, now you can choose between normal classes and special classes")
Type_of_class = input("Which one do you want?")
if Type_of_class == "normal classes" :
    print ("The price for normal classes are 200$")
elif Type_of_class == "special classes" :
    print ("The price for special classes are 499$")
paying = input("How do you want to pay, cash or card?")
if paying == "card" :
    print ("Great, The amount must be transfered one week before the start of classes.")
elif paying == "cash" :
    print ("Great, The amount must be transfered one week before the start of classes.")
print ("The classes start on 25 june")
print ("Thank you for your time")




