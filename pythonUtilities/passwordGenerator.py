import string
import random


def generatePassword(length, includeUppercase, includeDigits, includeSpecial):
    validChars = string.ascii_lowercase

    password = [random.choice(validChars)]
    if includeUppercase:
        validChars += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if includeDigits:
        validChars += string.digits
        password.append(random.choice(string.digits))
    if includeSpecial:
        validChars += string.punctuation
        password.append(random.choice(string.punctuation))

    for _ in range(length - len(password)):
        password.append(random.choice(validChars))
    random.shuffle(password)
    return "".join(password)


def validateInput(requirement):
    val = ""
    match requirement:
        case "con":
            val = input(
                "Do you want to generate another password? (yes/no): ")
        case "uppercase letters":
            val = input(
                "Do you want to include uppercase letters? (yes/no): ")
        case "numbers":
            val = input("Do you want to include numbers? (yes/no): ")
        case "special characters":
            val = input(
                "Do you want to include special characters? (yes/no): ")
        case _:
            raise ValueError(f"Invalid requirement: {requirement}")
    val = val.strip().lower()
    while val not in {"yes", "no"}:
        val = input(
            "Invalid input. Please enter 'yes' or 'no': ").strip().lower()
    return val


def main():
    con = "yes"
    while con == "yes":
        try:
            length = int(input("Enter how long you want the password to be: "))
            includeUpper = validateInput("uppercase letters") == "yes"
            includeDigits = validateInput("numbers") == "yes"
            includeSpecial = validateInput("special characters") == "yes"

            numRequirement = sum(
                [includeUpper, includeDigits, includeSpecial]) + 1
            while length < numRequirement:
                print(
                    f"Your length is too short for the number of requirements you set ({numRequirement}).")
                length = int(
                    input(f"Please enter a length of at least {numRequirement}: "))
            password = generatePassword(
                length, includeUpper, includeDigits, includeSpecial)
            print(f"Your password is: {password}")
        except ValueError:
            print("Please enter a valid number for the length")
        finally:
            con = validateInput("con")
    print("Goodbye")


if __name__ == '__main__':
    main()
