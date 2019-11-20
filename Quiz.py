#To Hip or Not to Hop???

def question_one():
    response = input("What year was the Slim Shady LP released? A) 1991 B) 1977 C) 1985 D) 1999 ")

    if response == "D":
        print("That's right!")
        return 1
    else: 
        print("Sorry, the correct answer is D) 1999")
        return 0

def question_two():
    response2 = input("What is the name of Kanye's 5th studio album? A) Late Registration B) The Life of Pablo C) MBDTF D) College Dropout ")

    if response2 == "C":
        print("You got it!")
        return 1
    else:
        print("Incorrect, the right answer is C) MBDTF.")
        return 0

def question_three():
    response3 = input("Did Kanye West sample Through the Wire? Type T for true or F for false ")

    if response3 == "T":
        print("Wrong.")
        return 0
    elif response3 == "F":
        print("Right!")
        return 1
    else:
        return response3

def question_four():
    response4 = input("Who is this legendary Memphis rap group that won an Academy Award for best original song in 2006? A) Wutang Clan B) Young Money C) Mobb Deep D) Three 6 Mafia ")

    if response4 == "D":
        print("That was right!")
        return 1
    else:
        print("Incorrect.")
        return 0

def question_five():
    response5 = input("Whose debut album is Illmatic? A) Nas B) Ja Rule C) Travis Scott D) Flava Flav")

    if response5 == "A":
        print("That is correct!")
        return 1
    else:
        print("Sorry that was incorrect.")
        return 0


total_score = 0
result = question_one() + question_two() + question_three() + question_four() + question_five()
total_score += result
print(total_score)