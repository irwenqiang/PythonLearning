#列表推导式类似于数学有木有?!!

S = [x ** 2 for x in range(10)]
V = [2 ** i for i in range(10)]
M = [x for x in S if x % 2 == 0]
print S
print V
print M

print '---------------'
# 列表推导式可以相互嵌套
noprimes = [j for i in range(2, 8) for j in range(i * 2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print primes

print '---------------'
words = 'The quick brown fox jumps over the lazy dog'.split()
print words

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print i

