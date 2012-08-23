fobj = open("ad_lesbiam.txt")

for line in fobj:
    print line.rstrip()
fobj.close()

print '-----------'
fobj_in = open("ad_lesbiam.txt")
fobj_out = open("ad_lesbiam2.txt", "w")

i = 1
for line in fobj_in:
    print line.rstrip()
    fobj_out.write(str(i) + ":" + line)
    i = i + 1

fobj_in.close()
fobj_out.close()

print '-----------'
poem = open("ad_lesbiam.txt").readlines()
print poem[0],
print poem[1],
print poem[2],
print poem[3],
print poem[4],

print '-----------'
poem = open("ad_lesbiam.txt").read()
print poem[16:24]

print type(poem)

print '-----------'
import pickle
data = (1.4, 42)
output = open('data.pkl', 'w')
pickle.dump(data, output)
output.close()

f= open('data.pkl')
data = pickle.load(f)
print data

