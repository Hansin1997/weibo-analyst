from yaml import safe_load


class Config:
    def __init__(self, file):
        f = open(file, 'r')
        self.data = config = safe_load(f)
        f.close()
