from ft_filter import ft_filter

def is_alpha(c):
    return c.isalpha()

def main():
    data = "He110 W0rld!"
    filtered = ft_filter(is_alpha, data)
    print(''.join(filtered))

if __name__ == "__main__":
    main()