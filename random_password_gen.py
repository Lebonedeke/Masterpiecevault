import random
import string

characters = list(string.ascii_letters + string.digits +'!@#$%^&*')


def gen_password():

      password_length = int(input('how long do you want the password to be ? '))
      random.shuffle(characters)

      password =[]

      for i in range(password_length):
          password.append(random.choice(characters))

      random.shuffle(password)

      password ="".join(password)

      print(password)

gen_password()