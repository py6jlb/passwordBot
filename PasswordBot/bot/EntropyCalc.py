import math

class EntropyCalc():

    def calc(self, password):
        charspace = 30
        pass_len = len(password)
        entropy = math.log(charspace**pass_len, 2)
        return int(entropy)