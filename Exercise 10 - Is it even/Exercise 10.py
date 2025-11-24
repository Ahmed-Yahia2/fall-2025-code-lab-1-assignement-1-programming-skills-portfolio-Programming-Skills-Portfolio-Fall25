def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."
def main():
    value = int(input("Enter a number: "))
    result = check_even_odd(value)
    print(result)
if __name__ == "__main__":
    main()
