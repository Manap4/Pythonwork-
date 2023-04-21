import re

email =  input("Whats your email?").strip()
#username, domain=email.split("@")

#if username and domain.endswith(".com"):
if re.search (r"\^.+@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")    