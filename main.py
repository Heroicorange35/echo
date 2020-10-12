import time
import random
import sys

puberty = 0
alcoholone = random.randint(1,4)
atest = "null"
deathage = random.randint(1,100)
midlc = random.randint(20,60)
looks = random.randint(1,5)
marrigeage = random.randint(18,50)
depression = random.randint(1,4)
babies = random.randint(16,30)
wifeage = random.randint(19,50)
wdeathage = random.randint(51,90)
socioeconomicstatus = random.randint(1,6)
antivax = 0
profession = random.randint(1,11)
survivalc = random.randint(1,10)
survivalcp = random.randint(1,50)
catchingrona = random.randint(10,100)
catchingcpox = random.randint(5,30)
covid = random.randint(1,3)
cpox = random.randint(1,3)
smoking = random.randint(1,4)
addictsm = random.randint(21,100)
car = 1
immor = random.randint(1,5)
deathcause = random.randint(1,8)
immdeathage = random.randint(250,1000)
kidnapped = random.randint(1,5)
paid = random.randint(1,3)
kidnppdage = random.randint(1,17)

if profession == 1:
    job = "Rapper"
elif profession == 2:
    job = "Grocer"
elif profession == 3:
    job = "Artist"
elif profession == 4:
    if car == 1:
        job = "Uber Driver"
    else:
        pass
elif profession == 5:
    job = "Nurse"
elif profession == 6:
    job = "Doctor"
elif profession == 7:
    job = "Chef"
elif profession == 8:
    job = "Musician"
elif profession == 9:
    job = "Player"
elif profession == 10:
    job = "Gamer"
elif profession == 11:
    job = "Scientist"
else: 
    pass

if socioeconomicstatus == 1:
    weath = "Homeless"
elif socioeconomicstatus == 2:
    wealth = "Poor"
elif socioeconomicstatus == 3:
    wealth = "Average"
elif socioeconomicstatus == 4:
    wealth = "Anti-Vax"
    antivax = 1
elif socioeconomicstatus == 5:
    wealth = "Wealthy"
elif socioeconomicstatus == 6:
    wealth = "Loaded"
else:
    pass

if depression == 1:
    sadness = 4
elif depression == 2:
    sadness = 3
elif depression == 3:
    sadness = 2
elif depression == 4:
    sadness = 1
else:
    pass

if looks == 1:
    newmarrigeage = marrigeage + 5
elif looks == 2:
    newmarrigeage = marrigeage + 2
elif looks == 3:
    newmarrigeage = marrigeage
elif looks == 4:
    newmarrigeage = marrigeage - 2
elif looks == 5:
    newmarrigeage = marrigeage - 5
else:
    pass

if looks == 1:
    looks = "Revolting"
elif looks == 2:
    looks = "Ugly"
elif looks == 3:
    looks = "Average"
elif looks == 4:
    looks = "Good"
elif looks == 5:
    looks = "Beautiful"
else:
    looks = "null"

if looks == "Revolting":
    newdepression = sadness + 2
elif looks == "Ugly":
    newdepression = sadness + 1
elif looks == "Average":
    newdepression = sadness
elif looks == "Good":
    newdepression = sadness - 1
elif looks == "Beautiful":
    newdepression = sadness - 2
else:
    newdepression = sadness

if alcoholone == 1:
    atest = "Terrible"
elif alcoholone == 2:
    atest = "Okay"
elif alcoholone == 3:
    atest = "Good"
elif alcoholone == 4:
    atest = "Great"
else:
    atest = "null"

print("Echo\nVersion 1.11.0\nIf it says 'Wealth not defined',\njust run again")
time.sleep(1)
for x in range(1001):
    print("Echo is " , x , " years old")
    age = x
    nwifeage = x + 5
    time.sleep(1)
    if age == 12:
        puberty = 1
        time.sleep(1)
    elif age == 0:
        print("Echo was born into a " , wealth , " family")
    elif age == 2:
        if antivax == 1:
            print("Echo is going through a mid-life crisis")
            time.sleep(1)
            print("He is now scarred for life")
        else:
            pass
    elif age == 13:
        if newdepression >= 4:
            print("Echo is depressed")
        else:
            pass
        time.sleep(1)
    elif age == 16:
        print("Echo can now drive")
        time.sleep(1)
        if wealth == "Poor":
            print("But he doesn't have a car because his family is too poor")
            car = 0
        else:
            pass
    elif age == 18:
        puberty = 0
        print("Echo looks " , looks)
        time.sleep(.5)
        print("Echo decided to be a " , job)
        time.sleep(1)
    elif age == 21:
        print("Echo drank alcohol for the first time")
        print("It went, " , atest)
        time.sleep(1)
        if job == "Rapper":
            print(" _______________ ")
            print("|               |")
            print("|      Echo     |")
            print("|    Age: ",age,"   |")
            print("|               |")
            print("|               |")
            print("|               |")
            print("|_______________|")
            sys.exit("Echo was shot")
        elif job == "Scientist":
            if immor == 1:    
                print(" _______________ ")
                print("|               |")
                print("|      Echo     |")
                print("|    Age: ∞     |")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|_______________|")
                print("Echo discovered immortality")
                deathage = 1000
            else:
                pass
    else:
        pass
    if age == newmarrigeage:
        print("Echo and his girlfriend have decided \nto take to the next level\nand are getting married\nshe is " , wifeage , " years old")
        time.sleep(1)
    else: 
        pass
        time.sleep(1)
    if age == deathage:
        if deathcause == 1:
            print(" _______________ ")
            print("|               |")
            print("|      Echo     |")
            print("|    Age: ",age,"   |")
            print("|               |")
            print("|               |")
            print("|               |")
            print("|_______________|")
            sys.exit("Echo died of alcohol posioning")
        elif deathcause == 2:
            print(" _______________ ")
            print("|               |")
            print("|      Echo     |")
            print("|    Age: ",age,"   |")
            print("|               |")
            print("|               |")
            print("|               |")
            print("|_______________|")
            sys.exit("Echo died of a car crash")
        elif deathcause == 3:
            print(" _______________ ")
            print("|               |")
            print("|      Echo     |")
            print("|    Age: ",age,"   |")
            print("|               |")
            print("|               |")
            print("|               |")
            print("|_______________|")
            sys.exit("Echo died of natural causes")
        elif deathcause == 4:
            print(" _______________ ")
            print("|               |")
            print("|      Echo     |")
            print("|    Age: ",age,"   |")
            print("|               |")
            print("|               |")
            print("|               |")
            print("|_______________|")
            sys.exit("Echo has killed themself")
        elif deathcause == 5:
            print(" _______________ ")
            print("|               |")
            print("|      Echo     |")
            print("|    Age: ",age,"   |")
            print("|               |")
            print("|               |")
            print("|               |")
            print("|_______________|")
            sys.exit("Echo was murdered")
        elif deathcause == 6:
            print(" _______________ ")
            print("|               |")
            print("|      Echo     |")
            print("|    Age: ",age,"   |")
            print("|               |")
            print("|               |")
            print("|               |")
            print("|_______________|")
            sys.exit("A toaster, the ultimate bath bomb")
        elif deathcause == 7:
            print(" _______________ ")
            print("|               |")
            print("|      Echo     |")
            print("|    Age: ",age,"   |")
            print("|               |")
            print("|               |")
            print("|               |")
            print("|_______________|")
            sys.exit("Echo drank gasoline")
        elif deathcause == 8:
            print(" _______________ ")
            print("|               |")
            print("|      Echo     |")
            print("|    Age: ",age,"   |")
            print("|               |")
            print("|               |")
            print("|               |")
            print("|_______________|")
            sys.exit("Echo comitted SHOOT SHOOT")
        else:
            pass
    else:
        pass
    if age == immdeathage:
        print(" _______________ ")
        print("|               |")
        print("|      Echo     |")
        print("|    Age: ",age,"|")
        print("|               |")
        print("|               |")
        print("|               |")
        print("|_______________|")
        sys.exit("Echo got tired of being immortal and\nkilled himself")
    else:
        pass
    if age == midlc:
        crisis = random.randint(1,4)
        newwifeage = random.randint(19,30)
        print("Echo is going through a mid-life crisis")
        time.sleep(1)
        if crisis == 1:
            print("Echo decided to go to Italy")
            time.sleep(.5)
            print("Echo is now poor")
        elif crisis == 2:
            print("Echo is getting a divorce with his " , wifeage , " year old wife")
            time.sleep(.5)
            print("He is now married to a " , newwifeage , " year old wife")
        elif crisis == 3:
            print("Echo has decided he wants to give to the community \nand is now poor")
        elif crisis == 4:
            print("Echo is now feeling guilty for a past \nwrong-doing he committed\nhe's going to make it right with\nthat person")
        else:
            pass
    else:
        pass
    if age == babies:
        print("Echo now has a child")
    else:
        pass
    if nwifeage == wdeathage:
        print("Echo's wife has died")
    else:
        pass
    if covid == 1:
        if age == catchingrona:
          print("Echo has contracted CORONAVIRUS")
          if antivax == 1:
            print(" _______________ ")
            print("|               |")
            print("|      Echo     |")
            print("|    Age: ",age,"   |")
            print("|               |")
            print("|               |")
            print("|               |")
            print("|_______________|")
            sys.exit("Echo Died Because of CORONAVIRUS")
          else:
            if survivalc == 1:
              print(" _______________ ")
              print("|               |")
              print("|      Echo     |")
              print("|    Age: ",age,"   |")
              print("|               |")
              print("|               |")
              print("|               |")
              print("|_______________|")
              sys.exit("Echo Died Because of CORONAVIRUS")
            else:
              print("Echo has survived CORONAVIRUS")
        else:
            pass
    else:
        pass
    if cpox == 1:
        if age == catchingcpox:
            if antivax == 1:
                print(" _______________ ")
                print("|               |")
                print("|      Echo     |")
                print("|    Age: ",age,"   |")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|_______________|")
                print("Echo Died Because of CHICKEN POX")
                sys.exit("Lol shoulda vaccinated")
            else:
                pass
            if survivalcp == 1:
                print(" _______________ ")
                print("|               |")
                print("|      Echo     |")
                print("|    Age: ",age,"   |")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|_______________|")
                sys.exit("Echo Died Because of CHICKEN POX")
            else:
                pass
        else:
            pass
    else:
        pass
    if age == addictsm:
        if smoking == 1:
            print("Echo is now addicted to cigarettes")
        else:
            pass
    else:
        pass
    if age == kidnppdage:
        if kidnapped == 1:
            print("Echo has been kidnapped")
            time.sleep(1)
            print("The ransom is $1,000")
            if wealth == "Homeless":
                print(" _______________ ")
                print("|               |")
                print("|      Echo     |")
                print("|    Age: ",age,"   |")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|_______________|")
                print("Your parents couldn't pay the ransom")
                sys.exit("You were killed by your captors")
            elif wealth == "Poor":
                print(" _______________ ")
                print("|               |")
                print("|      Echo     |")
                print("|    Age: ",age,"   |")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|_______________|")
                print("Your parents couldn't pay the ransom")
                sys.exit("You were killed by your captors")
            elif wealth == "Average":
                if paid == 1:
                    print(" _______________ ")
                    print("|               |")
                    print("|      Echo     |")
                    print("|    Age: ",age,"   |")
                    print("|               |")
                    print("|               |")
                    print("|               |")
                    print("|_______________|")
                    print("Your parents wouldn't pay the ransom")
                    sys.exit("You were killed by your captors")
                else:
                    print("Your parents paid the ransom")
            elif wealth == "Anti-Vax":
                if paid == 1:
                    print(" _______________ ")
                    print("|               |")
                    print("|      Echo     |")
                    print("|    Age: ",age,"   |")
                    print("|               |")
                    print("|               |")
                    print("|               |")
                    print("|_______________|")
                    print("Your parents wouldn't pay the ransom")
                    sys.exit("You were killed by your captors")
                else:
                    print("Your parents paid the ransom")
            elif wealth == "Wealthy":
                if paid == 1:
                    print("Your parents paid the ransom")
                else:
                    print(" _______________ ")
                    print("|               |")
                    print("|      Echo     |")
                    print("|    Age: ",age,"   |")
                    print("|               |")
                    print("|               |")
                    print("|               |")
                    print("|_______________|")
                    print("Your parents wouldn't pay the ransom")
                    sys.exit("You were killed by your captors")
            elif wealth == "Loaded":
                if paid == 1:
                    print("Your parents paid the ransom")
                else:
                    print(" _______________ ")
                    print("|               |")
                    print("|      Echo     |")
                    print("|    Age: ",age,"   |")
                    print("|               |")
                    print("|               |")
                    print("|               |")
                    print("|_______________|")
                    print("Your parents wouldn't pay the ransom")
                    sys.exit("You were killed by your captors")
        else:
            pass
    else:
        pass
