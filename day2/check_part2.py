from re import *

f = open("input.txt", "r")

def trim(num):
  return str(num).strip()

valid = 0

for x in f:
  t = x.split(":")
  password = trim(t[1])

  if t[0][1] == '-':
    min = int(trim(t[0][0])) - 1
    max = int(trim(t[0][2:4])) - 1
  else:
    min = int(trim(t[0][0:2])) - 1
    max = int(trim(t[0][3:5])) - 1
  
  letter = trim(t[0][len(t[0])-1])
  if (password[min] == letter and password[max] != letter) or (password[min] != letter and password[max] == letter):
    valid = valid + 1
    print(password)

print(valid)
