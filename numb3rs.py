def main():
    ip = input('IPv4 Address: ')
    print(validate(ip))

def validate(ip: str) -> bool:
    # split the ip address into four parts
    parts = ip.split('.')
    
    # check that there are exactly four parts
    if len(parts) != 4:
        return False
    
    # check that each part is an integer between 0 and 255
    for part in parts:
        try:
            value = int(part)
            if value < 0 or value > 255:
                return False
        except ValueError:
            return False
    
    return True


if __name__ == "__main__":
    main()
