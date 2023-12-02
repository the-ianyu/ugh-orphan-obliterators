import datetime, sys

points = 1 ** 0 - 1
number_of_trips = 0
reviews = []
numbers = "1234890"
numbers2 = "01"
numbers3 = "1234567890"
free_ride = 0
free_kms = 0

def leave():
    exit = input("Exit program? (Y/N):  ")
    if exit.lower() == "y":
        print(f"You have {points} points.")
        print("Goodbye! Have a nice day.")
        sys.exit()
    return 

while True:
    count = 0
    print("")
    print("What would you like to do?")
    print("Press 1 for a ride")
    print("Press 2 for a transit option")
    print("Press 3 to redeem rewards")
    print("Press 4 to use rewards")
    print("Press 8 to check amount of points")
    print("Press 9 to give a review")
    print("Press 0 to leave")
    choice = input("Option: ")
    print("")

    for each in numbers:
        if each == choice:
            choice = int(choice)
            count = count + 1
            break
        if count == 1:
            print("Invalid option, please choose again:")
            break
    
    if choice == 1:
        number_of_trips = number_of_trips + 1
        if number_of_trips == 1:
            print("First ride: +50 points")
            points = points + 50
        else:
            print("Points for each ride: +5 points")
            points = points + 5
        type_of_ride = input("Type of ride: (ESML):")
        if type_of_ride.lower() == "s":
            print("Eco-valid car, low levels of emissions: +3 points")
            points = points + 3
        elif type_of_ride.lower() == "e":
            print("Electric car, 0 emissions: +5 points")
            points = points + 5
        elif type_of_ride.lower() == "m" or type_of_ride.lower() == "l":
            print("Normal car")
        else:
            print("Invalid")
        originaltime = datetime.datetime.now()
        time = originaltime.strftime("%H%M")
        time = int(time)
        if time >= 500 and time <= 729:
            print("Early bird promo: +3 points")
            points = points + 7
        elif time >= 1600 and time <= 1659:
            print("Before rush hour promo: +5 points")
            points = points + 5
        elif time >= 2130 and time <= 2359:
            print("Late owl promo: +7 points")
            points = points + 3
    
    elif choice == 2:
        follow_map = input("Did you follow the map? 1 = yes, 0 = no: ")
        if follow_map == "1":
            print("Followed map: +25 points")
            points = points + 25
            number_of_trips = number_of_trips + 1
            #might develop this bit
        elif follow_map != "0":
            print("Invalid option, please choose again:")

    elif choice == 3:
        print("How to redeem points?")
        print("Press 0 for 1 free one-way transit ticket: -250 points")
        print("Press 1 for a free kilometer on rideshare: -80 points")
        redeemed = input("Option: ")
        for each in numbers2:
            if each == "0" or each == "1":
                redeemed = int(redeemed)
                break
            else:
                print("Invalid option, please choose again:")
                break
        if redeemed == 0 and 250 <= points:
            print("1 free Uberland transit ticket")
            free_ride = free_ride + 1
            points = points - 250
        elif redeemed == 0 and 250 >= points:
            print("Insufficient points, please choose again:")
        elif redeemed == 1:
            maxkilos = points // 80
            if maxkilos == 0:
                print("Insufficient points")
            print(f"You currently have {points}. The maximum free distance you can redeem is {maxkilos}km")
            kilos = input("How many kilometers would you like to redeem?: ")
            try:
                kilos = int(kilos)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                break
            freekilos = kilos * 80
            if freekilos <= maxkilos and maxkilos != 0:
                print(f"Travel free on ride share for {kilos}km")
                free_kms = free_kms + kilos
                points = points - freekilos
            else:
                print("Insufficient points, please choose again:")
        else:
            print("Invalid option, please choose again:")

    elif choice == 4:
        print("How to redeem points?")
        print("Press 0 to use free one-way transit ticket.")
        print("Press 1 to use free kilometers on rideshare.")
        redeeming = input("Option: ")
        for each in numbers2:
            if each == "0" or each == "1":
                redeeming = int(redeeming)
                break
            else:
                print("Invalid option, please choose again:")
                break
        if redeeming == 0 and free_ride > 0:
            print("Used 1 free one-way transit ticket. You have {free_ride} remaining.")
            free_ride = free_ride - 1
        elif redeeming == 1 and free_kms > 0:
            kilos = input(f"How many free kms will you use? The maximum you can redeem right now is {free_kms} free km(s)")
            try:
                kilos = int(kilos)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                break
            if kilos < free_kms:
                print("You do not have that many free kms. Please try again.")
            else: 
                free_kms = free_kms - kilos
                print(f"Used {kilos} free km(s). You have {free_kms} free km(s) remaining.")
        elif free_ride < 1 or free_kms < 1:
            print("You do not have a free ride/free kms. Please purchase first.")
        else:
            print("Invalid input. Please enter a valid answer.")

    elif choice == 8:
        print(f"You have {points} points.")

    elif choice == 9: #review
        review4driver = input("Submit review for most recent driver: ")
        reviews.append(review4driver)
        points = points + 3
        print("fThanks for submitting a review! You get 3 points! You now have {points}")
        print("Here is your most recent review:")
        print(reviews[len(reviews) - 1])
    elif choice == 0:
        print(f"You have {points} points.")
        print("Goodbye! Have a nice day.")
        sys.exit()
    else:
        print("Invalid option, please choose again:")
    leave()
