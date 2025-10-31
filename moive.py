print(" welcome to book my moive application")

def t_city():
    print("please select your city\n 1. banglore \n 2. pune \n 3. delhi \n 4. mumbai")
    try:
        c = int(input("enter your choice:"))
    except ValueError:
        print("please enter a number")
        return t_city()
    if c == 1:
        print("you have selected banglore")
    elif c == 2:
        print("you have selected pune")
    elif c == 3:
        print("you have selected delhi")
    elif c == 4:
        print("you have selected mumbai")
    else:
        print("please choose a valid city")
        return t_city()
    return t_movie()   # proceed to movie selection 

def t_movie():
    print("\nplease select the movie you want to watch \n 1. xyz \n 2. pqr \n 3. opq \n 4. back")
    try:
        t = int(input("enter your choice:"))
    except ValueError:
        print("please enter a number")
        return t_movie()
    if t == 1:
        print("you have selected moive 1.xyz")
    elif t == 2:
        print("you have selected movie 2.pqr")
    elif t == 3:
        print("you have selected moive 3.opq")
    elif t == 4:
        return t_city()
    else:
        print("please choose a valid moive")
        return t_movie()
    return t_theatre()   # proceed to theatre  

def t_theatre():
    print("\nplease select the theatre\n1. inox\n2. pvr\n3. back")
    try:
        h = int(input("enter your choice:"))
    except ValueError:
        print("please enter a number")
        return t_theatre()
    if h == 1:
        print("you have selected inox")
    elif h == 2:
        print("you have selected pvr")
    elif h == 3:
        return t_movie()
    else:
        print("please enter a valid option")
        return t_theatre()
    return t_screen() # proceed to screen

def t_screen():
    print("\nchoose your screen \n1. screen 1 \n2. screen 2 \n3. screen 3 \n4. back")
    try:
        s = int(input("select screen:"))
    except ValueError:
        print("please enter a number")
        return t_screen()
    if s == 1:
        print(" you selected screen 1 ")
    elif s == 2:
        print("you selected screen 2")
    elif s == 3:
        print("you selected screen 3")
    elif s == 4:
        return t_theatre()
    else:
        print("please enter valid option")
        return t_screen()
    return timing(s)  # proceed to timing 

def timing(s):
    slot1 = {"1":"10.00-1.00","2":"1.10-4.10","3":"4.20-7.20","4":"7.30-10.30"}
    slot2 = {"1":"10.15-1.15","2":"1.25-4.25","3":"4.35-7.35","4":"7.45-10.45"}
    slot3 = {"1":"10.30-1.30","2":"1.40-4.40","3":"4.50-7.50","4":"8.00-10.45"} 
    if s == 1:
        print("\nplease select the timing:\n1. {}\n2. {}\n3. {}\n4. {}\n".format(*slot1.values()))
        time = input("enter slot number: ")
        print("selected time is:", slot1.get(time, "invalid time"))
    elif s == 2:
        print("\nplease select the timing:\n1. {}\n2. {}\n3. {}\n4. {}\n".format(*slot2.values()))
        time = input("enter slot number: ")
        print("selected time is:", slot2.get(time, "invalid slot"))
    elif s == 3:
        print("\nplease select the timing:\n1. {}\n2. {}\n3. {}\n4. {}\n".format(*slot3.values()))
        time = input("enter slot number:")
        print("selected time is:", slot3.get(time, "invalid slot"))
    else:
        print("please enter valid option")
        return t_screen()

# restart the program 
t_city()
