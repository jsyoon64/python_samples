import re

mystring = 'Happy Birthday %d' % 20
print(mystring)
pattern = 'py'

print("*** reg exp ***")
print(re.search(pattern, mystring).span()) ## this prints starting and end indices
print(re.search(pattern, mystring).span()[0])  ## this does what you wanted

print("*** in & find method ***")
if pattern in mystring:
    print(mystring.find(pattern))
    print(mystring.rfind(pattern))
