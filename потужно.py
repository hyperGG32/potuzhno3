"""
Advanced Password Quality Meter — Strings Only

GOAL
----
Read a username and a password and classify the password.

INPUT with input() function
-----
Line 1: username
Line 2: password

MANDATORY RULES (all must pass or print EXACTLY "REJECT"):
  R1) length: 10..64 characters inclusive
  R2) contains at least one digit
  R3) contains at least one lowercase letter
  R4) contains at least one uppercase letter
  R5) contains at least one special from:
      ! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . ? / \\ |
  R6) no spaces or tabs
  R7) must start with a LETTER (A–Z or a–z)
  R8) must NOT contain the username (case-insensitive)
  R9) must NOT contain the reversed username (case-insensitive)
  R10) must NOT contain these weak substrings (case-insensitive):
       "password", "qwerty", "12345", "admin", "god"

CLASSIFICATION (only if all R1..R10 pass):
  Score the following extras (each +1):
    E1) ends with a digit OR a special
    E2) contains BOTH '-' and '_' somewhere
    E3) contains at least one of '@' or '#'
    E4) contains at least two categories among {digit, upper, lower, special} at
        the BEGINNING 4 chars (first four chars contain at least two categories)
  Total extras: 0..4
  LABEL:
    0-1 -> OK
    2-3 -> STRONG
    4   -> ELITE

OUTPUT
------
If any mandatory rule fails: print
  REJECT

Else print
  RESULT: <OK|STRONG|ELITE> (len=<n>, d=<0/1>, lo=<0/1>, up=<0/1>, sp=<0/1>)

NOTES / HINTS
-------------
- You may use: len, in, not in, strip, lower, upper, replace, startswith/endswith,
  slicing (e.g., s[:4], s[::-1]), comparisons, boolean ops, f-strings.
"""
import string
import sys

username = input("Username: ")
password = input("Password: ")
#номера помилок відповідають правилу, яке вони порушують
# після гугла ясно шо краще всього користуватись сетами в пайтон, вони ідеально підходять; & - пересічення. якшо є пересічення - ззнач все добре; ascii_letters - алфавіт маленькими і капсом
if not username or not password:
    print("REJECT")
    sys.exit(67)
# if len(password) >= 10 or len(password) <= 64 or not set("0123456789") & set(password) or not set(string.ascii_letters) & set(password) or not set("!@#$%^&*()-_=+[]{};:,.?/\\|") & set(password) or set(" \t") & set(password) or not set(password[0]) & set(string.ascii_letters) or not username.lower() in password.lower() or not username[::-1].lower() in password.lower() or not any(sub in password.lower() for sub in ["password", "qwerty", "12345", "god", "admin"]): нечитаємо, переробити
#    print("ok")
if len(password) < 10 or len(password) > 64:
    print("REJECT")
    sys.exit(1)
if not set("0123456789") & set(password):
    print("REJECT")
    sys.exit(2)
if not set(string.ascii_lowercase) & set(password):
    print("REJECT")
    sys.exit(3)
if not set(string.ascii_uppercase) & set(password):
    print("REJECT")
    sys.exit(4)
if not set("! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . ? / \\ |".replace(" ", '')) & set(password):
    print("REJECT")
    sys.exit(5)
if set(" \t") & set(password):
    print("REJECT")
    sys.exit(6)
if not password[0] in string.ascii_letters:
    print("REJECT")
    sys.exit(7)
if username.lower() in password.lower():
    print("REJECT")
    sys.exit(8)
if username.lower()[::-1] in password.lower():
    print("REJECT")
    sys.exit(9)
if any(weak in password.lower() for weak in ["password", "12345", "god", "qwerty", "admin"]):
    print("REJECT")
    sys.exit(10)
score = 0

if password[-1] in "0123456789! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . ? / \\ |".replace(" ", ''):
    score += 1 # ЧОМУ НЕМА ++SCORE ;-;
if all(special in password for special in ['-', '_']):
    score += 1
if any(special2 in password for special2 in ['@', '#']):
    score += 1
IDKhowtodoitinanotherway = [0,0,0,0]
for a in list(password[0:4]):
    if a in "0123456789":
        IDKhowtodoitinanotherway[0] = 1
    if a in string.ascii_uppercase:
        IDKhowtodoitinanotherway[1] = 1
    if a in string.ascii_lowercase:
        IDKhowtodoitinanotherway[2] = 1
    if a in "! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . ? / \\ |".replace(" ", ''):
        IDKhowtodoitinanotherway[3] = 1

if sum(IDKhowtodoitinanotherway) >= 2:
    score += 1

if score > 3:
    rating = "ELITE"
elif score > 1:
    rating = "STRONG"
else:
    rating = "OK"

print(f"RESULT: {rating} (len={len(password)})")