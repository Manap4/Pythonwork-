
def main():
    s = input('Text: ')
    print(count(s))

def count(s: str) -> int:
    # split the string into words and convert to lowercase
    words = s.lower().split()
    
    # count the number of times "um" appears as a standalone word
    count = 0
    for word in words:
        if word == "um":
            count += 1
    
    return count



if __name__ == "__main__":
    main()
