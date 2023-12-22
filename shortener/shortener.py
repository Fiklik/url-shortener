import random
import string


TOKEN_SIZE = 6


class Shortener:
    def __init__(self):
        self.token_size = TOKEN_SIZE

    def generate_token(self):
        chars = string.ascii_letters + string.digits
        token = "".join(random.choice(chars) for _ in range(self.token_size))
        return token
