import random
import string


def randomString (length=28):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(length))


print(randomString())

print([randomString()] * 100)

def mutation(letter):
    if random.randint(1, 100) <= 5:
        return random.choice(randomString())
    else:
        return letter

print(random.randint(1,100))