import random
from textblob import TextBlob as tb
from textblob.np_extractors import ConllExtractor


def pluralizeNounPhrase(noun_phrase):
    return noun_phrase.pluralize()


def processUserInput(userInput):
    response = ""
    user_input_blob = tb(userInput, np_extractor=ConllExtractor())
    if user_input_blob.polarity <= -0.5:
        response = "Oh dear, that sounds bad."
    elif user_input_blob.polarity <= 0:
        response = "Hmm, that's not great. "
    elif user_input_blob.polarity <= 0.5:
        response = "Well, that sounds positive. "
    elif user_input_blob.polarity <= 1:
        response = "Wow, that sounds great. "

    if user_input_blob.noun_phrases:
        response += (
            "Can you tell me more about "
            + "".join(pluralizeNounPhrase(user_input_blob.noun_phrases))
            + ". "
        )
    else:
        response += "Can you tell me more? "
    return response


print(
    "Hello, I am Marvin, the simple robot. You can end this conversation at any time by typing 'bye' After typing each answer, press 'enter' How are you today?"
)

continue_conv: bool = True

while continue_conv:
    userInput = input(">>> ")
    if userInput == "bye" or userInput == "Bye":
        continue_conv = False
    else:
        response = processUserInput(userInput)
        print(response)
