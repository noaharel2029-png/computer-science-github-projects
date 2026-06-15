"""
Dog Breed Guesser!
Author: Noa Harel
Description: A website that can guess whatever dog breed your thinking of by asking yes or no questions! the program will use nested if statemenes to guess the breed the user is thinking of baseed off of the users responses
"""

# Get user's name
print("Hello! What's your name?")
user_name = input()

# Easter egg: if user types "dog" as their name
if user_name == "dog":
    print("Hahahha funny! whats your real name?")
    user_name = input("whats your real name? ")

print("Nice to meet you, " + user_name + "!")

# question 1: Is the breed small or big?
print("is the dog breed you are thinking of small?")
is_small_breed = input()

# small breed branch
if is_small_breed == "yes":
    print("Ok im thinking of a small breed...")
    
    # Question 2: Does it have long hair?
    print("does it have long hair?")
    has_long_hair = input()
    
    # Small breed with long hair
    if has_long_hair == "yes":
        print("is it known for being friendly?")
        is_friendly = input()
        
        if is_friendly == "yes":
            print("Im guessing of a... Shih Tzu!")
        elif is_friendly == "no":
            print("Im guessing of a Pomeranian!")
    
    # Small breed with short hair
    elif has_long_hair == "no":
        print("is it known for being friendly?")
        is_friendly = input()
        
        if is_friendly == "yes":
            print("Is it really really small?")
            is_toy_breed = input()
            
            if is_toy_breed == "yes":
                print("im guessing of a Chihuahua!")
            elif is_toy_breed == "no":
                print("im guessing of a Pug!")
        
        elif is_friendly == "no":
            print("does it have short hair?")
            has_short_hair = input()
            
            if has_short_hair == "yes":
                print("im guessing of a Dalmatian!")
            elif has_short_hair == "no":
                print("im guessing of a Greyhound!")

# large breed branch
elif is_small_breed == "no":
    print("Ok, thinking of a bigger breed...")
    
    # question 2: Is it a working dog?
    print("is it a working dog?")
    is_working_dog = input()
    
    # big working breed
    if is_working_dog == "yes":
        print("is it known for being friendly?")
        is_friendly = input()
        
        if is_friendly == "yes":
            print("does it have a thick coat?")
            has_thick_coat = input()
            
            if has_thick_coat == "yes":
                print("im guessing of a German Shepherd!")
            elif has_thick_coat == "no":
                print("im guessing of a boxer!")
        
        elif is_friendly == "no":
            print("Im guessing of a Husky!")
    
    # Large non working breed
    elif is_working_dog == "no":
        print("is it known for being friendly?")
        is_friendly = input()
        
        if is_friendly == "yes":
            print("Im guessing of a Golden Retriever!")
        
        elif is_friendly == "no":
            print("does it have short hair?")
            has_short_hair = input()
            
            if has_short_hair == "yes":
                print("im guessing of a Dalmatian!")
            elif has_short_hair == "no":
                print("im guessing of a Greyhound!")

# ending if user gives invalid answer
else:
    print("I give up! What breed are you thinking of?")
