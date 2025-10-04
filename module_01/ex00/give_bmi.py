from typing import List, Union

Number = Union[int, float]

def give_bmi(height: List[Number], weight: List[Number]) -> List[float]:
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists.")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("All elements must be int of float.")

        if h <= 0:
            raise ValueError("Height must be positive.")
        
        if w <= 0:
             raise ValueError("Weight must be positive.")

        return [w / (h ** 2) for h, w in zip(height, weight)]

def apply_limit(bmi: List[float], limit: int) -> List[bool]:
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list.")
    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be int of float.")

    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("All BMI values must be int or float.")
        
    return [b > limit for b in bmi]

def main():
    try:
        # height = [2.71, 1.15]
        # weight = [165.3, 38.4]
        height = [1.64]
        weight = [63.5]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 25))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()