import re


datafile = 'data.txt'

with open(datafile) as file:
    txt = file.read()

print(len(re.findall(r'[a-zA-Z]+',txt)))


