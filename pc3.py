from collections import defaultdict

d_char = defaultdict(str)

text = ''.join([line.rstrip() for line in open('input_pc3')])

for i in text:
    if i in d_char:
        d_char[i] += 1
    else:
        d_char[i] = 1

chars = ''
for key, value in d_char.iteritems():
    if value < 10:
        chars += key

print chars
word = ''

for i in text:
    if i in chars:
        word += i

print word

# Output: http://www.pythonchallenge.com/pc/def/equality.html
test