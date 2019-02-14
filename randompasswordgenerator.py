#random password generator
import random

if __name__ == '__main__':
    def passgen (length):
        S = 'ABCDEFGHJIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()+'
        passLength = int(length)
        password = "".join(random.sample(S, passLength))
        print(password)

passgen(8)
