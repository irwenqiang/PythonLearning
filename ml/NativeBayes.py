#Native Bayes

#Calculate the Prob. of class:cls
def P(data, cls_val, cls_name="class"):
    cnt = 0.0
    
    for e in data:
        if e[cls_name] == cls_val:
            cnt += 1
            
    return cnt / len(data)

#Calculate the Prob(attr/cls)
def PT(data, cls_val, attr_name, attr_val, cls_name="class"):
    cnt1 = 0.0
    cnt2 = 0.0
    
    for e in data:
        if e[cls_name] == cls_val:
            cnt1 += 1
        if e[attr_name] == attr_val:
            cnt2 += 1
            
    return cnt2 / cnt1

#Calculate the NB
def NB(data, test, cls_y, cls_n):
    PY = P(data, cls_y)
    PN = P(data, cls_n)

    for key, val in test.items():
        print key, val
        PY *= PT(data, cls_y, key, val)
        PN *= PT(data, cls_n, key, val)

    return {cls_y:PY, cls_n:PN}

if __name__ == "__main__":

#data
    data = [
        {"outlook":"sunny", "temp":"hot", "humidity":"high", "wind":"weak", "class":"no" },
        {"outlook":"sunny", "temp":"hot", "humidity":"high", "wind":"strong", "class":"no" },
        {"outlook":"overcast", "temp":"hot", "humidity":"high", "wind":"weak", "class":"yes" },
        {"outlook":"rain", "temp":"mild", "humidity":"high", "wind":"weak", "class":"yes" },
        {"outlook":"rain", "temp":"cool", "humidity":"normal", "wind":"weak", "class":"yes" },
        {"outlook":"rain", "temp":"cool", "humidity":"normal", "wind":"strong", "class":"no" },
        {"outlook":"overcast", "temp":"cool", "humidity":"normal", "wind":"strong", "class":"yes" },
        {"outlook":"sunny", "temp":"mild", "humidity":"high", "wind":"weak", "class":"no" },
        {"outlook":"sunny", "temp":"cool", "humidity":"normal", "wind":"weak", "class":"yes" },
        {"outlook":"rain", "temp":"mild", "humidity":"normal", "wind":"weak", "class":"yes" },
        {"outlook":"sunny", "temp":"mild", "humidity":"normal", "wind":"strong", "class":"yes" },
        {"outlook":"overcast", "temp":"mild", "humidity":"high", "wind":"strong", "class":"yes" },
        {"outlook":"overcast", "temp":"hot", "humidity":"normal", "wind":"weak", "class":"yes" },
        {"outlook":"rain", "temp":"mild", "humidity":"high", "wind":"strong", "class":"no" },
        ]
    
    #calculate
    print NB(data,{"outlook":"sunny","temp":"cool","humidity":"high","wind":"strong"},"yes","no")
