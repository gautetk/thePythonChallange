from collections import defaultdict

d_char = defaultdict(str)

f = open('input_pc3', 'r')

for line in f:
    for i in line:
        if i in d_char:
            d_char[i] += 1
        else:
            d_char[i] = 1

chars = ''
for key, value in d_char.iteritems():
    if value < 4:
        chars += key

print chars
word = ''
f = open('input_pc3', 'r')
for line in f:
    for i in line:
        if i in chars:
            word += i

print word
f.close()

# Output: http://www.pythonchallenge.com/pc/def/equality.html
