from typing import List

def slice_me(family: list, start: int, end:int) -> list:
    if not isinstance(family, list):
        raise TypeError("family must be a list of lists.")

    row_length = None
    for row in family:
        if not isinstance(row, list):
            raise TypeError("family must be a 2D list (list of lists).")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise ValueError("All rows must be the same size.")

    print(f"My shape is : ({len(family)}, {row_length})")

    new_family = family[start:end]

    if new_family:
        print(f"My new shape is : ({len(new_family)}, {len(new_family[0])}))")
    else:
        print(f"My new shape is : (0, 0)")

    return new_family


def main():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()