import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        s = sys.argv[1]
        n = int(sys.argv[2])
        words = s.split()
        result = list(ft_filter(lambda word: len(word) > n, words))
        print(result)
    except (ValueError, AssertionError):
        print("AssertionError: wrong arguments")


if __name__ == "__main__":
    main()
