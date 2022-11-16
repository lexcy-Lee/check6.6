list = []

def cin(): #Ask for the grades
    list.append(int(input("What's your Term 1 AES grade?")))
    list.append(int(input("What's your Term 1 Maths 1 grade?")))
    list.append(int(input("What's your Term 1 Physics 1 grade?")))
    list.append(int(input("What's your Term 1 Computer Programming 1 grade?")))
    list.append(int(input("What's your Term 2 AES grade?")))
    list.append(int(input("What's your Term 2 Chemistry 1 grade?")))
    list.append(int(input("What's your Term 2 Maths 2 grade?")))
    list.append(int(input("What's your Term 2  Physics 2 grade?")))
    list.append(int(input("What's your Term 3 AES grade?")))
    list.append(int(input("What's your Term 3 Maths 3 grade?")))
    list.append(int(input("What's your Term 3 Physics 3 grade?")))
    list.append(int(input("What's your Term 3 Creative Design grade?")))

def check(): #Check if he/she pass
    for index in range(len(list)): #Need at least 40% in each subject
        if list[index] < 40:
            return "Sorry you do not progress because you need at least 40% in each subject."
        break
    tot = 0
    for index in range(len(list)): #Calculate the average
        tot = tot + list[index]
    avr = tot / 12
    if avr < 60: #At least 60% in average
        return "Sorry you do not progress because you need at least 60% in average."
    if (list[6] < 65) | (list[9] < 65): #Need at least 65% in Maths 2&3
        return "Sorry you do not progress because you need at least 65% in Maths 2&3."
    elif list[8] < 60: #Need at least 60% in Term 3 AES
        return "Sorry you do not progress because you need at least 60% in Term 3 AES."
    else: #Pass
        return "You did the progress."

def cout(): #Tell them how he/she did
    print(check())

cin()
check()
cout()
quit()