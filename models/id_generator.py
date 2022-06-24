import string
import random


class IdGenerate:
    def __init__(self):
        self.id_generated = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(5)])
