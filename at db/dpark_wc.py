from dpark import DparkContext

def word_count(file_path, word):
    dpark = DparkContext()
    f = dpark.textFile(file_path, splitSize = 16 << 20)

    print word, 'count:', f.map(lamba line:line.strip()).filter(lambda line:word in line).count()
    
