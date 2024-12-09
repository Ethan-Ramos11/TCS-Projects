import random
import time

responses = [
    "It is certain.",
    "Without a doubt.",
    "You may rely on it.",
    "Yes, definitely.",
    "It is decidedly so.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]


def checkContinue():
    con = input("Do you want to ask another question? yes/no: ")
    while con not in {'yes', 'no'}:
        print("You did not enter a valid response please try again: ")
        con = input("Do you want to continue? yes/no: ")
    return con


con = "yes"
print("I am the magic 8ball")
while con == "yes":
    question = input("What would you like to know? ")
    print("thinking...")
    time.sleep(random.randint(1,3))
    print(random.choice(responses))
    con = checkContinue()
