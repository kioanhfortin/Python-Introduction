# Data Struc Type
# List []: Ordered, Mutable (add, remove, change items), Allow duplicate
# Tuple (): Ordered, Immutable(cannot be modified once created), allow duplicate
# Set {}: Unordered, Mutable (add, remove, but not changed directly), No duplicates
# Dictionary {}: Unordered, Mutable, Unique keys (values can repeat)
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "France!")
ft_set = {"Hello", "Paris!"}
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)