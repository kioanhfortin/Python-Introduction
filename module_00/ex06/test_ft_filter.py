from ft_filter import ft_filter

def run_test(name, function, iterable):
    try:
        expected = list(filter(function, iterable))
        result = list(ft_filter(function, iterable))
        assert expected == result, f"❌ {name}: expected {expected}, got {result}"
        print(f"✅ {name}: passed")
    except Exception as e:
        print(f"❌ {name}: exception occurred -> {e}")

def main():
    run_test("Alpha letters", str.isalpha, "He11o World!")
    run_test("Digits only", str.isdigit, "a1b2c3")
    run_test("Uppercase only", str.isupper, "AbCdE")
    run_test("None function with truthy filter", None, [0, 1, False, True, "", "yes"])
    run_test("Empty iterable", str.isdigit, "")
    run_test("List of booleans", None, [False, True, False, True])
    run_test("List of strings with None", None, ["", "Hello", "", "World"])
    run_test("Numbers divisible by 3", lambda x: x % 3 == 0, range(20))

if __name__ == "__main__":
    main()