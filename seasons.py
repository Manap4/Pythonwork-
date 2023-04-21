from datetime import datetime, date


def main():
    birthdate = get_birthdate_from_user()
    age = age_in_minutes(birthdate)
    print(f"You are {age}.")

    
def age_in_minutes(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age == 0:
        return "a newborn baby"
    else:
        age_in_minutes = age * 525600
        return f"{age_in_minutes:,} minutes old"


def get_birthdate_from_user():
    dob = input("Please enter your date of birth in YYYY-MM-DD format: ")
    try:
        birthdate = datetime.strptime(dob, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please try again.")
        return get_birthdate_from_user()
    else:
        return birthdate


if __name__ == "__main__":
    main()
