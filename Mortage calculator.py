print("Welcome to mortage calculator")
salary=int(input("What is your salary?"))
if salary >= 2000:
    print("You are eligible for a mortage")
    credit_score=int(input("What is your credit score?"))
    if credit_score >= 900 and credit_score <=1000:
        rate=3
        print("Interest rate is 3%")
    elif credit_score >800:
        rate=4
        print("Interest rate is 4%")
    elif credit_score >700:
        rate=6
        print("Interest rate is 6%")
    else:
        print("Interest rate is 8%")
    disability=input("Do you have any disability?,YorN.")
    if disability=="Y":
        rate -=2
    print(f"Final interest rate is:{rate}%")
else:
    print("sorry,you are not eligible")