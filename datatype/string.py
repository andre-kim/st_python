# slice_string():
text = "Python is good"
print(text[:3])
print(text[3:])

wrong_name = "antre"
name = wrong_name[:2] + 'd' + wrong_name[3:]
print(name)

# format_string():
text = "i am %d years old" % 30
text_string = "i am %s years old" % '30'
text_advanced = "i am {0} years old".format(30)
text_advanced_two_factor = "i am {0} {1} {string}".format(30, 'years',
                                                          string='old')

print(text)
print(text_string)
print(text_advanced)
print(text_advanced_two_factor)

# function
text = "i am 30 years old"
print(text.count('a'))
print(text.find('e'))
print(text.index('e'))
print(text.find('z'))
# print(text.index('z'))

a = "hello"
print(a.upper())
b = "HELLO"
print(b.lower())

text_replace = "The Essence of Object-Orientation"
print(text_replace.replace("Object", "Subject"))

