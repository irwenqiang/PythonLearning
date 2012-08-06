friendInfo = {
        'chenwq'    :   {'xmu', 'chenwq@gmail.com'},
        'ariel' :   {'yealink', 'ariel@yealink.com'},
        'chenwb'    :   {'guankou', 'chenwb@guankou.gov'}
    }

def printAll():
    for name, info in friendInfo.items():
        print 'Contact %s' % name
     
        i = 0
        for ou in info:
            if i % 2 == 0:
                print 'at %s '% ou
            elif i % 2 != 0:
                print 'via email:%s' % ou
            i = i + 1
        print '\n'

def findByName(name):
    if name in friendInfo:
        printInfoByName(friendInfo, name)
    else:
        print 'Cann\'t find %s ' % name


def printInfoByName(friendInfo, name):
    i = 0
    for ou in friendInfo[name]:
        if i % 2 == 0:
            print 'at %s '% ou,
        elif i % 2 != 0:
            print 'via email:%s' % ou
        i = i + 1

def updateByName(friendInfo, name, ou='xmu', email='chenwq@gmail.com'):
    if name in friendInfo:
        # 很方便的赋值...
        friendInfo[name] = ou,email
        print 'update success!'
    else:
        print 'Cann\'t find %s ' % name
        
