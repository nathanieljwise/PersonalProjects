#imports the random module
import random
#imports the time module
import time

#Asks for user's first name.
firstname = input("What's your first name? ")
time.sleep(.9)

#Asks for user's last name.
surname = input("What's your last name? ")
time.sleep(.8)

#Changes names to title case
Firstname = firstname.title()
Surname = surname.title()

time.sleep(1.3)

#If the user is Nathaniel Wise, gives deference to the creator.
if Firstname == "Nathaniel" and Surname == "Wise":
    print("Hello, " + Firstname + " " + Surname + ". Thank you for my existence.")
    time.sleep(1.3)
    
#If the user is Isaac Friend, gives a compliment.
else:
    if Firstname == "Isaac" and Surname == "Friend":
        print("Hello, " + Firstname + " " + Surname + ". You're a really solid guy.")
        
#If the user is Priscilla Wise, asks about the office
    else:
        if Firstname == "Priscilla" and Surname == "Wise":
            print("Hi, " + Firstname + ", I'm very glad to see you!")

            time.sleep(1.1)
            officecolor = input("What color is your office? ")
            officecolorlower = officecolor.lower()
            time.sleep(.9)
            if officecolorlower == "yellow":
                print("Oh, I had an office that was yellow when I was growing up!")
            else:
                if officecolorlower == "purple":
                    print("Oh, my daddy had a TV in his purple office growing up.")
                else:
                    if officecolorlower == "pink":
                        print("Oh, my daddy had a pink office, and a bunch of dogs that lived at our house.")
                    else:
                        time.sleep(.1)

#If the user is neither
        else:
            print("Hello, " + Firstname + " " + Surname + ". Good to meet you.")

time.sleep(1.2)

#Asks what pet the user has
pet = input("What kind of pet do you have? ")

#Sets the input to lowercase
petlower = pet.lower()

#Sets tidbits of conversation about the pet
petconvo1 = ("Oh, I've heard that " + petlower + " is a good companion to have.")
petconvo2 = ("Oh, really? I had " + petlower + " when I was growing up.")
petconvo3 = ("Oh, I bet " + petlower + " eats a lot of food.")
 
#Turns the tidbits into a list
petconvolist = [petconvo1, petconvo2, petconvo3]

#Sets a random choice from the list as a variable
convo = random.choice(petconvolist)

#Prints that choice
print(convo)
    
#Continues the conversation
if convo == petconvo1:
    time.sleep(.4)
    print("Wouldn't you agree?")
elif convo == petconvo2:
    time.sleep(.6)
    print("I think it's important for children to grow up with pets.")
elif convo == petconvo3:
    time.sleep(1)
    foodbudget=input("Does it cost a lot to feed " + petlower + "? ")
    time.sleep(.5)
