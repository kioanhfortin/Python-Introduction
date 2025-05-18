def all_thing_is_obj(obj:any) -> int:
    # Check for known types
    if isinstance(obj, list):
        print("List :", type(obj))
    elif isinstance(obj, tuple):
        print("Tuple :", type(obj))
    elif isinstance(obj, set):
        print("Set :", type(obj))
    elif isinstance(obj, dict):
        print("Dict :", type(obj))
    elif isinstance(obj, str) and obj == "Brian":
        print("Brian is in the kitchen :", type(obj))
    else:
        print("Type not found")
    
    return 42
