dictionary = {
        "Ave it": "Exclamation",
        "Bobbins": "Nonsense",
        "Brew": "Tea",
        "Butty": "Sandwich",
        "Buzzin": "Excited / Extreme Happiness",
        "Cadge": "Freeload / Scrounge / Get Something Free",
        "Chuddy": "Chewing Gum",
        "Chuffed": "Happy",
        "Do One": "Go Away",
        "Duds": "Underwear / Boxers",
        "Easy": "Hello",
        "Fit": "Tasty / Attractive",
        "Gaggin": "Thirsty",
        "Give Over": "Stop It / Expression of Disbelief",
        "Keks": "Trousers",
        "Knackered": "Tired / Exhausted",
        "Legless": "Extremely Drunk",
        "Mardy": "Moody / Surly / Moaning",
        "Mingin": "Horrible / Revolting",
        "Mint": "Great, Fantastic",
        "Mooch": "Wander Around Aimlessly",
        "Nowt": "Nothing",
        "Our Kid": "Any Friend or Family Member",
        "Peg It": "To Run / Flee",
        "Proper": "Really / A Term of Exaggeration",
        "Rank": "Disgusting",
        "Scran": "Food",
        "Snide": "Tight / Not Generous",
        "Sorted": "Good / Excellent",
        "Sound": "Good / Fine",
        "Swear Down": "A Promise of The Truth",
        "Top One": "Excellent"
            }

choice = None
while choice != "0":
    print(
        """
    Please choose from the following options

        0 - Quit The Manc Dictionary
        1 - List All Manc Words / Terms in Dictionary
        2 - Look Up a Manc Word / Term
        3 - Add a Manc Word / Term
        4 - Redefine a Manc Word / Term
        5 - Delete a Manc Term
        """
    )
    choice = input("""
    Please enter your choice: """)
    if choice == "0":
        print("""
    Thank you for using the Manc Dictionary. Good-bye!
        """)
    elif choice == "1":
        print("""
    Here is a list of all the terms in the Manc Dictionary:
    """)
        for terms in sorted(dictionary):
            print(f"""\t{terms}""")
    elif choice == "2":
        word = input("""
    Which Manc word would you like to look for?: """)
        if word in dictionary:
            definition = dictionary[word]
            print(f"""
        {word} means {definition}
        """)
        else:
            print(f"""
    Sorry, the word {word} is not in our dictionary
            """)
    elif choice == "3":
        word = input("""
    Which word do you want to add to the Manc Dictionary?: """)
        if word not in dictionary:
            definition = input("""
    What's the definition?: """)
            dictionary[word] = definition
            print(f"""
    OK, {word} has been added to the Manc Dictionary.
        """)
        else:
            print("""
    That word already exists in our Manc Dictionary!
        """)
    elif choice == "4":
        word = input("""
    What Manc term would you like to redefine?: """)
        if word in dictionary:
            definition = input("""
    What's the new definition of our Manc word?: """)
            dictionary[word] = definition
            print(f"""
    OK, {word} has been redefined in the Manc Dictionary!
        """)
        else:
            print("""
    That term doesn't exist in the Manc Dictioanry! Maybe You'd like to add it.
        """)
    elif choice == "5":
        word = input("""
    Which word from the Manc Dictionary would you like to delete?: """)
        if word in dictionary:
            del dictionary[word]
            print(f"""
    Okay, {word} was deleted from the Manc Dictionary.
        """)
        else:
            print(f"""
    Sorry, {word} doesn't exist in the Manc Dictionary.
        """)
    else:
        print(f"""
    Sorry, but {choice} is not a valid choice. PLease check the options again.
        """)
    