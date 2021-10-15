x = 'Michael Jackson'

# slicing
print(x[:5])

# strideing
# x[from:to:step-size]
print(x[::2])
print(x[8:13:2])

# replication
print(80*'=')

# raw strings
x = r'UNIX uses \n for newlines.'
print(x)

# escapes
x = 'Use \\t for a Tab.'
print(x)

## string methods
s = 'Michael Jackson is the best!'

# replace
print(s.replace('Jackson', 'Meyer'))

# find
print(s.find('e'))
print(dir(s))

# casefold
# only affects equivalents (not umlauts in general)
s = 'Das Maß aller Dinge ist äußerlich betrachtet...'
print(s.lower())
print(s.casefold())
