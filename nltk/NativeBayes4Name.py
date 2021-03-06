#def gender_features(word):
#    return {'last_letter': word[-1]}

def gender_features(word):
    return {'suffix1':word[-1:], 'suffix2':word[-2:]}
    #return {'last_letter': word[-1]}

from nltk.corpus import names
import random
import nltk

names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])

random.shuffle(names)

train_names = names[1500:]
devtest_names = names[500:1500]
test_names = names[:500]

train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
test_set = [(gender_features(n), g) for (n,g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier, devtest_set)

errors = []

for(name, tag) in devtest_names:
    
    guess = classifier.classify(gender_features(name))

    if guess != tag:
        errors.append((tag, guess,name))

for(tag, guess, name) in sorted(errors): # doctest:+ELLIPSIS +NORMALIZE_WEITESPACE
    print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)


