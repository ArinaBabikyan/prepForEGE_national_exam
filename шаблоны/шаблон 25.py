import re

for n in range(2024, 10 ** 10, 2024):
    if re.fullmatch('1.{1}2157.{0,3}4', str(n)):
        print(n)