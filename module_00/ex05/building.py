import sys
import string


def main():

    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0
    size = 0

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("What is the text to count?\n")
        space += 1
        size += 1

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punctuation += 1
        elif char.isspace() or char == '\n':
            space += 1
        elif char.isdigit():
            digit += 1
        size += 1
    print(f"The text contains {size} characters:")
    print(f"- {upper} upper letters")
    print(f"- {lower} lower letters")
    print(f"- {punctuation} punctuation marks")
    print(f"- {space} spaces")
    print(f"- {digit} digits")


if __name__ == "__main__":
    main()
