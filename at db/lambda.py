foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print filter(lambda x: x % 3 == 0,foo)

print map(lambda x: x * 2 + 10, foo)

print reduce(lambda x, y: x + y, foo)

total = 0;
for i in range(0, len(foo)):
    total += foo[i]


print '---------------------------------------------'

a = [1, 2, 3]
b = [1, 3, 2]

c = [2, 1, 3]

d = map(lambda x, y, z: x + y + z, a, b, c)

print '---------------------------------------------'

sentence = 'It is raining cats and dogs'
words = sentence.split()

print words

lengths = map(lambda word:len(word),words)

print lengths
