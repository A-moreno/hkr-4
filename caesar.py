#caesar
import sys

n = int(raw_input().strip())
s =raw_input().strip();
k=int(raw_input().strip())

azu=""
for a in s:
  if a.isalpha():
    if a.islower():
      azu= azu+chr((((ord(a)+k)-97)%26)+97)
    else:
      azu= azu+chr((((ord(a)+k)-65)%26)+65)
  else:
    azu= azu + a
print azu
