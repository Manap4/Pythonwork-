def validate_email_address(email_address):
   
    if email_address.count("@") != 1:
        return False
    
    
    local_part, domain_part = email_address.split("@")
    
    
    if not local_part or not domain_part:
        return False
    
    
    for char in local_part + domain_part:
        if not char.isalnum() and char not in ".-_":
            return False
    
    
    if "." not in domain_part:
        return False
    
    
    top_level_domains = ["com", "net", "org", "edu", "gov", "mil"]
    top_level_domain = domain_part.split(".")[-1]
    if top_level_domain not in top_level_domains:
        return False
    
    return True


email_address = input("Enter an email address: ")


if validate_email_address(email_address):
    print("Valid")
else:
    print("Invalid")
