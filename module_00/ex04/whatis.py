import sys

def main():
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        return

    arg = sys.argv[1]

    if not (arg.isdigit() or (arg.startswith('-') and arg[1:].isdigit())):
        print("AssertionError: argument is not an integer")
        return

    num = int(sys.argv[1])
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
