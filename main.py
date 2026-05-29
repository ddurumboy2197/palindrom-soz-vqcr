def soz_palindrommi(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

print(soz_palindrommi("Madam"))  # True
print(soz_palindrommi("Hello"))  # False
