import sys


NESTED_MORSE = {
    "A": ".-",     "B": "-...",   "C": "-.-.",
    "D": "-..",    "E": ".",      "F": "..-.",
    "G": "--.",    "H": "....",   "I": "..",
    "J": ".---",   "K": "-.-",    "L": ".-..",
    "M": "--",     "N": "-.",     "O": "---",
    "P": ".--.",   "Q": "--.-",   "R": ".-.",
    "S": "...",    "T": "-",      "U": "..-",
    "V": "...-",   "W": ".--",    "X": "-..-",
    "Y": "-.--",   "Z": "--..",
    "0": "-----",  "1": ".----",  "2": "..---",
    "3": "...--",  "4": "....-",  "5": ".....",
    "6": "-....",  "7": "--...",  "8": "---..",
    "9": "----.",
    " ": "/"
}


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Wrong arguments")
        input_string = sys.argv[1]

        if not all(char.upper() in NESTED_MORSE for char in input_string):
            raise AssertionError("Wrong Arguments")

        morse_encoded = ' '.join(NESTED_MORSE[char.upper()]
                                 for char in input_string)
        print(morse_encoded)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
