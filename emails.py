import random
import string

email_list = []

def email_generator():
    for email in range(5000):
        email = ''.join(random.choice( string.ascii_lowercase) for x in range(7))+'@gmail.com'
        email_list.append(email)
    return email_list




