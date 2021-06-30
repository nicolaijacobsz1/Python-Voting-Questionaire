
"""Voting program to help register users"""
# the start of the voting program
print("*****************************************************")
print("Welcome to the Python Voter Registration Application.")
while(1):
    #asking if the user wants to continue
    conti=input("Do you want to continue with Voter Registration?\n").lower()
    # will continue if the user enters yes
    if conti=="yes":
        #ask for first name
        fname=input("What is your first name?\n")
        #if the user don't wants to contine exit from the program
    else:
        break
    #asking if the user wants to continue
    conti=input("Do you want to continue with Voter Registration?\n").lower()
    #if the user entered yes it will continue to next question
    if conti=="yes":
        #ask for last name
        lname=input("What is your last name?\n")
    else:
        break
    #asking if the user wants to continue
    conti=input("Do you want to continue with Voter Registration?\n").lower()
    #if the user entered yes it will continue to next question
    if conti=="yes":
    #validating age between 18 and 120
        while(1):
            try:
                age = int(input("What is your age?\n "))
                if age>=18 and age<120:
                    break
                #if user entered invalid age print this
                else:
                   print('you must be older than 18 and younger than 120')
            except ValueError:
                print(' value is incorrect')
    #ask if the user wants to continue
    conti=input("Do you want to continue with Voter Registration?\n").lower()
    #if the user entered yes the questions will continue
    if conti=="yes":

    #ask if the user is a US citizen
        while(1):
            try:
                citizen=input("Are you a U.S. Citizen?\n")
                if citizen=="yes":
                    break
                else:
                    print("You need to be a U.S Citizen to vote.\n")
            except:
                continue
    else:
        break
    #asking if the user wants to continue
    conti=input("Do you want to continue with Voter Registration?\n").lower()
    #if the user entered yes the questions will continue
    #check the state entered by user has two letters
    if conti=="yes":

        while(1):
            try:
                state=input("What state do you live?\n")
                if len(state)==2: #only will accept 2 letter for state name
                    break
                else:
                    print("Please enter the two letters of your state\n")
            except:
                continue
    else:
        break
    #asking if the user wants to continue
    conti=input("Do you want to continue with Voter Registration?\n").lower()
    #if the user entered yes the questions will continue
    if conti=="yes":
    #ask for the zip code
        zip_code=input("What is your zip code?\n")
        #prints the details provided
        print("\nThanks for registering to vote.Here is the information we received.")
        print("Name (first last): {} {}".format(fname,lname))
        print("Age: {}".format(age))
        print("U.S. Citizen: {}".format(citizen))
        print("State: {}".format(state))
        print("Zip code: {}".format(zip_code))
        print("Thanks for trying the Voter Registration Application.\n Your voter registration card should be shipped within 3 weeks.")
        print("***********************************************************")
    break
