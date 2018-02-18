import random
import string
count = int(input("Token len:"))
list_passwd_all = random.sample(string.ascii_letters + string.digits, count - 3)
list_passwd_all.extend(random.sample(string.digits, 1))
list_passwd_all.extend(random.sample(string.ascii_lowercase, 1))
list_passwd_all.extend(random.sample(string.ascii_uppercase, 1))
random.shuffle(list_passwd_all)
str_passwd = ''.join(list_passwd_all)
print(str_passwd)