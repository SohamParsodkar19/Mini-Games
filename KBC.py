questions = [
    [
        "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ],
    [
    "What is your name", "Akanksha", "Soham", "Triveni", "Angel", "Shipra", 4
    ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0

for i in range(0,len(questions)):
    
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}             b. {question[2]} ")
    print(f"c. {question[3]}             d. {question[4]} ")
    reply = int(input("Enter your answer (1-4):  or 0 to quit:"))
    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        print("\n------------------------------------------------------------------------\n")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            moeny = 10000000    
    else:
        print("Wrong answer")
        break 
print(f"Your Have won {money}")    