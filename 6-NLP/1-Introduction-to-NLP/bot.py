import random

random_responses = [
    "That is quite interesting, please tell me more.",
    "I see. Do go on.",
    "Why do you say that?",
    "Funny weather we've been having, isn't it?",
    "Let's change the subject.",
    "Did you catch the game last night?",
]
print(
    "Hello, I am Marvin, the simple robot. You can end this conversation at any time by typing 'bye' After typing each answer, press 'enter' How are you today?"
)

continue_conv: bool = True

while continue_conv:
    userInput = input(">>> ")
    if userInput == "bye" or userInput == "Bye":
        continue_conv = False
    else:
        print(random.choice(random_responses))
