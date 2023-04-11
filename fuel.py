while True:
    try:
        fraction_str = input("Please enter a fraction in the format X/Y: ")
        x, y = map(int, fraction_str.split('/'))
        if x > y or y == 0:
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        print("Invalid input, please try again.")

percentage = round((x / y) * 100)

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")