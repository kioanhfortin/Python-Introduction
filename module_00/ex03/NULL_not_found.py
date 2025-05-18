def NULL_not_found(obj: any) -> int:
    try:
        # handle each "null" type separately
        if obj is None:
            print("Nothing: None <class '", type(obj).__name__, "'>", sep="")
        elif isinstance(obj, float) and obj != obj: # NaN check
            print("Cheese: nan <class '", type(obj).__name__, "'>", sep="")
        elif obj == 0 and isinstance(obj, int):
            print("Zero: 0 <class '", type(obj).__name__, "'>", sep="")
        elif obj == "":
            print("Empty: <class '", type(obj).__name__, "'>", sep="")
        elif obj is False:
            print("Fake: False <class '", type(obj).__name__, "'>", sep="")
        else:
            print("Type not Found")
            return 1
        return 0

    except Exception as e:
        print("Error:", e)
        return 1