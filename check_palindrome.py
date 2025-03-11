#palindrome string
name = "abc"
rev = ""
for i in name:
    rev = i + rev
if name == rev:
    print("name is a palindrome")
else:
    print("name is not a palindrome")
