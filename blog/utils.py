import random
import string


def get_random_alphanumeric(size=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))
