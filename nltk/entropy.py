import nltk
import math
s1 = ['male','male','male','male']
s2 = ['male','female','male','male']
s3 = ['female', 'male', 'female', 'male']

def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    print freqdist
    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    print probs
    return -sum([p * math.log(p, 2) for p in probs])

